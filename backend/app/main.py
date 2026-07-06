from fastapi import FastAPI

from app.db.database import engine, Base

# Import all models
from app.models.user import User
from app.models.camera import Camera
from app.models.alert import Alert
from app.api.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="CCTV_DETECTOR_SYSTEM")

app.include_router(auth_router)

from app.api import camera

app.include_router(camera.router)

from app.api import health

app.include_router(health.router)

from app.api import stream
app.include_router(stream.router)

from app.api import alerts
app.include_router(alerts.router)