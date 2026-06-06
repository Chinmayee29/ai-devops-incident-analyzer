from pydantic import BaseModel
from datetime import datetime


class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: str


class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

        
from pydantic import BaseModel

class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: str

class IncidentUpdate(BaseModel):
    status: str