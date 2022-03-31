import cv2
import numpy as np
import MobileNetSSD

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    localDetector = MobileNetSSD.Detector()
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        localBounderies = localDetector.detect(frame)
        print(localBounderies)

        frame = localDetector.getCurruntFrameWithBoundingBox()

        cv2.imshow('Lazy Lanes', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()