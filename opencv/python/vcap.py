#!/usr/bin/env python
#

import numpy as np
import cv2
import myutil

def init_window(width):
    cv2.namedWindow("frame")
    cv2.namedWindow("gray")
    cv2.moveWindow("frame", 0, 0)
    cv2.moveWindow("gray", width, 0)

if __name__ == '__main__':

    # read settings from json
    app_name = 'vcap.py'
    data = myutil.read_setting('setting.json')
    video_index = data[app_name]['video_index']
    print("video input from: {}".format(video_index))
    Width = data[app_name]['width']
    Height = data[app_name]['height']
    init_window(Width)

    cap = cv2.VideoCapture(video_index)
    if cap.isOpened():
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, Width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Height)
        print("press 'q' to quit")
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            frame -= 128
            # Display the resulting frame
            cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
