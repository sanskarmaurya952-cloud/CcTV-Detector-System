import cv2

from app.services.camera_stream import CameraStream
from app.services.detector import Detector


def generate_frames(camera_url: str):

    camera = CameraStream(camera_url).start()
    detector = Detector().start()

    while True:

        # Latest camera frame
        frame = camera.read()

        if frame is None:
            continue

        frame = cv2.resize(frame, (416, 416))

        # Detector ko frame do
        detector.update(frame)

        # Latest processed frame lo
        output = detector.get_frame()

        # Starting me jab detection complete na hua ho
        if output is None:
            output = frame

        ret, buffer = cv2.imencode(
            ".jpg",
            output,
            [cv2.IMWRITE_JPEG_QUALITY, 60]
        )

        if not ret:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )