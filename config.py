import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # PostgreSQL Configuration
    DB_TYPE = os.getenv('DB_TYPE', 'postgresql')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
    POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', 'rims')
    POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', 5432))
    POSTGRES_SCHEMA = os.getenv('POSTGRES_SCHEMA', 'qasesequences')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', True)
