from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import cv2
import time

from app.db.database import get_db
from app.models.camera import Camera
from app.services.camera_manager import camera_manager

router = APIRouter(prefix="/stream", tags=["Live Stream"])


def generate_stream(session):
    """
    Stream frames from an existing CameraSession.
    """

    while True:

        frame = session.get_frame()

        if frame is None:
            time.sleep(0.01)
            continue

        ret, buffer = cv2.imencode(
            ".jpg",
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 70]
        )

        if not ret:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )


@router.get("/{camera_id}")
def stream_camera(
    camera_id: int,
    db: Session = Depends(get_db),
):
    # Camera exists?
    camera = db.query(Camera).filter(Camera.id == camera_id).first()

    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")

    # Existing session use karo
    session = camera_manager.get_session(camera.id)

    # Agar session nahi hai to create karo
    if session is None:
        session = camera_manager.add_camera(
            camera.id,
            camera.rtsp_url
        )

    return StreamingResponse(
        generate_stream(session),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )