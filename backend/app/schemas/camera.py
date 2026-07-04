from pydantic import BaseModel

class CameraCreate(BaseModel):
    name: str
    location: str
    rtsp_url: str

class CameraResponse(BaseModel):
    id: int
    name: str
    location: str
    rtsp_url: str
    status: str

    class Config:
        from_attributes = True