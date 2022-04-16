import cv2
import sys
import KCF_Tracker as KCF

if __name__ == '__main__':
    
    bbox = (287, 23, 86, 320)
    KCF.Tracker.Initialize(KCF.tracker)
    KCF.Tracker.intiate_tracker(KCF.tracker, bbox)
