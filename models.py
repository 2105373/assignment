from pydantic import BaseModel, Field # type: ignore
from datetime import datetime
from typing import Optional

class CalendarEvent(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime]
