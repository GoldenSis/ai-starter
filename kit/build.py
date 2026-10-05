#!/usr/bin/env python3
"""Build the single-file kits (kit/AI-STARTER.md, kit/AI-STARTER.fr.md).

The English kit comes from skills/, the source of truth for agents. The French
kit comes from kit/fr/: a native French copy of each SKILL.md body
(kit/fr/<skill>.md) and of each template (kit/fr/templates/<file>). When you
change a skill or a template, change its French copy in the same commit.
The script strips frontmatter, puts the bodies in order behind a short header
for chat assistants, and appends the templates. Commit the output.

    python3 kit/build.py          write the kits
    python3 kit/build.py --check  exit 1 if a kit is out of date
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
FR = ROOT / "kit" / "fr"
ORDER = [
    "ai-starter-onboarding",
    "ai-starter-process-scan",
    "ai-starter-first-skill",
    "ai-starter-skill-check",
]

HEADER = {
    "en": """# AI Starter · the whole playbook in one file

Generated from the `skills/` folder of https://github.com/GoldenSis/ai-starter by `kit/build.py`. Do not edit by hand.

## For the assistant reading this

You are running AI Starter with a business owner, in a chat (ChatGPT, Gemini, Perplexity, DeepSeek, Mistral Le Chat, claude.ai or any other). The playbook below was written for assistants that can write files; adapt it this way:

- **Start, resume, status.** When the owner says "start AI Starter", "AI Starter step 3" or "AI Starter status", follow *Start, resume, status* in the onboarding section.
- **Files.** When a step says to write a file, show it in one code block with its file name on the line above, and ask the owner to save it (in a ChatGPT project, a Gemini Gem or a Perplexity Space, they can add it to the files there).
- **State.** You may not see earlier chats. At the end of each step, print a three-line status block (steps done, chosen task, date) and ask the owner to paste it back when they return. Never show `ai-starter/state.json` or any other progress file in the chat: this short block replaces it.
- **Skills.** When a step says "load the X skill", go to the section of that name below.
- **Scripts.** You probably cannot run the Python check. Make its checks by reading.
- **Mail and calendar.** If you cannot reach them, use the paste route in the process scan section.
- **Paths** such as `templates/company.md` refer to the templates at the end of this file.

Reply in the language the owner writes in.
""",
    "fr": """# AI Starter · tout le parcours en un seul fichier

Généré par `kit/build.py` à partir du dossier `kit/fr/` de https://github.com/GoldenSis/ai-starter. À ne pas modifier à la main.

## Pour l'IA qui lit ce fichier

Vous conduisez le parcours AI Starter avec la personne qui dirige une entreprise, dans une conversation (ChatGPT, Gemini, Perplexity, DeepSeek, Mistral Le Chat, claude.ai ou une autre). Elle écrit en français : répondez en français, avec un registre courtois qui préfère le conditionnel (« vous pourriez », « il serait utile ») aux impératifs secs. Le parcours ci-dessous a été écrit pour une IA capable d'écrire des fichiers ; adaptez-le ainsi :

- **Démarrer, reprendre, faire le point.** « Lance AI Starter », « AI Starter étape 3 » et « où en est AI Starter » veulent dire démarrer, faire l'étape 3 et faire le point : suivez *Démarrer, reprendre, faire le point* dans la première section.
- **Fichiers.** Quand une étape demande d'écrire un fichier, montrez-le dans un seul bloc de code, avec son nom sur la ligne du dessus, et proposez à la personne de l'enregistrer (dans un Projet ChatGPT, un Gem Gemini ou un Space Perplexity, elle pourrait l'ajouter aux fichiers).
- **Où l'on en est.** Vous ne voyez peut-être pas les conversations précédentes. À la fin de chaque étape, affichez un bloc de trois lignes (étapes faites, tâche choisie, date) et proposez à la personne de vous le recoller à son retour. N'affichez jamais `ai-starter/state.json` ni aucun autre fichier de suivi dans la conversation : ce petit bloc le remplace.
- **Sections.** Quand une étape renvoie à une section, par exemple `ai-starter-process-scan`, passez à la section qui porte ce nom plus bas.
- **Script.** Vous ne pouvez probablement pas lancer le contrôle en Python. Faites ses vérifications en lisant.
- **Mails et agenda.** Si vous ne pouvez pas les atteindre, passez par le copier-coller décrit dans la section `ai-starter-process-scan`.
- **Chemins.** Les chemins comme `templates/company.md` renvoient aux modèles en fin de fichier.
- **Mots simples.** Avec la personne, dites « routine », « votre IA » et « récapitulatif », jamais « skill », « compétence », « plugin », « agent », « connecteur » ni « registre ».
""",
}

TEMPLATES_TITLE = {"en": "Templates", "fr": "Modèles"}
SECTION_TAG = {"en": "skill", "fr": "section"}


def body(skill_md):
    text = skill_md.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        text = text[end + 4:]
    text = text.strip()
    # Demote headings one level so each skill sits under its own "## <name>" section.
    return re.sub(r"^(#{1,5}) ", r"#\1 ", text, flags=re.M)


def build(lang):
    parts = [HEADER[lang].strip()]
    for name in ORDER:
        src = SKILLS / name / "SKILL.md" if lang == "en" else FR / f"{name}.md"
        # The skill's own title becomes the section heading, tagged with the skill name.
        parts.append(re.sub(r"^## (.+)$", rf"## \1 · {SECTION_TAG[lang]} `{name}`", body(src), count=1, flags=re.M))
    tpl = [f"## {TEMPLATES_TITLE[lang]}"]
    for name in ORDER:
        for f in sorted((SKILLS / name / "templates").glob("*.md")):
            # Every English template needs its French copy; a missing one stops the build.
            src = f if lang == "en" else FR / "templates" / f.name
            content = src.read_text(encoding="utf-8").strip()
            tpl.append(f"### templates/{f.name}\n\n````markdown\n{content}\n````")
    parts.append("\n\n".join(tpl))
    return "\n\n".join(parts) + "\n"


def main(argv):
    stale = False
    for lang, out in (("en", "AI-STARTER.md"), ("fr", "AI-STARTER.fr.md")):
        path = ROOT / "kit" / out
        text = build(lang)
        if "--check" in argv:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                print(f"{path.relative_to(ROOT)} is out of date; run python3 kit/build.py")
                stale = True
        else:
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)} ({len(text.splitlines())} lines)")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
