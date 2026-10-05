# Contrôle d'une routine

La moitié du contrôle est mécanique : un script s'en charge et donne la même réponse à chaque fois. L'autre moitié demande du jugement, et c'est à vous de la faire en lisant la routine. Ne changez rien tant que la personne n'a pas donné son accord. Avec elle, dites « routine », jamais « skill ».

## 1 · Lancer le script

```
python3 scripts/skill_lint.py <dossier de la routine ou dossier de routines>
```

Le script n'a besoin que de Python 3, rien à installer. Cible par défaut : `ai-starter/skills/` dans le dossier courant, puis `.claude/skills/` et `.agents/skills/`. Si vous ne pouvez pas lancer de script (une IA de conversation), faites les mêmes contrôles en lisant. Il signale :

- **FAIL** : pas de `SKILL.md`, un `name` absent ou mal formé, une `description` absente ou de plus de 1 024 caractères, un corps de plus de 500 lignes.
- **WARN** : un fichier atteint depuis `SKILL.md` qui dépasse 100 lignes sans sommaire en tête ; un fichier atteint seulement via un autre fichier, que l'IA risque de ne faire que survoler ; un module Python importé sans ligne d'installation dans `SKILL.md`.
- **NOTE** : des règles propres à Claude, comme les mots `claude` ou `anthropic` dans un nom, refusés lors d'un envoi sur claude.ai ou l'API Claude. Les autres outils les acceptent : une NOTE ne fait donc jamais échouer une routine.

## 2 · Lire ce qu'un script ne peut pas juger

Lisez `SKILL.md` et chaque fichier qu'il cite. Pour chaque étape, posez la question : que se passe-t-il si l'IA la fait autrement la prochaine fois ?

- **Pas grand-chose** (rédiger, résumer, choisir ses mots) : des instructions simples suffisent. Si l'étape est trop détaillée, avec des majuscules, des « TOUJOURS » ou de longues listes de cas particuliers, proposez de la couper. Les modèles actuels réussissent moins bien avec les routines anciennes et trop directives.
- **Quelque chose de sérieux** (de l'argent, une suppression, un envoi, tout ce qu'un client voit) : l'étape demande une commande exacte ou un script, ou une règle qui confie le cas à un humain. La prose seule ne suffit pas.
- **L'ordre compte** (vérifier les données avant d'en tirer le rapport) : la routine devrait contenir une courte liste à cocher que l'IA recopie et suit, et une étape de vérification qui la renvoie en arrière en cas d'échec (« si un chiffre ne correspond pas, revenir à l'étape 2 »).

## 3 · Rendre compte, puis attendre

Affichez un seul tableau : constat, fichier, pourquoi c'est important, changement proposé. D'abord les FAIL, puis les WARN, puis les NOTE, puis les constats de lecture. Passez sous silence ce qui va bien, et dites combien de contrôles sont passés.

Demandez à la personne quels changements faire. Ne faites que ceux-là, relancez le script, et montrez les nombres avant et après. Ne touchez jamais à une routine venue du plugin de quelqu'un d'autre ; faites le constat et arrêtez-vous.
