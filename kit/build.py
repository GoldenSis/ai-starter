#!/usr/bin/env python3
"""Build the single-file kits (kit/AI-STARTER.md, kit/AI-STARTER.fr.md) from skills/.

The skills are the only source of truth. This script strips their frontmatter,
puts them in order behind a short header for chat assistants, and appends the
templates. Run it after any change under skills/ and commit the output.

    python3 kit/build.py          write the kits
    python3 kit/build.py --check  exit 1 if a kit is out of date
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
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
- **State.** You may not see earlier chats. At the end of each step, print a three-line status block (steps done, chosen task, date) and ask the owner to paste it back when they return.
- **Skills.** When a step says "load the X skill", go to the section of that name below.
- **Scripts.** You probably cannot run the Python check. Make its checks by reading.
- **Mail and calendar.** If you cannot reach them, use the paste route in the process scan section.
- **Paths** such as `templates/company.md` refer to the templates at the end of this file.

Reply in the language the owner writes in.
""",
    "fr": """# AI Starter · tout le parcours en un seul fichier

Généré depuis le dossier `skills/` de https://github.com/GoldenSis/ai-starter par `kit/build.py`. À ne pas modifier à la main.

Le parcours ci-dessous est rédigé en anglais, la langue dans laquelle il est maintenu. L'assistant le lit sans difficulté et vous répondra en français si vous lui écrivez en français ; les fichiers de contexte seront eux aussi rédigés en français.

## Pour l'assistant qui lit ce fichier

You are running AI Starter with a business owner, in a chat (ChatGPT, Gemini, Perplexity, DeepSeek, Mistral Le Chat, claude.ai or any other). The owner writes in French: reply in French, in a courteous register that prefers the conditional ("vous pourriez", "il serait utile") to bare imperatives. Adapt the playbook this way:

- **Start, resume, status.** "Lance AI Starter", "AI Starter étape 3" and "où en est AI Starter" mean start, step 3 and status: follow *Start, resume, status* in the onboarding section.
- **Files.** When a step says to write a file, show it in one code block with its file name on the line above, and ask the owner to save it (in a ChatGPT project, a Gemini Gem or a Perplexity Space, they can add it to the files there).
- **State.** You may not see earlier chats. At the end of each step, print a three-line status block (steps done, chosen task, date) and ask the owner to paste it back when they return.
- **Skills.** When a step says "load the X skill", go to the section of that name below.
- **Scripts.** You probably cannot run the Python check. Make its checks by reading.
- **Mail and calendar.** If you cannot reach them, use the paste route in the process scan section.
- **Paths** such as `templates/company.md` refer to the templates at the end of this file.
""",
}

TEMPLATES_TITLE = {"en": "Templates", "fr": "Modèles (templates)"}


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
        # The skill's own title becomes the section heading, tagged with the skill name.
        parts.append(re.sub(r"^## (.+)$", rf"## \1 · skill `{name}`", body(SKILLS / name / "SKILL.md"), count=1, flags=re.M))
    tpl = [f"## {TEMPLATES_TITLE[lang]}"]
    for name in ORDER:
        for f in sorted((SKILLS / name / "templates").glob("*.md")):
            content = f.read_text(encoding="utf-8").strip()
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
