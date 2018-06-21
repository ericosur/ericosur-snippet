#!/usr/bin/env python
#
# further reading: https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
#

import numpy as np
import cv2
import myutil


class MyCap:
    def __init__(self, readConfig=True, name='gblur.py'):
        self.name = name

        # default values
        self.width = 640
        self.height = 480
        self.video_index = 0
        self.win_count = 0
        self.sigmaX = 5
        self.sigmaY = 5
        if readConfig:
            self.read_config()
        self.init_window()

    def read_config(self):
        # read settings from json
        app_name = self.name
        data = myutil.read_setting('setting.json')
        try:
            #self.foobar = data[app_name]['foo_bar']
            self.video_index = data[app_name]['video_index']
            print("video input from: {}".format(self.video_index))
            self.width = data[app_name]['width']
            self.height = data[app_name]['height']
            self.sigmaX = data[app_name]['sigmaX']
            self.sigmaY = data[app_name]['sigmaY']
        except KeyError:
            print('no such key, fallback using default values')
        print('config read...')

    def init_window(self):

        cv2.namedWindow('rgb')
        self.win_count += 1
        cv2.moveWindow('rgb', 0, 0)

        cv2.namedWindow('blur')
        self.win_count += 1
        cv2.moveWindow('blur', self.width, 0)
        print('init_window...')

    def action(self):
        cap = cv2.VideoCapture(self.video_index)
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
            print("press 'q' to quit")
            while(True):
                # Capture frame-by-frame
                ret, frame = cap.read()

                if self.win_count == 0:
                    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2.imshow('frame', frame)
                else:
                    # Our operations on the frame come here
                    blur = cv2.GaussianBlur(frame, (self.sigmaX, self.sigmaY), 0)
                    cv2.imshow('rgb', frame)
                    cv2.imshow('blur', blur)


                key = cv2.waitKey(1)
                if key & 0xFF == ord('q') or key == 27:
                    break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


def main():
    foo = MyCap()
    foo.action()


if __name__ == '__main__':
    main()
