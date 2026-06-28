import cv2

from beatvision.logger import logger
from beatvision.config import AppConfig


class CameraManager:

    def __init__(self):

        self.config = AppConfig()

        self.cap = cv2.VideoCapture(self.config.camera.index)

        if not self.cap.isOpened():
            raise RuntimeError("Não foi possível abrir a webcam.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.camera.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.camera.height)
        self.cap.set(cv2.CAP_PROP_FPS, self.config.camera.fps)

        logger.success("Webcam inicializada.")

    def read(self):

        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def release(self):

        self.cap.release()

        logger.info("Webcam liberada.")