#!/usr/bin/env python3 

import cv2
import numpy as np

def cannyEdgeDetector(frame):
    grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    bluredFrame = cv2.GaussianBlur(grayScaleFrame, (5, 5), 0)
    cannyEdges = cv2.Canny(bluredFrame, 50, 150)

    return cannyEdges

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow('Lazy Lanes', cannyEdgeDetector(frame))
        print(np.array(frame).shape)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    '''
    
    int main() {

        Stream cap = new Stream();

        Trackerd tracker = new Trackerd();
        Detectord detector = new Detectord();

        Controllerd controller = ne Controller();
        framed frame = new Framed();    

        while(cap.isOpend()) {
            if(tracker.isPerson()) {
                controller.gimbal(tracker.getCoordinates());
                framed.broadcast(tracker.getCoordinates());
            } else {
                tracker.inputPerson(detector.detect());
            } 
        }
    }

    '''