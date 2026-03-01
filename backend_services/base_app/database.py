from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from backend_services.tables.base_table import Base

SQL_DB_URL = "postgresql://postgres:Changeme123@localhost:5432/api_db"

engine = create_engine(
    SQL_DB_URL,
    echo=True,  # будет видеть все SQL запросы в консоли (полезно для отладки)
    pool_size=5,  # размер пула соединений
    max_overflow=10  # максимум доп. соединений)
)

session_maker = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":

    from backend_services.tables.user_table import (
        User, PersonalInfo, Contact, Employment,
        Education, Settings, Statistics
    )

    create_tables()
