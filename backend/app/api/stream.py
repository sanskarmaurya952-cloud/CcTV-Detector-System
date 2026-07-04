from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.camera import Camera
from app.models.user import User
from app.core.security import get_current_user
from app.services.video_stream import generate_frames

router = APIRouter(prefix="/stream", tags=["Live Stream"])


@router.get("/{camera_id}")
def stream_camera(
    camera_id: int,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    camera = db.query(Camera).filter(
    Camera.id == camera_id
).first()

    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")

    return StreamingResponse(
        generate_frames(camera.rtsp_url),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )