from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.event_schema import EventBatch
from app.db.session import get_db
import time

router = APIRouter()

@router.post("/api/v1/events/batch")
def ingest_events(payload: EventBatch, db: Session = Depends(get_db)):
    start = time.time()

    data = [event.dict() for event in payload.events]

    db.bulk_insert_mappings("event", data)
    db.commit()

    processing_ms = (time.time() - start) * 1000

    return {
        "accepted": len(data),
        "processing_ms": processing_ms
    }