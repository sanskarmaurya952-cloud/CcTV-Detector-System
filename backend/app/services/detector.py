import threading
import queue

from ultralytics import YOLO

from app.services.intrusion import IntrusionDetector
from app.services.alert import AlertService


class Detector:

    def __init__(self):
        self.model = YOLO("yolov8n.onnx")

        self.intrusion = IntrusionDetector()
        self.alert = AlertService()

        self.input_queue = queue.Queue(maxsize=1)
        self.output_frame = None

        self.running = False
        self.lock = threading.Lock()

    def start(self):

        if self.running:
            return self

        self.running = True

        threading.Thread(
            target=self.detect,
            daemon=True
        ).start()

        return self

    def update(self, frame):

        if self.input_queue.full():
            try:
                self.input_queue.get_nowait()
            except queue.Empty:
                pass

        self.input_queue.put(frame)

    def get_frame(self):

        with self.lock:
            if self.output_frame is None:
                return None

            return self.output_frame.copy()

    def detect(self):

        while self.running:

            try:
                frame = self.input_queue.get(timeout=1)
            except queue.Empty:
                continue

            results = self.model(
                frame,
                imgsz=224,
                conf=0.45,
                classes=[0],
                max_det=3,
                verbose=False
            )

            intrusion, output = self.intrusion.check(results, frame)

            if intrusion:
                # Abhi sirf console alert
                self.alert.trigger(
                    camera_id=1,
                    alert_type="INTRUSION",
                    frame=output
                )

            with self.lock:
                self.output_frame = output

    def stop(self):

        self.running = False