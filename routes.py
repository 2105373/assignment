from fastapi import APIRouter, HTTPException # type: ignore
from app.models import CalendarEvent # type: ignore
from app.database import calendar_collection # type: ignore
from app.schemas import CreateEventSchema, UpdateEventSchema # type: ignore
from bson import ObjectId # type: ignore

router = APIRouter()

@router.post("/events", response_description="Create a new event")
async def create_event(event: CreateEventSchema):
    event = CalendarEvent(**event.dict())
    result = await calendar_collection.insert_one(event.dict(by_alias=True))
    return {"id": str(result.inserted_id)}

@router.get("/events")
async def get_events():
    events = await calendar_collection.find().to_list(100)
    return events

@router.get("/events/{id}")
async def get_event(id: str):
    event = await calendar_collection.find_one({"_id": ObjectId(id)})
    if event:
        return event
    raise HTTPException(status_code=404, detail="Event not found")

@router.put("/events/{id}")
async def update_event(id: str, event: UpdateEventSchema):
    updated_event = await calendar_collection.update_one({"_id": ObjectId(id)}, {"$set": event.dict(exclude_unset=True)})
    if updated_event.modified_count:
        return {"msg": "Event updated"}
    raise HTTPException(status_code=404, detail="Event not found")

@router.delete("/events/{id}")
async def delete_event(id: str):
    delete_result = await calendar_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count:
        return {"msg": "Event deleted"}
    raise HTTPException(status_code=404, detail="Event not found")
