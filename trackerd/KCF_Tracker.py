#!/usr/bin/env python3

import cv2
import sys


class Tracker:

    def Initialize(self):
       
        #create the tracker object
        tracker = cv2.TrackerKCF_create()

        return self.tracker


    def intiate_tracker (self, bbox):
       
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
        ok = self.tracker.init(frame, bbox)

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
                

           

        # Display tracker type on frame
        #cv2.putText(frame, "KCF Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

        # Display FPS on frame
        #cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

      
        

    