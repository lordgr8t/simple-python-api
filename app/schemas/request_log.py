import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RequestLogCreate(BaseModel):
    ip: str
    endpoint: str
    method: str


class RequestLogOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    ip: str
    endpoint: str
    method: str
    created_at: datetime