from pydantic import BaseModel # type: ignore
from datetime import datetime
from typing import Optional

class CreateEventSchema(BaseModel):
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: datetime

class UpdateEventSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
