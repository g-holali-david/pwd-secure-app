# Projet d'Authentification avec Flask et Redis

## Description
Ce projet est une application d'authentification utilisant **Flask** et **Redis** comme base de données pour stocker les utilisateurs. Il permet aux utilisateurs de s'inscrire, se connecter et accéder à un tableau de bord.

## Technologies utilisées
- **Flask** (Framework Web Python)
- **Redis** (Stockage des utilisateurs sous forme de hachage)
- **Bootstrap 5** (Interface utilisateur améliorée)
- **bcrypt** (Sécurisation des mots de passe avec hashage)

---

## Installation

### 1️⃣ Prérequis
Assurez-vous d'avoir **Python 3.x** installé ainsi que **Redis** en cours d'exécution.

### 2️⃣ Cloner le projet
```sh
$ git clone https://github.com/votre-repo/projet-auth.git
$ cd projet-auth
```

### 3️⃣ Créer un environnement virtuel et installer les dépendances
```sh
$ python -m venv venv
$ source venv/bin/activate  # Sur Mac/Linux
$ venv\Scripts\activate    # Sur Windows
$ pip install -r requirements.txt
```

### 4️⃣ Lancer Redis (si ce n'est pas déjà fait)
Sur Windows (PowerShell) :
```sh
$ Start-Service Redis
```
Sur Linux/macOS :
```sh
$ redis-server
```

### 5️⃣ Configurer l'application
Modifiez le fichier **config.py** si nécessaire, notamment pour l'adresse Redis :
```python
class Config:
    SECRET_KEY = "super_secret_key"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_PASSWORD = None  # Pas de mot de passe
```

### 6️⃣ Lancer l'application Flask
```sh
$ python app.py
```
L'application sera accessible à : [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Fonctionnalités
✅ **Inscription** avec stockage sécurisé des mots de passe
✅ **Connexion** avec vérification des identifiants
✅ **Tableau de bord** affichant les informations de l'utilisateur
✅ **Déconnexion sécurisée**
✅ **Messages Flash** pour informer l'utilisateur
✅ **Interface responsive** grâce à Bootstrap

---

## Améliorations possibles
🚀 Ajouter la gestion des sessions avec expiration
🔐 Implémenter une authentification à deux facteurs (2FA)
📧 Ajouter la récupération de mot de passe via e-mail

---

## Auteur
👤 **GAVI Holali David**
