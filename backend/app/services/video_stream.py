import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def generate_frames(camera_url: str):

    cap = cv2.VideoCapture(camera_url)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cap.isOpened():
        raise Exception("Unable to open camera stream.")

    frame_count = 0
    output_frame = None

    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.resize(frame, (640, 480))
        frame_count += 1

        if frame_count % 3 == 0:
            results = model(
                frame,
                imgsz=320,
                conf=0.5,
                verbose=False
            )
            output_frame = results[0].plot()

        if output_frame is None:
            output_frame = frame

        ret, buffer = cv2.imencode(
            ".jpg",
            output_frame,
            [cv2.IMWRITE_JPEG_QUALITY, 70]
        )

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )

    cap.release()