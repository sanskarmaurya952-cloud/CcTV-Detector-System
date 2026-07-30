from app.services.camera_session import CameraSession


class CameraManager:

    def __init__(self):

        self.sessions = {}

    def add_camera(self, camera_id, rtsp_url):

        if camera_id in self.sessions:
            return self.sessions[camera_id]

        session = CameraSession(camera_id, rtsp_url)

        session.start()

        self.sessions[camera_id] = session

        return session

    def remove_camera(self, camera_id):

        if camera_id not in self.sessions:
            return

        self.sessions[camera_id].stop()

        del self.sessions[camera_id]

    def get_session(self, camera_id):

        return self.sessions.get(camera_id)

    def stop_all(self):

        for session in self.sessions.values():
            session.stop()

        self.sessions.clear()


camera_manager = CameraManager()