# AI Starter

[English](README.md) · **Français**

Votre IA apprend votre entreprise en une demi-heure environ, puis prend en charge une tâche répétitive à votre place.
Vous repartez avec une IA qui connaît votre activité et écrit comme vous, la liste des tâches qu'elle pourrait faire, et une tâche qu'elle fait déjà.
Pour les dirigeants et les petites équipes, sans rien de technique à connaître. Fonctionne avec ChatGPT, Gemini, Claude et les autres.

### ➜ Commencer ici (sans installation) : https://plusdefun.ch/fr/ai-starter/

## Comment ça marche, en 3 étapes

1. **Vous donnez un fichier à votre IA** : ChatGPT, Gemini, Claude…
2. **Elle vous pose des questions simples**, pendant une trentaine de minutes.
3. **Elle prend en charge une première tâche répétitive**, testée sur un exemple réel.

Vous pouvez vous arrêter à tout moment et reprendre plus tard.

## Ce que vous obtenez

- **Une IA qui connaît votre entreprise et écrit comme vous.** Votre offre, vos clients, votre ton, vos formules habituelles.
- **La liste des tâches qu'elle pourrait faire pour vous**, classées selon le temps qu'elles vous prennent chaque semaine.
- **Une tâche qu'elle fait désormais pour vous**, testée sur un cas réel de votre semaine. Devis, relances, réponses à la même question : celle dont vous seriez le plus heureux d'être débarrassé.

## Ce qu'elle ne fait jamais

- Elle n'envoie aucun mail ni message. Elle prépare des brouillons ; c'est vous qui envoyez.
- Elle ne paie rien et ne supprime rien.
- Elle ne lit rien sans votre accord. Vos données restent dans votre propre compte ; Plus de Fun n'en voit aucune.
- Les mots de passe et coordonnées bancaires sont écartés s'ils apparaissent.

## Vous préférez vous lancer seul ?

1. Il suffit de télécharger [`kit/AI-STARTER.fr.md`](kit/AI-STARTER.fr.md) (la flèche de téléchargement, en haut à droite de la page du fichier).
2. Ouvrez ensuite votre IA, joignez-lui le fichier et collez le message de départ, que vous trouverez dans [`kit/START-PROMPT.md`](kit/START-PROMPT.md).
3. Répondez à ses questions. Pour reprendre plus tard, il suffit d'écrire **lance AI Starter**.

Si votre IA ne peut pas lire votre messagerie, elle vous proposera plutôt de coller une vingtaine de mails envoyés récemment.

## Aide

