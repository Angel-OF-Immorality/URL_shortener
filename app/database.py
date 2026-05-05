# DB Layer - Connection and Engine
# How to talk to DB and hand out sessions for DB functions

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# loading environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./shortener.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {},
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Generator function:
    call -> next(get_db)

    Returns a session and closes it when used.
    Even when an error occurs

    Return -> Gives a session but doesn't ensures clean up
    Yield + Try-Finally block -> Gives conn and ensures the connection is closed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
