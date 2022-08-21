import cv2
import numpy as np

class Framer:
    def __init__(self):
        self.width = [i for i in range(20, 641, 20)]
        self.height = [i for i in range(15, 481, 15)]
        self.normalizationFactor = 10 
        self.prevLocalCoordinates = None
        self.calculatedCoordinates = None

    def calculateCoordinates(self, localCoordinates):
        if localCoordinates != None:
            self.prevLocalCoordinates = localCoordinates
            x1, y1, x2, y2 = localCoordinates[0], localCoordinates[1], localCoordinates[2], localCoordinates[3]
        else:
            x1, y1, x2, y2 = self.prevLocalCoordinates[0], self.prevLocalCoordinates[1], self.prevLocalCoordinates[2], self.prevLocalCoordinates[3]
        
        startx = ( x1 - ((x2 - x1)/self.normalizationFactor) )
        starty = ( y1 - ((y2 - y1)/self.normalizationFactor) )

        if startx < 0: startx = 0
        if starty < 0: starty = 0
        if x2 > 640: x2 = 640
        if y2 > 480: x2 = 480

        for i in range(len(self.width)):
            if self.width[i] > ((x2 - x1)):
                index =  i+1
                break
        try:
            self.calculatedCoordinates = (int(startx), int(starty), int(startx + self.width[index]), int(starty + self.height[index]))
        except:
            pass
        
        return self.calculatedCoordinates

    def frame(self, localCoordinates, frame):
        zoomedCoordinates = self.calculateCoordinates(localCoordinates)
        croppedFrame = frame[zoomedCoordinates[1]:zoomedCoordinates[3], zoomedCoordinates[0]:zoomedCoordinates[2]]
        croppedFrame = cv2.resize(croppedFrame,(640,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)

        return croppedFrame