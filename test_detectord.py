import cv2
import numpy as np
from imutils.video import FPS
import time
from detectord import MobileNetSSD

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    localDetector = MobileNetSSD.Detector()

    time.sleep(2.0)
    fps = FPS().start()
    
    print("[INFO] start")
    while(cap.isOpened()):
        ret, frame = cap.read()
        localBounderies = localDetector.detect(frame)
        print("[INFO] decettion successful, person bounderies: {}".format(localBounderies))

        frame = localDetector.getCurruntFrameWithBoundingBox()

        cv2.imshow('detectord test', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        fps.update()
    
    fps.stop()

    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cap.release()
    cv2.destroyAllWindows()