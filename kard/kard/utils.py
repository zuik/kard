from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from kard.config import DB_URL


def setup_database():
    engine = create_engine(DB_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
