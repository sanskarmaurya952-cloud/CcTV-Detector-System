import os
import time
import cv2


class AlertService:

    def __init__(self):
        self.last_alert_time = {}
        self.cooldown = 5  # seconds

        os.makedirs("snapshots", exist_ok=True)

    def trigger(
        self,
        camera_id: int,
        alert_type: str,
        frame
    ):

        current = time.time()

        # Camera-wise cooldown
        if camera_id in self.last_alert_time:
            if current - self.last_alert_time[camera_id] < self.cooldown:
                return False

        self.last_alert_time[camera_id] = current

        # Save snapshot
        filename = f"{camera_id}_{int(current)}.jpg"
        path = os.path.join("snapshots", filename)

        cv2.imwrite(path, frame)

        print(f"🚨 {alert_type} | Camera {camera_id}")
        print(f"📸 Snapshot Saved: {path}")

        return True