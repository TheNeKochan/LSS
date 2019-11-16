from ctypes import *
import numpy as np
import json
import mss
import cv2


class VideoCamera(object):
    def __init__(self):
        self.cfg = json.load(open('config_client.json'))
        self.monitor = {'top': 0, 'left': 0, 'width': windll.user32.GetSystemMetrics(0), 'height': windll.user32.GetSystemMetrics(1)}
        self.img = None
        self.old_img = None
        self.jpeg = None
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        pass  # self.video.release()

    def get_frame(self):
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        try:
            with mss.mss() as sct:
                self.img = np.array(sct.grab(self.monitor))
                self.img = cv2.resize(self.img, (1920, 1080))
                self.jpeg = cv2.imencode('.jpg', self.img)[1].tobytes()
                self.old_img = self.jpeg
                return self.old_img
        except:
            return self.old_img
