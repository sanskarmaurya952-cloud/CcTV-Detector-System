import threading
import time
import logging
from typing import Optional

import cv2
import numpy as np

logger = logging.getLogger(__name__)


class CameraSession:
    """
    Handles a single RTSP camera session.

    Responsibilities:
    - Connect RTSP
    - Read frames continuously
    - Auto reconnect
    - FPS calculation
    - Latest frame cache
    """

    def __init__(self, camera_id: int, rtsp_url: str):

        self.camera_id = camera_id
        self.rtsp_url = rtsp_url

        self.capture = None

        self.running = False

        self.thread = None

        self.latest_frame: Optional[np.ndarray] = None

        self.lock = threading.Lock()

        self.last_frame_time = 0

        self.fps = 0

        self.frame_count = 0

        self.reconnect_count = 0

        self.connected = False

    # ------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._capture_loop,
            daemon=True
        )

        self.thread.start()

        logger.info(f"Camera {self.camera_id} started")

    # ------------------------

    def stop(self):

        self.running = False

        if self.thread:

            self.thread.join(timeout=2)

        if self.capture:

            self.capture.release()

        logger.info(f"Camera {self.camera_id} stopped")

    # ------------------------

    def _connect(self):

        logger.info(f"Connecting Camera {self.camera_id}")

        self.capture = cv2.VideoCapture(self.rtsp_url)

        self.connected = self.capture.isOpened()

        return self.connected

    # ------------------------

    def _capture_loop(self):

        while self.running:

            if not self.capture or not self.capture.isOpened():

                success = self._connect()

                if not success:

                    logger.warning(
                        f"Camera {self.camera_id} reconnecting..."
                    )

                    self.reconnect_count += 1

                    time.sleep(5)

                    continue

            ret, frame = self.capture.read()

            if not ret:

                logger.warning(
                    f"Camera {self.camera_id} frame lost."
                )

                self.capture.release()

                time.sleep(2)

                continue

            with self.lock:

                self.latest_frame = frame

            self.frame_count += 1

            now = time.time()

            if self.last_frame_time == 0:

                self.last_frame_time = now

            elapsed = now - self.last_frame_time

            if elapsed >= 1:

                self.fps = self.frame_count

                self.frame_count = 0

                self.last_frame_time = now

    # ------------------------

    def get_frame(self):

        with self.lock:

            if self.latest_frame is None:
                return None

            return self.latest_frame.copy()

    # ------------------------

    def get_metrics(self):

        return {

            "camera_id": self.camera_id,

            "connected": self.connected,

            "fps": self.fps,

            "reconnect_count": self.reconnect_count

        }