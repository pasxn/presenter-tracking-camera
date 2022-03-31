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

    def detect(self, frame):
        frame = cv2.flip(frame,1)
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.2:
                idx = int(detections[0, 0, i, 1])
                if str(CLASSES[idx]) == "person":
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		    (startX, startY, endX, endY) = box.astype("int")
		    label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
		    cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
		    y = startY - 15 if startY - 15 > 15 else startY + 15
		    cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
