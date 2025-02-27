import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")
    REDIS_HOST = "127.0.0.1"  # Redis sur localhost
    REDIS_PORT = 6379
    REDIS_PASSWORD = None  # Pas de mot de passe pour Redis
    PEPPER = b"PoivreSecret123"  # Poivre pour renforcer la sécurité
