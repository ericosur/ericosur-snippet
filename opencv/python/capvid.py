#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long

'''
from: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
python script that uses opencv to capture and record video
'''

from __future__ import print_function
#import numpy as np
import os
import sys
import cv2

OUTPUT_FN = 'outpy.avi'

def delete_if_exists(fn):
    '''
    Checks and deletes the output file
    You cant have a existing file or it will through an error
    '''
    if os.path.isfile(fn):
        os.remove(fn)


def main(video_id=0):
    '''main'''
    doWriteAVI = False
    ofn = OUTPUT_FN

    if doWriteAVI:
        delete_if_exists(ofn)

    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_id)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Unable to read camera feed")
        return

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    if doWriteAVI:
        #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #fourcc = cv2.VideoWriter_fourcc(*'8BPS')
        # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        out = cv2.VideoWriter(ofn, fourcc, 30, (frame_width, frame_height), False)

    print('press "q" or ESC to quit...')
    while True:
        ret, frame = cap.read()
        if ret:
            aframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if doWriteAVI:
                # Write the frame into the file
                out.write(aframe)

            # Display the resulting frame
            cv2.imshow('aframe', aframe)

            # Press Q on keyboard to stop recording
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key == 0x1B:
                break
        # Break the loop
        else:
            break

    # When everything done, release the video capture and video write objects
    cap.release()
    if doWriteAVI:
        out.release()
    # Closes all the frames
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main(video_id=int(sys.argv[1]))
        else:
            main()
    except ValueError:
        print('Usage: ./capvid.py [video_id]')
