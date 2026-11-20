import psycopg
from decouple import config


def get_db_connection():
    connection = psycopg.connect(
        dbname=config("DB_NAME"),
        user=config("DB_USER"),
        password=config("DB_PASSWORD"),
        host=config("DB_HOST"),
        port=config("DB_PORT", default=5432, cast=int),
        connect_timeout=5,
    )

    return connection