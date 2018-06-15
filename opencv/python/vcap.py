#!/usr/bin/env python
#
# further reading: https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
#

import numpy as np
import cv2
import myutil


class MyCap:
    def __init__(self, useDefault=False, name='vcap.py'):
        self.name = name

        # default values
        self.width = 640
        self.height = 480
        self.video_index = 0
        self.hasGray = False
        self.hasBGR = False
        self.hasRGB = False
        self.hasTest = True
        self.win_count = 0
        if not useDefault:
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
            self.hasGray = data[app_name]['gray']
            self.hasRGB = data[app_name]['rgb']
        except KeyError:
            print('no such key, fallback using default values')
        print('config read...')

    def init_window(self):

        if self.hasGray:
            cv2.namedWindow('gray', flags=cv2.WINDOW_AUTOSIZE)
            self.win_count += 1
            cv2.moveWindow('gray', int(self.width * 1.5), 0)
        if self.hasRGB:
            cv2.namedWindow('rgb', flags=cv2.WINDOW_AUTOSIZE)
            self.win_count += 1
            cv2.moveWindow('rgb', 0, 0)
        if self.hasTest:
            cv2.namedWindow('test', flags=cv2.WINDOW_AUTOSIZE)
            cv2.moveWindow('test', 0, int(self.height*1.5))

        print('init_window...')

    def split_blue(self, img):
        #img = cv2.resize(img, (self.width, self.height))
        b,g,r = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype=img.dtype)
        #cv2.imshow('red', cv2.merge([zeros, zeros, r]))

        no_blue_img = cv2.merge([b, g, r])
        return no_blue_img
        #cv2.imshow('green', cv2.merge([zeros, g, zeros]))


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
                    if self.hasGray:
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('gray', gray)

                    if self.hasRGB:
                        #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        rgb = frame
                        cv2.imshow('rgb', rgb)

                    if self.hasTest:
                        ifrm = frame.copy()
                        blue = self.split_blue(ifrm)
                        cv2.imshow('test', blue)


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
