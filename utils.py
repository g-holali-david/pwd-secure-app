import bcrypt
import redis
from config import Config

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
    """Connexion à Redis Cloud"""
    try:
        redis_client = redis.StrictRedis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            username=Config.REDIS_USERNAME,  # Ajout de l'utilisateur
            password=Config.REDIS_PASSWORD,  # Ajout du mot de passe
            decode_responses=True
        )
        redis_client.ping()  # Vérifier la connexion
        print("✅ Connexion réussie à Redis Cloud !")
        return redis_client
    except redis.ConnectionError:
        print("❌ Impossible de se connecter à Redis Cloud")
        return None

redis_client = get_redis_connection()
