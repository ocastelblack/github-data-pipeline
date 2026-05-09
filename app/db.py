import os
import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

from models import Base

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


def wait_for_db():

    retries = 10

    while retries > 0:
        try:
            with engine.connect():
                print("Conexión exitosa a PostgreSQL")
                return

        except OperationalError:
            print("Esperando PostgreSQL...")
            retries -= 1
            time.sleep(5)

    raise Exception("No se pudo conectar a PostgreSQL")


def create_tables():
    Base.metadata.create_all(engine)
    print("Tablas creadas")