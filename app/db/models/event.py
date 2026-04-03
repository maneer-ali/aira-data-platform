from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional
from enum import Enum

class EventType(str, Enum):
    page_view = "page_view"
    product_view = "product_view"
    add_to_cart = "add_to_cart"
    purchase = "purchase"
    click = "click"
    dismiss = "dismiss"

class Event(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    tenant_id: UUID
    customer_id: UUID
    event_type: EventType
    product_id: Optional[UUID] = None
    properties: dict
    timestamp: datetime