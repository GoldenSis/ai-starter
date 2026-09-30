# AI Starter

Un plugin pour Claude qui met une entreprise au travail avec l'IA sans consultant au téléphone. Vous l'installez, vous lancez une commande, vous répondez à quelques questions par écrit. À la fin, Claude connaît votre entreprise, vous avez un audit écrit des tâches qui mangent votre semaine, et une première compétence tourne sur celle dont vous paieriez le plus cher pour être débarrassé.

Par [Plus de Fun Agency](https://plusdefun.ch), Genève. Version anglaise : [README.md](README.md).

## Ce que ça fait

Sept étapes, chacune reprenable. Vous pouvez arrêter quand vous voulez et revenir.

| Étape | Ce qui se passe | Ce que vous donnez |
|---|---|---|
| 0 | Accueil, et votre accord sur ce qui sera lu | un oui |
| 1 | Connexion de vos outils (mail, agenda, documents, messagerie) | lesquels vous utilisez |
| 2 | Entretien | sept réponses courtes, par écrit |
| 3 | Quatre fichiers de contexte pour que Claude connaisse votre entreprise et écrive comme vous | l'autorisation de lire dix mails envoyés, ou trois phrases tapées sur le moment |
| 4 | Analyse des tâches : mails envoyés et agenda échantillonnés, tâches récurrentes trouvées et notées | l'autorisation pour l'échantillon |
| 5 | Première compétence : la tâche écrite noir sur blanc, allégée, transformée en compétence, testée sur un vrai exemple | un vrai exemple et le résultat que vous en aviez tiré |
| 6 | Registre : tout ce qui a été construit, où ça se trouve, comment le lancer | rien |

## Ce que ça ne fait jamais

Ça n'envoie jamais un mail ni un message, ne paie rien, ne supprime rien. Ça rédige ; vous envoyez. Rien de ce qui est lu ne sort de votre compte Claude. Plus de Fun ne voit aucune de vos données. Les mots de passe, clés et coordonnées bancaires sont écartés s'ils apparaissent dans ce que vous collez.

## Installation

Dans Claude Code :

```
/plugin marketplace add GoldenSis/ai-starter
/plugin install ai-starter@plusdefun
```

Puis, dans le dossier où vous voulez que les fichiers vivent :

```
/ai-starter:start
```

`/ai-starter:status` montre où vous en êtes. `/ai-starter:start 5` relance une étape. `/ai-starter:start reset` repart de zéro sans effacer ce qui a été construit.

Dans Claude Cowork ou l'application de bureau, ajoutez le plugin depuis le même dépôt via Réglages, Plugins.

## Où vont les fichiers

Tout atterrit dans `ai-starter/` à l'intérieur de votre dossier de projet :

```
ai-starter/
  state.json          où vous en êtes
  tools.md            ce qui est connecté
  interview.md        vos réponses, mot pour mot
  context/            company.md · brand-voice.md · preferences.md
  CLAUDE.md           le court fichier d'instructions qui pointe vers eux
  process-audit.md    les tâches trouvées, notées, une recommandée
  skills/<tâche>/     audit.md · SKILL.md · test.md
  ledger.md           ce qui a été construit, en clair
```

## Langues

Il répond dans la langue dans laquelle vous écrivez, et rédige les fichiers de contexte dans cette langue.

## Aide

Pour une construction plus grande qu'une compétence : arnaud.chretien@plusdefun.ch.

## Licence

MIT.
