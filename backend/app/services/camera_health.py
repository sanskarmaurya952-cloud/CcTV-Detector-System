import cv2

def check_camera_status(rtsp_url: str):
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        return False

    ret, frame = cap.read()
    cap.release()

    return ret