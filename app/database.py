from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#loading environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./shortener.db")

engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)


SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

# Parent Class for DB ops -> Tracks subclasses and
# maps sub class -> tables
# All tables are stored in Base.metadata
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()