Par [Plus de Fun Agency](https://plusdefun.ch), Genève. Pour un projet plus vaste : arnaud.chretien@plusdefun.ch.

Licence : MIT.

## Pour les développeurs

### Claude Code (plugin)

```
/plugin marketplace add GoldenSis/ai-starter
/plugin install ai-starter@plusdefun
```

Il suffit ensuite de lancer `/ai-starter:start` dans le dossier où les fichiers devraient se trouver. `/ai-starter:status` indique où vous en êtes, `/ai-starter:check` relit une skill, `/ai-starter:start 5` relance une étape, `/ai-starter:start reset` repart de zéro sans effacer ce qui a été construit. Dans Claude Cowork ou l'application de bureau, le plugin peut s'ajouter depuis le même dépôt via Réglages, Plugins.

### Codex, Pi, Hermes, et tout agent qui lit les skills SKILL.md

```
git clone https://github.com/GoldenSis/ai-starter
sh ai-starter/install.sh --dry-run   # pour voir ce qu'il ferait
sh ai-starter/install.sh
```

Le script repère les agents présents sur la machine et copie les quatre skills dans le dossier de chacun (`--link` crée des liens plutôt que des copies, `--uninstall` les retire). Il ne remplace jamais une autre skill du même nom, sauf avec `--force`.

| Outil | Dossier des skills | Source |
|---|---|---|
| Claude Code | `~/.claude/skills` | documentation Claude Code, Skills |
| Codex | `~/.agents/skills` | documentation OpenAI Codex, Skills |
| Pi | `~/.agents/skills` (lit aussi `~/.pi/agent/skills`) | documentation Pi, `skills.md` |
| Hermes | `~/.hermes/skills` | documentation Hermes, Skills |

Codex et Pi partagent `~/.agents/skills` : le script n'y dépose donc qu'une copie, car une seconde dans `~/.pi/agent/skills` provoquerait chez Pi un avertissement de doublon. L'ancien dossier `~/.codex/skills` ne figure plus dans la documentation de Codex pour les skills personnelles ; le script n'y touche pas.

En dehors de Claude Code, pas de commande à retenir : il suffit d'écrire **lance AI Starter**, **où en est AI Starter**, **AI Starter étape 5** ou **vérifie mes routines**.

**Windows :** il suffirait de copier les quatre dossiers de `skills\` dans `%USERPROFILE%\.claude\skills`, `%USERPROFILE%\.agents\skills` ou `%USERPROFILE%\.hermes\skills`, selon l'agent utilisé.

### IA de conversation : Projets, Gems, Spaces

Tout le parcours tient dans un fichier, entièrement en français : [`kit/AI-STARTER.fr.md`](kit/AI-STARTER.fr.md). Le message à coller se trouve dans [`kit/START-PROMPT.md`](kit/START-PROMPT.md).

- **ChatGPT :** vous pourriez créer un Projet (ou un GPT personnalisé), coller le message de départ dans ses instructions et y ajouter le fichier.
- **Gemini :** même principe avec un Gem, le fichier étant ajouté sous Knowledge. Google annonce que les Gems des comptes personnels deviendront des skills à partir de novembre 2026.
- **Perplexity :** même principe avec un Space.
- **DeepSeek, Mistral Le Chat, claude.ai ou toute autre IA :** il suffit de coller le message de départ et de joindre le fichier.

### Les sept étapes, pour référence

Chaque étape peut se reprendre. Avec la personne, le parcours dit « routine » pour une skill et « récapitulatif » pour le registre (`ledger.md`).

| Étape | Ce qui se passe | Ce que la personne donne |
|---|---|---|
| 0 | Accueil, et accord sur ce qui sera lu | un oui |
| 1 | Liens avec les outils (mail, agenda, documents, messagerie) | lesquels elle utilise |
| 2 | Entretien | sept réponses courtes, par écrit |
| 3 | Fichiers de contexte : entreprise, façon d'écrire, préférences | dix mails envoyés à lire, ou trois phrases tapées sur le moment |
| 4 | Liste des tâches récurrentes, notées | un échantillon de mails envoyés et d'agenda, ou une vingtaine de mails collés |
| 5 | Première routine : décrite, allégée, écrite, testée sur un vrai exemple ; une seconde IA peut la relire | un vrai exemple et le résultat obtenu |
| 6 | Récapitulatif : tout ce qui a été construit, où cela se trouve, comment le lancer | rien |

### Plusieurs IA ensemble

À l'étape 5, la routine terminée peut être confiée à une seconde IA, qui cherchera ce qui pourrait mal tourner ; le récapitulatif note quelle IA l'a construite et laquelle l'a relue. La routine est écrite en Markdown simple : le même fichier sert de SKILL.md pour un agent, d'instructions pour un Projet ou un GPT, de Gem ou de Space.

### Où vont les fichiers

```
ai-starter/
  state.json          où vous en êtes
  tools.md            ce qui est relié
  interview.md        vos réponses, mot pour mot
  context/            company.md · brand-voice.md · preferences.md
  AGENTS.md           le court fichier d'instructions qui pointe vers eux
  CLAUDE.md           une ligne, @AGENTS.md, pour que Claude Code lise les mêmes règles
  process-audit.md    les tâches trouvées, notées, une recommandée
  skills/<tâche>/     audit.md · SKILL.md · test.md
  ledger.md           le récapitulatif de ce qui a été construit
```

Dans une IA de conversation, l'IA affiche chaque fichier pour que vous puissiez l'enregistrer, ou l'ajouter au Projet, au Gem ou au Space.

### Pour les mainteneurs

Les skills de `skills/` sont la source pour les agents et pour le kit anglais. Le kit français est construit à partir des copies françaises de `kit/fr/` (une par skill, plus `kit/fr/templates/`) : les deux se modifient dans le même commit. Ensuite, `python3 kit/build.py` régénère les kits, `python3 kit/build.py --check` confirme qu'ils sont à jour, et `python3 skills/ai-starter-skill-check/scripts/skill_lint.py skills/` vérifie les skills.
