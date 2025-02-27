# Projet d'Authentification avec Flask et Redis

Ce projet est une application Flask utilisant Redis comme base de données pour gérer l'authentification des utilisateurs.

## Fonctionnalités
- Inscription et connexion sécurisées avec hachage de mot de passe (bcrypt + poivre)
- Stockage des utilisateurs dans Redis
- Tableau de bord utilisateur après connexion
- Gestion de session avec Flask

## Prérequis
- Python 3.x
- Redis (local ou hébergé sur le cloud)
- Un environnement virtuel Python (optionnel mais recommandé)

## Installation

### 1. Cloner le dépôt
```sh
git clone <URL_DU_REPO>
cd projet-auth
```

### 2. Créer un environnement virtuel et installer les dépendances
```sh
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurer Redis
Vous avez deux options pour configurer Redis :

#### Option 1 : Utiliser Redis Cloud (Recommandé)
Créez une base de données Redis sur un service cloud comme [Redis Cloud](https://app.redislabs.com/). Notez l'hôte, le port, l'utilisateur et le mot de passe fournis.

Dans `config.py`, renseignez les informations de votre instance Redis Cloud :
```python
class Config:
    SECRET_KEY = "super_secret_key"
    REDIS_HOST = "redis-xxx.eu-west-3-1.ec2.redns.redis-cloud.com"
    REDIS_PORT = 17750
    REDIS_USERNAME = "default"
    REDIS_PASSWORD = "VotreMotDePasse"
    PEPPER = b"PoivreSecret123"
```

#### Option 2 : Installer Redis en local
- **Linux/macOS :**
```sh
sudo apt update && sudo apt install redis-server
```
- **Windows :** [Téléchargez Redis pour Windows](https://github.com/microsoftarchive/redis/releases)

Dans `config.py`, utilisez la configuration locale :
```python
class Config:
    SECRET_KEY = "super_secret_key"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_PASSWORD = None  # Pas de mot de passe si Redis est en local
    PEPPER = b"PoivreSecret123"
```

### 4. Lancer l'application
```sh
python app.py
```
L'application sera accessible à l'adresse : `http://127.0.0.1:5000`

## Test de la connexion Redis
Vérifiez que Redis fonctionne correctement :
```python
import redis
r = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, username=Config.REDIS_USERNAME, password=Config.REDIS_PASSWORD, decode_responses=True)
print(r.ping())  # Doit retourner True
```

## Déploiement
Pour un déploiement en production, utilisez un serveur WSGI comme Gunicorn et configurez une base de données Redis Cloud.

## Auteur
Dav's Lab: GAVI Holali David

## Licence
MIT

