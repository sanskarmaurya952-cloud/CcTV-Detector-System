from pydantic import BaseModel
from datetime import datetime


class AlertResponse(BaseModel):
    id: int
    camera_id: int
    alert_type: str
    image_path: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True