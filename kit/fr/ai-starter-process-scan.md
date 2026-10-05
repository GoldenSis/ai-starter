# Liste des tâches

But : une courte liste écrite, `ai-starter/process-audit.md`, qui nomme les trois tâches récurrentes qu'il vaudrait le plus la peine de confier à l'IA, et en choisit une pour commencer. Des preuves plutôt que des opinions : chaque tâche candidate indique où elle a été vue.

## D'abord l'accord

Dites en un seul message ce que vous lirez, et attendez le oui :

- les 100 derniers mails envoyés (objet, destinataires, premières lignes ; le reste du texte n'est pas nécessaire),
- les quatre dernières semaines d'agenda (titres, durées, nombre de participants),
- tout dossier que la personne indique.

Si elle refuse une source, passez-la. Si elle refuse tout, établissez la liste à partir de l'entretien seul et notez « entretien seul ».

## Lecture

Utilisez les liens disponibles dans cette conversation (Gmail, Google Agenda, Microsoft 365, Drive, ou ce que l'étape 1 a confirmé). Ne lisez que ce qui a été accepté. N'envoyez, n'étiquetez, n'archivez et ne modifiez jamais rien. Gardez l'échantillon brut hors du fichier : la liste contient des nombres et des tendances, pas les mails eux-mêmes.

Si aucun lien n'atteint la messagerie ou l'agenda, ne vous arrêtez pas. Proposez le copier-coller : « Pourriez-vous coller ou joindre une vingtaine de vos mails envoyés récemment (l'objet, le destinataire et les premières lignes suffisent) et un export de votre agenda des deux dernières semaines ? » Un export d'agenda, c'est le fichier `.ics` que Google Agenda ou Outlook peut enregistrer, ou une capture d'écran de la vue semaine. Invitez la personne à retirer ce qu'elle ne voudrait pas voir lu avant de coller. Notez « échantillon collé » et utilisez les petits nombres tels quels.

Ce que chaque IA de conversation peut atteindre, d'après ses propres pages d'aide (à revérifier si le menu a changé) :

- ChatGPT : Gmail, Google Agenda, et la messagerie et l'agenda Outlook, via Réglages, Connecteurs. Un Projet contient des instructions et des fichiers ; un GPT personnalisé, des instructions et des fichiers de connaissance.
- Gemini : Gmail, Agenda et Drive via l'application Google Workspace (le réglage d'activité, « Keep Activity », doit être activé). Un Gem contient des instructions et des fichiers. Google annonce que les Gems des comptes personnels deviendront des skills à partir de novembre 2026.
- Perplexity : Gmail avec Google Agenda, et Outlook.com, via Réglages, Connecteurs ; un seul agenda principal. Un Space contient des instructions et des fichiers.
- DeepSeek : aucun lien avec la messagerie ou l'agenda trouvé dans sa documentation, donc copier-coller.
- Mistral Le Chat, claude.ai et les autres : non vérifiés ici. Demandez à la personne ce que son IA affiche sous Connecteurs ou Applications ; s'il n'y a rien, copier-coller.

## Regroupement

Regroupez ce que vous avez vu en tâches récurrentes. Une tâche est récurrente si elle apparaît au moins trois fois dans l'échantillon, ou une fois par semaine dans l'agenda. Regroupements typiques : répondre au même genre de demande, envoyer le même document, relancer un paiement ou une signature, préparer le même rapport, caler des rendez-vous, faire un devis, assurer le suivi après une réunion.

Pour chaque groupe, notez : en quoi consiste la tâche, sa fréquence (par semaine), le nombre approximatif de minutes à chaque fois, qui la fait, avec quel outil, et la preuve (par exemple « 14 mails envoyés avec "devis" dans l'objet, sur 4 semaines »).

## Notation

Trois colonnes, chacune de 1 à 5 :

- **Charge** : les heures par semaine qu'elle coûte (minutes × fréquence).
- **Répétition** : à quel point chaque occurrence ressemble à la précédente. Une tâche différente à chaque fois obtient 1.
- **Portée** : l'IA peut-elle la faire avec les liens disponibles, sans rien envoyer d'elle-même ? Une tâche qui demande un outil non relié obtient 1 tant qu'il ne l'est pas.

Classez par le produit des trois. En cas d'égalité, la tâche citée par la personne à la question 4 de l'entretien l'emporte.

## Résultat

Écrivez `ai-starter/process-audit.md` à partir de `templates/process-audit.md` :

1. Les sources lues, avec les nombres, et ce qui a été refusé.
2. Le tableau de tous les groupes trouvés (tâche, par semaine, minutes, outil, preuve).
3. Les trois premières tâches avec leurs notes, et pour chacune deux lignes sur ce que ferait la routine et ce qui reste à un humain.
4. La recommandation : une tâche, une phrase pour dire pourquoi, et ce que la personne devra fournir à l'étape 5 (un exemple réel de ce qui arrive, le résultat attendu, la règle pour les cas particuliers).

Présentez les trois premières dans un tableau et demandez laquelle construire. Ne commencez pas à construire ici.
