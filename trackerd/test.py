import cv2
import sys
import KCF_tracker as KCF

if __name__ == '__main__':
    
    bbox = (287, 23, 86, 320)    
    localtracker = KCF.Tracker()
    localtracker.intiate_tracker(bbox)
    localtracker.tracking()
