from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional

class APIKey(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID
    key_hash: str
    name: str
    scopes: dict
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None