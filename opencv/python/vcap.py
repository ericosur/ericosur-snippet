#!/usr/bin/env python
#

import numpy as np
import cv2
import myutil

if __name__ == '__main__':
    app_name = 'vcap.py'
    data = myutil.read_setting('setting.json')

    video_index = data[app_name]['video_index']
    cap = cv2.VideoCapture(video_index)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        print("press 'q' to quit")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
