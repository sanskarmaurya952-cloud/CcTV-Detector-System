from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.camera import Camera
from app.models.user import User
from app.core.security import get_current_user
from app.services.camera_health import check_camera_status

router = APIRouter(prefix="/health", tags=["Camera Health"])


@router.get("/{camera_id}")
def check_health(
    camera_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    camera = db.query(Camera).filter(
        Camera.id == camera_id,
        Camera.owner_id == current_user.id
    ).first()

    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")

    online = check_camera_status(camera.rtsp_url)

    camera.status = "online" if online else "offline"

    db.commit()

    return {
        "camera_id": camera.id,
        "camera_name": camera.name,
        "status": camera.status
    }