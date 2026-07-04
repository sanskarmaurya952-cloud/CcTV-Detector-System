from fastapi import FastAPI

from app.db.database import engine, Base

# Import all models
from app.models.user import User
from app.models.camera import Camera

from app.api.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="CCTV_DETECTOR_SYSTEM")

app.include_router(auth_router)

from app.api import camera

app.include_router(camera.router)

