import cv2
import threading
import queue


class CameraStream:

    def __init__(self, url):
        self.url = url
        self.cap = cv2.VideoCapture(url , cv2.CAP_FFMPEG)

        # Camera buffer minimum rakho
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.frame_queue = queue.Queue(maxsize=1)
        self.running = False

    def start(self):

        if self.running:
            return self

        if not self.cap.isOpened():
            raise Exception("Unable to open camera stream.")

        self.running = True

        threading.Thread(
            target=self.update,
            daemon=True
        ).start()

        return self

    def update(self):

        while self.running:

            success, frame = self.cap.read()

            if not success:
                continue

            # Queue full hai to purana frame hata do
            if self.frame_queue.full():
                try:
                    self.frame_queue.get_nowait()
                except queue.Empty:
                    pass

            self.frame_queue.put(frame)

    def read(self):

        try:
            return self.frame_queue.get_nowait()
        except queue.Empty:
            return None

    def stop(self):

        self.running = False

        if self.cap.isOpened():
            self.cap.release()