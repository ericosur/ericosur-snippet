#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=line-too-long
# pylint: disable=too-many-locals

'''
from: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
python script that uses opencv to capture and record video
'''

from __future__ import print_function
#import numpy as np
import os
import sys
import cv2


OUTPUT_FN = 'capvid.avi'

def delete_if_exists(fn):
    '''
    Checks and deletes the output file
    You cant have a existing file or it will through an error
    '''
    if os.path.isfile(fn):
        os.remove(fn)


def main(video_id=0):
    '''main'''
    doWriteAVI = True
    ofn = OUTPUT_FN
    DEFAULT_WIDTH = 320
    DEFAULT_HEIGHT = 240

    cv2.namedWindow('aframe')
    cv2.moveWindow('aframe', 0, 0)

    if doWriteAVI:
        delete_if_exists(ofn)

    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_id)
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Unable to read camera feed, exit...")
        return

    # CAP_PROP_FRAME_WIDTH is defined at videoio.hpp
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, DEFAULT_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, DEFAULT_HEIGHT)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if doWriteAVI:
        #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #fourcc = cv2.VideoWriter_fourcc(*'8BPS')
        # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        out = cv2.VideoWriter(ofn, fourcc, 20, (frame_width, frame_height))

    print('press "q" or ESC to quit...')
    cnt = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            #aframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aframe = frame

            if doWriteAVI:
                # Write the frame into the file
                out.write(aframe)

            # Display the resulting frame
            cv2.imshow('aframe', aframe)

            # Press Q on keyboard to stop recording
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key == 0x1B:
                break
            if key & 0xFF == ord('s'):
                fn = f'pic{cnt:04d}.png'
                print(f'imwrite {fn}...')
                cv2.imwrite(fn, aframe)
                cnt += 1
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
