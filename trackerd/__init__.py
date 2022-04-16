#!/usr/bin/env python3

import cv2
import sys


class Tracker:

    def __init__ ():
       
        #create the tracker object
        tracker = cv2.TrackerKCF_create()


    def intiate_tracker (bbox):
       
        # Read video
        video = cv2.VideoCapture(0)

        # Exit if video not opened.
        if not video.isOpened():
            print("Could not open video")
            sys.exit()

        # Read first frame.
        ok, frame = video.read()
        if not ok:
            print('Cannot read video file')
            sys.exit()

        # Uncomment the line below to select a different bounding box
        bbox = bbox

        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)

    def tracking ():

        flag = True
        while flag:
            # Read a new frame
            ok, frame = video.read()
            if not ok:
                break

            # Start timer
            timer = cv2.getTickCount()

            # Update tracker
            ok, bbox = tracker.update(frame)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
                print(bbox)
            else :
                # Tracking failure
                flag = False
            
            # Display result
            cv2.imshow("Tracking", frame)         

        

            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27: break
                
