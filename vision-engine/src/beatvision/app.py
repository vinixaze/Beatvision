import cv2

from beatvision.camera import CameraManager
from beatvision.renderer import Renderer
from beatvision.fps import FPSCounter
from beatvision.logger import logger
from beatvision.hand_tracker import HandTracker


class App:

    def __init__(self):

        logger.info("Inicializando BeatVision...")

        self.camera = CameraManager()

        self.renderer = Renderer()

        self.fps = FPSCounter()
        
        self.hand_tracker = HandTracker()

    def run(self):

        while True:

            frame = self.camera.read()


            if frame is None:
                break

            result = self.hand_tracker.process(frame)

            frame = self.hand_tracker.draw(frame, result)

            fps = self.fps.update()

            cv2.putText(
                frame,
                f"FPS: {fps}",
                (15, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            self.renderer.draw(frame)

            if self.renderer.should_close():
                break

        self.camera.release()

        self.renderer.destroy()

        logger.success("BeatVision finalizado.")