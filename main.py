#!/usr/bin/env python3 

import cv2
import numpy as np
from imutils.video import FPS
import time
from detectord import MobileNetSSD
from trackerd import KalmanFilter
from framed import Camera
from gimbald import Controller

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    localDetector = MobileNetSSD.Detector()
    localTracker = KalmanFilter.Kalmanfilter(0.1, 1, 1, 1, 0.1,0.1)
    localFramer = Camera.Framer()
    localController = Controller.GimbalController()

    time.sleep(2.0)
    fps = FPS().start()
    
    print("[INFO] start")
    while(cap.isOpened()):
        ret, frame = cap.read()
        outputFrame = cv2.flip(frame,1)

        localBounderies = localDetector.detect(frame)

        try: 
            midX = localBounderies[0] + ((localBounderies[2] - localBounderies[0])/2)
            midY = localBounderies[1] + ((localBounderies[3] - localBounderies[1])/2)     

            bboxLength = localBounderies[2] - localBounderies[0]
            bboxHeight = localBounderies[3] - localBounderies[1]          
        except: 
            pass

        centers = [np.array([[midX], [midY]])]

        if (len(centers) > 0):
            (x, y) = localTracker.predict()
            (x1, y1) = localTracker.update(centers[0])

        ksX = int(x1) - (bboxLength/2)
        keX = int(x1) + (bboxLength/2)

        ksY = int(y1) - (bboxHeight/2)
        keY = int(y1) + (bboxHeight/2)

        kalmanbounderies = (ksX, ksY,keX, keY)

        localController.sendCommands(kalmanbounderies)
        outputFrame = localFramer.frame(kalmanbounderies, frame)         

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