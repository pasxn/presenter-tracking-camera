import cv2
import numpy as np
from imutils.video import FPS
import time
import sys
import os 

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from detectord import MobileNetSSD
import KCF_tracker

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
            print(localBounderies)
            
            frame = localTracker.getCurruntFrameWithBoundingBox()
        else:
            tracker.inputPerson(localDetector.detect(frame))

        cv2.imshow('Lazy Lanes', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        fps.update()
    
    fps.stop()

    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cap.release()
    cv2.destroyAllWindows()