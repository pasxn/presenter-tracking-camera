#!/usr/bin/env python3 

import cv2
import numpy as np
from imutils.video import FPS
import time
from detectord import MobileNetSSD
from trackerd import KCFtracker
from framed import Camera
from gimbald import Controller

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    localDetector = MobileNetSSD.Detector()
    localTracker = KCFtracker.Tracker()
    localFramer = Camera.Framer()
    localController = Controller.GimbalController()

    time.sleep(2.0)
    fps = FPS().start()
    
    print("[INFO] start")
    while(cap.isOpened()):
        ret, frame = cap.read()
        outputFrame = cv2.flip(frame,1)

        localBounderies = localDetector.detect(frame)
        localController.sendCommands(localBounderies)
        outputFrame = localFramer.frame(localBounderies, frame)
            

        cv2.imshow('presenter-tracking-camera (output)', outputFrame)
        cv2.imshow('presenter-tracking-camera (source)', cv2.flip(frame, 1))

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        fps.update()
    
    fps.stop()

    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cap.release()
    cv2.destroyAllWindows()