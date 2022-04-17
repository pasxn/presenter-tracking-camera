import cv2
import sys

class Tracker:
    def __init__ (self):
        self.tracker = cv2.TrackerKCF_create()
        self.isPersonInFrame = False
        self.frame = None
        self.inputBbox = None
        self.bbox = None

    def inputPerson(self, inputBbox):
        self.isPersonInFrame = True
        self.inputBbox = inputBbox

    def getCoordinates(self, frame):
        self.frame = cv2.flip(frame,1)
        self.frame = frame
        ok = self.tracker.init(self.frame, self.inputBbox)
        ##########################################
        ok, self.bbox = self.tracker.update(self.frame)

        if not ok:
            self.isPersonInFrame = False
        else:
            print("[INFO] tracking successful")
            return self.bbox
            
    def getCurruntFrameWithBoundingBox(self):
        if self.isPersonInFrame:
            p1 = (int(self.bbox[0]), int(self.bbox[1]))
            p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
            cv2.rectangle(self.frame, p1, p2, (255,0,0), 2, 1) 

            return self.frame       
                
    def isPerson(self):
        return self.isPersonInFrame