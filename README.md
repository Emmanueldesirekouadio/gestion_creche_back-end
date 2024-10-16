

# Plateforme de Gestion de Crèche - Back-End

Ce projet constitue la partie back-end de la plateforme de gestion de crèche, développée avec **Django REST Framework (DRF)**. Il gère les API, les utilisateurs, les paiements, ainsi que les données relatives aux enfants, éducateurs et administrateurs.

## Développeurs Back-End

- **Kevin Laubhouet**
- **Togo Soumaila**
- **Kouadio Tia Emmanuel** (Lead, intervenant sur les deux parties)

## Prérequis

- **Python 3.8** ou supérieur
- **Django 3.2** ou supérieur
- **Django REST Framework**
- **PostgreSQL** (ou une autre base de données compatible)

## Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/nom-utilisateur/gestion_creche_back-end.git
   ```

2. **Accéder au répertoire du projet :**
   ```bash
   cd gestion_creche_back-end
   ```

3. **Créer un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Windows, utilisez venv\Scripts\activate
   ```

4. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

## Lancer le projet

1. **Appliquer les migrations de base de données :**
   ```bash
   python manage.py migrate
   ```

2. **Créer un super utilisateur pour accéder à l'interface d'administration :**
   ```bash
   python manage.py createsuperuser
   ```

3. **Lancer le serveur de développement :**
   ```bash
   python manage.py runserver
   ```

4. **Accéder à l'API et à l'interface admin :**
   Ouvrez votre navigateur et allez à l'adresse suivante :
   ```
   http://localhost:8000
   ```

## Fonctionnalités

- Gestion des utilisateurs (parents, éducateurs, administrateurs)
- Gestion des inscriptions et des présences
- Suivi des activités des enfants
- Paiements en ligne et gestion des finances
- API REST sécurisées pour le front-end

