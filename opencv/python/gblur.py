#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
further reading:
https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
'''

from __future__ import print_function
#import numpy as np
import cv2

from imgconfig import read_image_config

class MyCap():
    ''' class MyCap to capture video from webcam and perform blur '''

    def __init__(self, readConfig=True, name='gblur.py'):
        self.name = name

        # default values
        self.width = 640
        self.height = 480
        self.video_index = 0
        self.win_count = 0
        self.sigma_x = 5
        self.sigma_y = 5
        if readConfig:
            self.read_config()
        self.init_window()

    def read_config(self):
        ''' read settings from json '''
        app_name = self.name
        data = read_image_config()
        try:
            #self.foobar = data[app_name]['foo_bar']
            self.video_index = data[app_name]['video_index']
            print("video input from:", self.video_index)
            self.width = data[app_name]['width']
            self.height = data[app_name]['height']
            self.sigma_x = data[app_name]['sigma_x']
            self.sigma_y = data[app_name]['sigma_y']
        except KeyError:
            print('no such key, fallback using default values')
        print('config read...')

    def init_window(self):
        ''' init windows for imshow '''
        cv2.namedWindow('rgb')
        self.win_count += 1
        cv2.moveWindow('rgb', 0, 0)

        cv2.namedWindow('blur')
        self.win_count += 1
        cv2.moveWindow('blur', self.width, 0)
        print('init_window...')

    def action(self):
        ''' open webcam and perform action '''
        cap = cv2.VideoCapture(self.video_index)
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
            print("press 'q' to quit")
            while True:
                # Capture frame-by-frame
                ret, frame = cap.read()
                if not ret:
                    break

                if self.win_count == 0:
                    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2.imshow('frame', frame)
                else:
                    # Our operations on the frame come here
                    blur = cv2.GaussianBlur(frame, (self.sigma_x, self.sigma_y), 0)
                    cv2.imshow('rgb', frame)
                    cv2.imshow('blur', blur)

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q') or key == 27:
                    break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


def main():
    ''' main function '''
    mycap = MyCap()
    mycap.action()


if __name__ == '__main__':
    main()
