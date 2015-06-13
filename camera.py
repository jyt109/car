import cv2

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('car_traffic.mp4')

    def __del__(self):
        self.video.release()

    def get_numpy_frame(self):
        success, image = self.video.read()
        return success, str(image.tolist())
