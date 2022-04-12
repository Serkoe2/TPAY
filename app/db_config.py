import databases
import os


DB_URL = os.environ.get('DATABASE_URL')
if not DB_URL:
    DB_USER = "starter_kit"
    DB_PASSWORD = "qwerty"
    DB_HOST = "localhost"
    DB_NAME = "postgres"
    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
else:
    DB_URL.replace('postgres://', 'postgresql://')

# Use separate DB for tests
SQLALCHEMY_DATABASE_URL = DB_URL

database = databases.Database(SQLALCHEMY_DATABASE_URL)
