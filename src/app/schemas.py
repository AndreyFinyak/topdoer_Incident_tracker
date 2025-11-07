from pydantic import BaseModel
from app.infrastructure.db.models import IncidentStatus, IncidentSource


class IncidentCreate(BaseModel):
    body: str
    source: IncidentSource | None = IncidentSource.other


class IncidentRead(BaseModel):
    id: int
    body: str
    status: IncidentStatus
    source: IncidentSource

    class Config:
        orm_mode = True


class IncidentUpdate(BaseModel):
    id: int
    body: str | None = None
    status: IncidentStatus | None = None
    source: IncidentSource | None = None


class IncidentStatusUpdate(BaseModel):
    id: int
    status: IncidentStatus
