import cv2


class Renderer:

    def __init__(self, title="BeatVision"):

        self.title = title

    def draw(self, frame):

        cv2.imshow(self.title, frame)

    def should_close(self):

        return cv2.waitKey(1) & 0xFF == ord("q")

    def destroy(self):

        cv2.destroyAllWindows()