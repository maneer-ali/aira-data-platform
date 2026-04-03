from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4, UUID

class Tenant(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    slug: str
    plan_tier: str
    created_at: datetime = Field(default_factory=datetime.utcnow)