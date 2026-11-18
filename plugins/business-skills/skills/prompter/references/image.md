# Prompts pour la génération et la retouche d'image

- **Ordre de description**, du plus important au détail : sujet (apparence, pose, expression) →
  action → décor → composition et cadrage (type de plan, angle, point de vue) → éclairage →
  style ou médium (photo, aquarelle, rendu 3D, illustration vectorielle…) → palette et ambiance
  → détails techniques si photoréaliste (focale, profondeur de champ, grain).
- Écris une description visuelle continue plutôt qu'une pile de mots-clés, sauf si l'outil
  fonctionne mieux par tags (certains modèles Stable Diffusion).
- **Texte dans l'image** : texte exact entre guillemets, avec police, taille relative et
  emplacement.
- **Format** : ratio adapté à l'usage (1:1 réseau social, 16:9 bannière, 9:16 story, 2:3
  affiche…).
- **Exclusions** : si l'outil a un champ dédié (prompt négatif, `--no`), fournis-les à part.
  Sinon, décris positivement ce que tu veux.
- **Paramètres propres à l'outil** (ex. Midjourney : `--ar`, `--style raw`, `--stylize`) :
  n'ajoute que ceux dont tu connais la syntaxe valide pour l'outil nommé. Un paramètre inventé
  casse le prompt.
- **Style** : décris-le par ses caractéristiques (technique, palette, époque, mouvement) plutôt
  que par le nom d'un artiste vivant ou d'une marque. C'est plus précis et plus souvent accepté.
- **Retouche d'une image fournie** : précise ce qui change et ce qui doit rester identique
  (visage, cadrage, lumière, arrière-plan…).
