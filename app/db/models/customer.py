from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from datetime import datetime

class Customer(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    tenant_id: UUID
    external_id: str
    email: str
    attributes: dict
    first_seen: datetime
    last_seen: datetime