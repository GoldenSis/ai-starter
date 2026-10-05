# Première routine : observer, alléger, confier

N'automatisez jamais une tâche avant qu'elle ait été écrite et allégée. Un désordre automatisé n'est qu'un désordre plus rapide.

Avec la personne, appelez ce que vous construisez une « routine », jamais une skill, une compétence, un plugin ou un agent. `SKILL.md` reste le nom du fichier.

## 1 · Observer : comment c'est fait aujourd'hui

Demandez à la personne de décrire la tâche par écrit, étape par étape, comme elle l'a faite la dernière fois. Des étapes numérotées, une action chacune. Demandez un exemple réel de ce qui arrive (le mail, la demande, le fichier) et du résultat qu'elle a produit. Si les liens le permettent, proposez d'aller chercher vous-même le dernier exemple réel, et demandez-lui de confirmer qu'il est représentatif.

Écrivez les étapes dans `ai-starter/skills/<tache>/audit.md`. Comptez-les.

## 2 · Alléger : retirer ce qui n'apporte rien

Reprenez les étapes et marquez chacune : garder, fusionner, supprimer, ou confier à l'IA. Une étape se supprime quand son résultat ne sert jamais. Deux étapes fusionnent quand la seconde ne fait que remettre en forme la première. Proposez la liste raccourcie, avec le nombre d'étapes avant et après, et une ligne par changement. Demandez à la personne de confirmer ou de contester. C'est elle qui décide ; notez la liste finale.

Notez aussi la règle pour les cas que la routine ne doit pas traiter seule : une somme au-delà d'un montant, une réclamation, une question juridique, un nouveau client. Ces cas reviennent à un humain, et la routine le dit.

## 3 · Confier : écrire la routine

Écrivez `ai-starter/skills/<tache>/SKILL.md` à partir de `templates/skill-template.md`. Restez en Markdown simple, avec le court bloc d'en-tête en haut : le même fichier sert alors de skill pour Claude, Codex, Pi ou Hermes, et d'instructions à coller dans une IA de conversation, un Projet ChatGPT ou un GPT personnalisé, un Gem Gemini ou un Space Perplexity.

- dans l'en-tête, un `name` et une `description` qui dit quand l'utiliser, avec les mots de la personne,
- ce qui arrive (par où arrive la demande, quels éléments comptent),
- les étapes allégées, chacune comme une instruction à l'IA,
- la forme du résultat, avec l'exemple réel de la personne comme modèle,
- les règles de passage à un humain,
- ce que la routine ne fait jamais : elle n'envoie rien, ne paie rien, ne supprime rien. Elle rédige, et c'est la personne qui envoie.

Passez-la au contrôle (la section `ai-starter-skill-check` plus bas ; là où un script peut tourner, `python3 ../ai-starter-skill-check/scripts/skill_lint.py ai-starter/skills/<tache>`) et corrigez tout FAIL avant de continuer. Dans une IA de conversation qui ne peut pas lancer de script, faites ces contrôles en lisant.

Placez ensuite la routine là où l'IA de la personne la trouvera, et indiquez-lui le chemin. Demandez avant de copier.

- Claude Code : `.claude/skills/<tache>/` dans le projet, ou `~/.claude/skills/`. Cowork et l'application de bureau : le dossier de skills qu'elle utilise.
- Codex, Pi et les autres outils qui lisent le format Agent Skills : `.agents/skills/<tache>/` dans le projet, ou `~/.agents/skills/`.
- Hermes : `~/.hermes/skills/<tache>/`.
- Une IA de conversation (ChatGPT, Gemini, Perplexity, DeepSeek, Le Chat, claude.ai) : coller le fichier dans les instructions d'un Projet ChatGPT ou d'un GPT personnalisé, d'un Gem Gemini ou d'un Space Perplexity, ou le joindre au début d'une conversation. Donnez à la personne le texte à coller.

## 4 · Tester sur un exemple réel

Lancez la routine sur l'exemple réel de l'étape 1. Montrez le résultat à côté de celui que la personne avait produit. Demandez : est-ce juste, que changeriez-vous ? Corrigez et relancez une fois. Arrêtez-vous là ; un second tour, c'est pour demain, avec un second exemple.

Notez dans `ai-starter/skills/<tache>/test.md` : ce qui est arrivé, le résultat, l'avis de la personne, la date, et quelle IA a construit la routine.

## 5 · Facultatif : une seconde IA relit

Proposez-le une fois ; passez si la personne refuse. Une autre IA repère ce que la première tient pour acquis. Donnez à la personne ce texte à coller, avec le fichier de la routine, dans une autre IA (ChatGPT si vous êtes Claude, Claude ou Gemini si vous êtes ChatGPT, et ainsi de suite) :

> Voici une routine qu'une autre IA a écrite pour mon entreprise (des instructions pour une tâche répétitive). Merci de ne pas la réécrire. Pourriez-vous lister ce qui se passerait mal si vous l'appliquiez aux vrais cas de la semaine prochaine : une étape peu claire, un cas qu'elle ne couvre pas, tout ce qu'elle pourrait envoyer, payer ou supprimer sans moi ? Cinq points au plus, le plus grave en premier.

Quand la personne revient avec la réponse, corrigez seulement ce qu'elle approuve, et notez dans `test.md` quelle IA a relu la routine et ce qui a changé.

Revenez ensuite au parcours pour l'étape 6 ou, si cette section a été utilisée seule, indiquez où se trouvent les fichiers et comment lancer la routine.
