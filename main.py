#!/usr/bin/env python3 

import cv2
import numpy as np
from imutils.video import FPS
import time
import multiprocessing
from detectord import MobileNetSSD
from trackerd import KalmanFilter
from framed import Camera
from gimbald import Controller
from streamd import Server
from loggerd import Logger

# Keep track of processes
PROCESSES = []

# Keep track of FPS
fps = FPS().start()

def vision(manager):
    cap = cv2.VideoCapture(0); cap.set(3,640); cap.set(4,480)
    localDetector = MobileNetSSD.Detector()
    localTracker = KalmanFilter.Kalmanfilter(0.1, 1, 1, 1, 0.1,0.1)
    localFramer = Camera.Framer()
    localController = Controller.GimbalController()
    loggr = Logger.Datalogger("vision")
    
    loggr.LOG("start")
    while(cap.isOpened()):
        ret, frame = cap.read()

        localBounderies = localDetector.detect(frame)

        try: 
            localBounderies_0, localBounderies_1 = localBounderies[0], localBounderies[1]
            localBounderies_2, localBounderies_3 = localBounderies[2], localBounderies[3]
            
            midX = localBounderies_0 + ((localBounderies_1 - localBounderies_0)/2)
            midY = localBounderies_1 + ((localBounderies_3 - localBounderies_1)/2)     

            bboxLength = localBounderies_2 - localBounderies_0
            bboxHeight = localBounderies_3 - localBounderies_1          
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

        encodeParameter = [int(cv2.IMWRITE_JPEG_QUALITY), 65]
        manager[0] = cv2.imencode('.jpg', outputFrame, encodeParameter)[1]

        fps.update()
    
    fps.stop()

    loggr.LOG("elapsed time: {:.2f}".format(fps.elapsed()))
    loggr.LOG("approx. FPS: {:.2f}".format(fps.fps()))

    cap.release()
    cv2.destroyAllWindows()

def main():
    manager = multiprocessing.Manager()
    lst = manager.list()
    lst.append(None)

    httpServer = multiprocessing.Process(target=Server.server)
    socketHandler = multiprocessing.Process(target=Server.socket, args=(lst,))
    cameraHandler = multiprocessing.Process(target=vision, args=(lst,))

    PROCESSES.append(cameraHandler)
    PROCESSES.append(httpServer)
    PROCESSES.append(socketHandler)

    for p in PROCESSES:
        p.start()
    while True:
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        for p in PROCESSES:
            p.terminate()