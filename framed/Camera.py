import cv2
import numpy as np

class Framer:
    def __init__(self):
        self.width = [i for i in range(20, 641, 20)] 
        self.height = [i for i in range(15, 481, 15)]
        self.normalizationFactor = 6 

    def calculateCoordinates(self, localCoordinates):
        x1, y1, x2, y2 = localCoordinates[0], localCoordinates[1], localCoordinates[2], localCoordinates[3]
        startx = ( x1 - ((x2 - x1)/self.normalizationFactor) )
        starty = ( y1 - ((y2 - y1)/self.normalizationFactor) )

        for i in range(self.width):
            if self.width[i] > ((x2 - x1) + 8):
                index =  i

        calculatedCoordinates = (startx, starty, startx + self.width[index], starty + self.height[index])

        return calculatedCoordinates

    