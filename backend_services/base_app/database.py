import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend_services.services.tables.base_table import Base
from backend_services.utils.users.load_users import fill_users_tables

SQL_DB_URL = "postgresql://postgres@localhost:5432/api_db"

engine = create_engine(
    SQL_DB_URL,
    echo=True,  # будет видеть все SQL запросы в консоли (полезно для отладки)
    pool_size=5,  # размер пула соединений
    max_overflow=10  # максимум доп. соединений)
)

session_maker = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def create_database_if_not_exists():
    DB_USER = "postgres"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "api_db"

    conn = psycopg2.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database="postgres"
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f'CREATE DATABASE "{DB_NAME}"')
    else:
        print(f"База данных {DB_NAME} уже существует")

    cursor.close()
    conn.close()

def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    create_database_if_not_exists()

    from backend_services.services.tables.user_table import (
        User, PersonalInfo, Contact, Employment,
        Education, Settings, Statistics
    )

    create_tables()

    with session_maker() as session:
        fill_users_tables(session)
