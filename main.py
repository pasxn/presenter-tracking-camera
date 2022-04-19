#!/usr/bin/env python3 

import cv2
import numpy as np
from imutils.video import FPS
import time
import sys
import os 
from detectord import MobileNetSSD
from trackerd import KCF_tracker

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    localDetector = MobileNetSSD.Detector()
    localTracker = KCF_tracker.Tracker()

    time.sleep(2.0)
    fps = FPS().start()
    
    print("[INFO] start")
    while(cap.isOpened()):
        ret, frame = cap.read()

        if localTracker.isPerson():
            localBounderies = localTracker.getCoordinates(frame)
            print("[INFO] Tracker: {}".format(localBounderies))
            
            frame = localTracker.getCurruntFrameWithBoundingBox()
        else:
            localTracker.inputPerson(localDetector.detect(frame), frame)

        cv2.imshow('trackerd test', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        fps.update()
    
    fps.stop()

    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cap.release()
    cv2.destroyAllWindows()