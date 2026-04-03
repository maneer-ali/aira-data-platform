from sqlmodel import create_engine, Session
from sqlalchemy import text
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

def get_db(tenant_id: str = None):
    with Session(engine) as session:
        if tenant_id:
            session.exec(
                text(f"SET LOCAL app.current_tenant = '{tenant_id}'")
            )
        yield session