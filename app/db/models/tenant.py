from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime, timezone

class Tenant(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str
    slug: str
    plan_tier: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))