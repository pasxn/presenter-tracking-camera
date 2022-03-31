import numpy as np
import cv2

class Detector:
    def __init__(self):
        self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	                "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	                "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	                "sofa", "train", "tvmonitor"]
        self.COLORS = np.random.uniform(0, 255, size=(len(self.CLASSES), 3))
        self.model = cv2.dnn.readNetFromCaffe('model/MobileNetSSD_deploy.prototxt.txt', 
                                                    'model/MobileNetSSD_deploy.caffemodel')

        # intermediate and output parameters
        self.bounderies = None;
        self.frame = None
        self.confidence = None
        self.idx = None

    def detect(self, frame):
        self.frame = cv2.flip(frame,1)
        (h, w) = self.frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(self.frame, (300, 300)), 
                                                0.007843, (300, 300), 127.5)

        self.model.setInput(blob)
        detections = self.model.forward()

        for i in np.arange(0, detections.shape[2]):
            self.confidence = detections[0, 0, i, 2]
            if self.confidence > 0.2:
                self.idx = int(detections[0, 0, i, 1])
                if str(self.CLASSES[self.idx]) == "person":
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    self.bounderies = (startX, startY, endX, endY)

                    return self.bounderies

    def getCurruntFrameWithBoundingBox(self):
        label = "{}: {:.2f}%".format(self.CLASSES[self.idx], self.confidence * 100)
        cv2.rectangle(self.frame, (self.bounderies[0], self.bounderies[1]), 
                                        (self.bounderies[2], self.bounderies[3]), self.COLORS[self.idx], 2)
        y = self.bounderies[1] - 15 if self.bounderies[1] - 15 > 15 else self.bounderies[1] + 15
        cv2.putText(self.frame, label, (self.bounderies[0], y), cv2.FONT_HERSHEY_SIMPLEX, 
                                                                0.5, self.COLORS[self.idx], 2)

        return self.frame