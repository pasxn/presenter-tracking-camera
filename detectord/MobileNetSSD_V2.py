import cv2

class Detector:
    def __init__(self):
        self.CLASSES = []
        with open('modeld/coco.names','rt') as f:
            self.CLASSES = f.read().rstrip('n').split('n')

        self.model = cv2.dnn_DetectionModel('modeld/frozen_inference_graph.pb',
                            'modeld/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
        self.model.setInputSize(320,320)
        self.model.setInputScale(1.0/ 127.5)
        self.model.setInputMean((127.5, 127.5, 127.5))
        self.model.setInputSwapRB(True)

        # intermediate and output parameters
        self.bounderies = None
        self.frame = None

    def detect(self, frame):
        self.frame = frame
        classIds, confs, bbox = self.model.detect(self.frame,confThreshold = 0.45, nmsThreshold = 0.2)

        if len(classIds) != 0:
            for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                if classId == 1:
                    (startX, startY, endX, endY) = box.astype("int")
                    self.bounderies = (startX, startY, endX, endY)

                    return self.bounderies