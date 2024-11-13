# Backend

Le backend de ce projet est construit avec Django pour fournir des fonctionnalités de gestion des utilisateurs. Django est un framework web Python puissant et sécurisé, idéal pour construire des applications robustes et extensibles.

## Choix de Django

J'ai choisi Django pour ses capacités de gestion d'API REST, sa sécurité intégrée, et sa structure MVC, qui facilite le développement rapide d'applications web. De plus, Django offre un environnement sécurisé et fiable pour construire des API.

## Fonctionnalités

### Modèle Utilisateur :

Création d'un modèle User qui contient des informations telles que l'email, le nom complet, et le genre. Ce modèle est utilisé pour gérer les informations de base de chaque utilisateur.

### API de Gestion des Utilisateurs :

- **Inscription (signup)** : Permet de créer un nouvel utilisateur.
- **Connexion (signin)** : Permet aux utilisateurs de se connecter.
- **Modification de profil (edit)** : Permet aux utilisateurs de modifier leur profil.
- **Suppression de compte (delete)** : Supprime un utilisateur de la base de données.
- ajouter produit
- get produit

**Note** : Le projet n'utilise pas de tokens JWT pour l'authentification, car le développement a été concentré sur les fonctionnalités essentielles, sans la gestion avancée des sessions.

### Commandes

1. Appliquez les migrations pour préparer la base de données :
   ```bash
   python manage.py migrate
2. Lancez le serveur Django
   python manage.py runserver
