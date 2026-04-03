from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EventItem(BaseModel):
    customer_id: str
    event_type: str
    product_id: Optional[str]
    properties: dict
    timestamp: datetime

class EventBatch(BaseModel):
    events: List[EventItem]