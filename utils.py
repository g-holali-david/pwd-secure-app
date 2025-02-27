import bcrypt
import redis
from config import Config
import os

def hash_password(password):
    """Hashage du mot de passe avec sel + poivre"""
    password = password.encode('utf-8') + Config.PEPPER  
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed.decode('utf-8')

def verify_password(stored_hash, password):
    """Vérification du mot de passe haché"""
    password = password.encode('utf-8') + Config.PEPPER
    return bcrypt.checkpw(password, stored_hash.encode('utf-8'))


def get_redis_connection():
    """Connexion à Redis Cloud avec gestion des erreurs"""
    try:
        redis_client = redis.StrictRedis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT", 6379)),  # 6379 par défaut
            username=os.getenv("REDIS_USERNAME"),  # Ajout du username
            password=os.getenv("REDIS_PASSWORD"),
            decode_responses=True
        )
        redis_client.ping()  # Vérifier la connexion
        print("✅ Connexion réussie à Redis Cloud !")
        return redis_client
    except redis.AuthenticationError:
        print("❌ Erreur d'authentification : Vérifie REDIS_USERNAME et REDIS_PASSWORD")
    except redis.ConnectionError:
        print("❌ Impossible de se connecter à Redis Cloud : Vérifie REDIS_HOST et REDIS_PORT")
    except Exception as e:
        print(f"❌ Erreur inconnue : {e}")
    return None

redis_client = get_redis_connection()

