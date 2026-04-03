from sqlmodel import create_engine, Session
from sqlalchemy import text
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

def get_db():
    with Session(engine) as session:
        yield session