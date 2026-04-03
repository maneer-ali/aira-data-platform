from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime, timezone
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    power_user = "power_user"
    operator = "operator"
    viewer = "viewer"

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    tenant_id: UUID
    email: str
    password_hash: str
    display_name: str
    role: UserRole
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))