# Prompts pour modèles de texte et de code

- **Rôle** : donne un rôle d'expert précis et pertinent, jamais générique.
- **Contexte et motivation** : explique pourquoi chaque contrainte existe. Le modèle généralise
  mieux quand il comprend l'intention.
- **Structure** : sépare les sections (contexte, tâche, contraintes, format de sortie, exemples,
  données). Balises XML pour Claude ; pour les autres modèles, titres Markdown ou balises XML
  (les deux sont bien compris). Place toujours les données à traiter dans un bloc délimité,
  séparé des instructions.
- **Format de sortie** : précise structure, longueur, ton, langue et format (Markdown, JSON,
  tableau, code…).
- **Exemples** : quand le style ou le format compte, ajoute 1 à 3 exemples variés, en précisant
  qu'ils illustrent et ne sont pas à copier.
- **Raisonnement** : pour les tâches complexes (analyse, décision, débogage, architecture),
  demande au modèle de réfléchir étape par étape avant sa réponse finale.
- **Critères de réussite** : termine par une liste vérifiable de ce qui fait un excellent
  résultat, et demande au modèle de vérifier son travail avant de le livrer.
- **Clarification en aval** : si la tâche est ambiguë par nature, demande au modèle de poser ses
  questions avant de commencer.
- **Assistant réutilisable** : si la demande porte sur un assistant durable (API, GPT
  personnalisé, Gem, Projet), fournis un prompt système et un exemple de premier message
  utilisateur.

## Selon le type de tâche

- **Code** : stack et versions, conventions, gestion des erreurs, tests, sécurité, plan avant
  l'implémentation, critères d'acceptation.
- **Rédaction** : destinataire, objectif, ton, longueur, appel à l'action.
- **Analyse et recherche** : question précise, sources, citations exigées, séparation entre faits
  et hypothèses.
- **Agent** : objectif final, outils disponibles, autonomie autorisée, moments où demander
  confirmation, définition de « terminé ».
