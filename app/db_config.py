import databases

DB_USER = "starter_kit"
DB_PASSWORD = "qwerty"
DB_HOST = "localhost"
DB_NAME = "postgres"

# Use separate DB for tests

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)
