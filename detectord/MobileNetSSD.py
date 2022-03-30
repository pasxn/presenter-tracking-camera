from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np
import time
import cv2

class detector:
    def __init__(self):
        self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	        "sofa", "train", "tvmonitor"]
        self.COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
        self.model = cv2.dnn.readNetFromCaffe('model/MobileNetSSD_deploy.prototxt.txt', 'model/MobileNetSSD_deploy.caffemodel')