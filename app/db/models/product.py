from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from datetime import datetime
from decimal import Decimal

class Product(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    tenant_id: UUID
    external_id: str
    title: str
    description: str
    image_url: str
    price: Decimal
    currency: str
    category: str
    tags: dict
    stock_qty: int
    active: bool
    metadata: dict
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)