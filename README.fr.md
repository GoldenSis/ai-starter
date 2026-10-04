# AI Starter

Fonctionne avec n'importe quelle IA : Claude, ChatGPT, Gemini, Perplexity, DeepSeek, Codex, Pi, Hermes — une seule ou plusieurs ensemble.

AI Starter aide une entreprise à se mettre au travail avec l'IA, sans consultant au téléphone. Vous répondez à quelques questions par écrit. À la fin, votre assistant connaît votre entreprise, vous disposez d'un audit écrit des tâches qui occupent votre semaine, et une première compétence prend en charge celle dont vous seriez le plus heureux d'être débarrassé.

Par [Plus de Fun Agency](https://plusdefun.ch), Genève. English version: [README.md](README.md).

## Ce que ça fait

Sept étapes, chacune reprenable. Vous pouvez vous arrêter quand vous le souhaitez et revenir plus tard.

| Étape | Ce qui se passe | Ce que vous donnez |
|---|---|---|
| 0 | Accueil, et votre accord sur ce qui sera lu | un oui |
| 1 | Connexion de vos outils (mail, agenda, documents, messagerie) | lesquels vous utilisez |
| 2 | Entretien | sept réponses courtes, par écrit |
| 3 | Fichiers de contexte, pour que votre assistant connaisse votre entreprise et écrive comme vous | l'autorisation de lire dix mails envoyés, ou trois phrases tapées sur le moment |
| 4 | Analyse des tâches : mails envoyés et agenda échantillonnés, tâches récurrentes repérées et notées | l'autorisation pour l'échantillon, ou une vingtaine de mails envoyés collés dans la conversation |
| 5 | Première compétence : la tâche décrite, allégée, transformée en compétence, testée sur un vrai exemple ; une seconde IA peut la relire | un vrai exemple et le résultat que vous en aviez tiré |
| 6 | Registre : tout ce qui a été construit, où cela se trouve, comment le lancer | rien |

## Ce que ça ne fait jamais

Rien n'est envoyé, payé ni supprimé. L'assistant rédige ; c'est vous qui envoyez. Ce qu'il lit reste dans votre propre compte, et Plus de Fun ne voit aucune de vos données. Les mots de passe, clés et coordonnées bancaires sont écartés s'ils apparaissent dans ce que vous collez.

## Installation

### Claude Code (plugin)

```
/plugin marketplace add GoldenSis/ai-starter
/plugin install ai-starter@plusdefun
```

Il suffit ensuite de lancer `/ai-starter:start` dans le dossier où les fichiers devraient se trouver. `/ai-starter:status` indique où vous en êtes, `/ai-starter:check` relit une compétence, `/ai-starter:start 5` relance une étape, `/ai-starter:start reset` repart de zéro sans effacer ce qui a été construit. Dans Claude Cowork ou l'application de bureau, le plugin peut s'ajouter depuis le même dépôt via Réglages, Plugins.

### Codex, Pi, Hermes, et tout agent qui lit les compétences SKILL.md

```
git clone https://github.com/GoldenSis/ai-starter
sh ai-starter/install.sh --dry-run   # pour voir ce qu'il ferait
sh ai-starter/install.sh
```

Le script repère les agents présents sur la machine et copie les quatre compétences dans le dossier de chacun (`--link` crée des liens plutôt que des copies, `--uninstall` les retire). Il ne remplace jamais une autre compétence du même nom, sauf avec `--force`.

| Outil | Dossier des compétences | Source |
|---|---|---|
| Claude Code | `~/.claude/skills` | documentation Claude Code, Skills |
| Codex | `~/.agents/skills` | documentation OpenAI Codex, Skills |
| Pi | `~/.agents/skills` (lit aussi `~/.pi/agent/skills`) | documentation Pi, `skills.md` |
| Hermes | `~/.hermes/skills` | documentation Hermes, Skills |

Codex et Pi partagent `~/.agents/skills` : le script n'y dépose donc qu'une copie, car une seconde dans `~/.pi/agent/skills` provoquerait chez Pi un avertissement de doublon. L'ancien dossier `~/.codex/skills` ne figure plus dans la documentation de Codex pour les compétences personnelles ; le script n'y touche pas.

En dehors de Claude Code, pas de commande à retenir : il suffit d'écrire **lance AI Starter**, **où en est AI Starter**, **AI Starter étape 5** ou **vérifie mes compétences**.

**Windows :** il suffirait de copier les quatre dossiers de `skills\` dans `%USERPROFILE%\.claude\skills`, `%USERPROFILE%\.agents\skills` ou `%USERPROFILE%\.hermes\skills`, selon l'agent utilisé.

### ChatGPT, Gemini, Perplexity, DeepSeek et les autres IA de conversation

Tout le parcours tient dans un fichier : [`kit/AI-STARTER.fr.md`](kit/AI-STARTER.fr.md). Le message à coller se trouve dans [`kit/START-PROMPT.md`](kit/START-PROMPT.md).

- **ChatGPT :** vous pourriez créer un Projet (ou un GPT personnalisé), coller le message de départ dans ses instructions et y ajouter le fichier.
- **Gemini :** même principe avec un Gem, le fichier étant ajouté sous Knowledge. Google annonce que les Gems des comptes personnels deviendront des skills à partir de novembre 2026.
- **Perplexity :** même principe avec un Space.
- **DeepSeek, Mistral Le Chat, claude.ai ou toute autre IA :** il suffit de coller le message de départ et de joindre le fichier.

Si l'assistant ne peut pas lire votre messagerie, l'analyse des tâches vous proposera plutôt de coller une vingtaine de mails envoyés récents et un export de deux semaines d'agenda.

## Plusieurs IA ensemble

À l'étape 5, la compétence terminée peut être confiée à une seconde IA, qui cherchera ce qui pourrait mal tourner ; le registre note quelle IA l'a construite et laquelle l'a relue. La compétence est écrite en Markdown simple : le même fichier sert de SKILL.md pour un agent, d'instructions pour un Projet ou un GPT, de Gem ou de Space.

## Où vont les fichiers

```
ai-starter/
  state.json          où vous en êtes
  tools.md            ce qui est connecté
  interview.md        vos réponses, mot pour mot
  context/            company.md · brand-voice.md · preferences.md
  AGENTS.md           le court fichier d'instructions qui pointe vers eux
  CLAUDE.md           une ligne, @AGENTS.md, pour que Claude Code lise les mêmes règles
  process-audit.md    les tâches trouvées, notées, une recommandée
  skills/<tâche>/     audit.md · SKILL.md · test.md
  ledger.md           ce qui a été construit, en clair
```

Dans une IA de conversation, l'assistant affiche chaque fichier pour que vous puissiez l'enregistrer, ou l'ajouter au Projet, au Gem ou au Space.

## Langues

L'assistant répond dans la langue dans laquelle vous lui écrivez, et rédige les fichiers de contexte dans cette même langue. Le parcours lui-même est maintenu en anglais.

## Pour les mainteneurs

Les compétences de `skills/` sont la seule source. Après une modification, `python3 kit/build.py` régénère le kit et `python3 skills/ai-starter-skill-check/scripts/skill_lint.py skills/` les vérifie.

## Aide

Pour un projet plus vaste qu'une compétence : arnaud.chretien@plusdefun.ch.

## Licence

MIT.
