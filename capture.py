import mss
import cv2
import time
import numpy
# import socket
I = 0
# nc = socket.socket()
# nc.connect(('127.0.0.1', 45000))
try:
    time.sleep(1)
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {'top': 40, 'left': 0, 'width': 1920, 'height': 1080}
        while 1:
                # Get raw pixels from the screen, save it to a Numpy array
                img = numpy.array(sct.grab(monitor))
                img = cv2.resize(img, (1024, 768))
                # Display the picture
                _, jpeg = cv2.imencode('.jpg', img)
                # nc.send(jpeg.tobytes())
                # print(len(jpeg.tobytes()))
                open('a.jpg', 'wb').write(jpeg.tobytes())
                time.sleep(0.1)
                # Display the picture in grayscale
                # cv2.imshow('OpenCV/Numpy grayscale',
                # cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
                cv2.waitKey(1)
except:
    pass

