from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.camera import Camera
from app.models.user import User
from app.schemas.camera import CameraCreate, CameraResponse
from app.core.security import get_current_user

router = APIRouter(prefix="/camera", tags=["Camera"])


@router.post("/add", response_model=CameraResponse)
def add_camera(
    camera: CameraCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_camera = Camera(
        name=camera.name,
        location=camera.location,
        rtsp_url=camera.rtsp_url,
        owner_id=current_user.id,
        status="offline"
    )

    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)

    return new_camera

from typing import List

@router.get("/my-cameras", response_model=List[CameraResponse])
def get_my_cameras(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cameras = db.query(Camera).filter(
        Camera.owner_id == current_user.id
    ).all()

    return cameras