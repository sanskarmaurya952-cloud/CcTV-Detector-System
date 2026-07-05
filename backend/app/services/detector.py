import threading
import queue
from ultralytics import YOLO


class Detector:

    def __init__(self):
        self.model = YOLO("yolov8n.onnx")

        # Latest frame only
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

        # Purana frame hata do
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
                classes=[0],      # Sirf person
                max_det=3,
                verbose=False
            )

            output = results[0].plot()

            with self.lock:
                self.output_frame = output

    def stop(self):
        self.running = False