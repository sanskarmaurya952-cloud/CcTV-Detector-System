import cv2


class IntrusionDetector:

    def __init__(self):
        # Rectangle Zone (x1, y1, x2, y2)
        self.zone = (150, 100, 500, 400)

    def check(self, results, frame):

        x1, y1, x2, y2 = self.zone

        intrusion = False

        # Draw Zone
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        for box in results[0].boxes:

            cls = int(box.cls[0])

            # Person class only
            if cls != 0:
                continue

            bx1, by1, bx2, by2 = map(int, box.xyxy[0])

            cx = (bx1 + bx2) // 2
            cy = (by1 + by2) // 2

            # Draw center point
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

            # Check if center lies inside zone
            if x1 <= cx <= x2 and y1 <= cy <= y2:
                intrusion = True

                cv2.putText(
                    frame,
                    "INTRUSION",
                    (bx1, by1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

        return intrusion, frame