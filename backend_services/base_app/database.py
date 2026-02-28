from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQL_DB_URL = "postgresql://postgres:aRZ8kQfs@localhost:5432/.........."

engine = create_engine(SQL_DB_URL)

session_maker = sessionmaker(autoflush=False, autocommit=False, bind=engine)

