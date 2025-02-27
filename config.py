import os

from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_USERNAME = os.getenv("REDIS_USERNAME", None)
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
    PEPPER = os.getenv("PEPPER", "PoivreSecret123").encode('utf-8')
