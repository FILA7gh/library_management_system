import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
DEBUG=os.getenv('DEBUG', default=False)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='localhost').split(',')

POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT=os.getenv('POSTGRES_PORT', default=5432)
POSTGRES_HOST=os.getenv('POSTGRES_HOST', default='localhost')
