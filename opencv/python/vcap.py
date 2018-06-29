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
        self.hasHSV = True
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
            self.hasTest = data[app_name]['test']
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

        cv2.namedWindow('skin')
        cv2.moveWindow('skin', 0, 300)
        print('init_window...')

    def split_blue(self, img):
        #img = cv2.resize(img, (self.width, self.height))
        b,g,r = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype=img.dtype)
        #cv2.imshow('red', cv2.merge([zeros, zeros, r]))

        no_blue_img = cv2.merge([b, g, r])
        return no_blue_img
        #cv2.imshow('green', cv2.merge([zeros, g, zeros]))

    def skin_mask(self, img):
        # refer: https://www.programcreek.com/python/example/70440/cv2.findContours
        # refer: https://stackoverflow.com/questions/17124381/determine-skeleton-joints-with-a-webcam-not-kinect/17375222#17375222

        # refer: https://www.researchgate.net/publication/262371199_Explicit_image_detection_using_YCbCr_space_color_model_as_skin_detection

        im2 = img.copy()
        # Constants for finding range of skin color in YCrCb
        min_YCrCb = np.array([80, 130, 80], np.uint8)
        max_YCrCb = np.array([255 ,183 ,120], np.uint8)
        imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        skin = cv2.inRange(imgYCrCb, min_YCrCb, max_YCrCb)

        # Do contour detection on skin region
        foo, contours, hierarchy = cv2.findContours(skin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #foo, contours, hierarchy = cv2.findContours(skin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        #cv2.drawContours(im2, contours,-1,(127,255,0),1)

        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            if area > 400:
                cv2.drawContours(im2, contours, i, (128,255,0), 1)

        cv2.imshow('skin', im2);

        '''
        # apply erosions and dilations to the mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
        skinMask = cv2.GaussianBlur(skinMask, (3,3), 0)
        skin = cv2.bitwise_and(img, img, mask=skinMask)
        #cv2.imshow('skin mask', np.hstack([img, skin]))
        '''


    def action(self):
        cap = cv2.VideoCapture(self.video_index)
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
            print("press 'q' to quit")
            while(True):
                # Capture frame-by-frame
                ret, frame = cap.read()
                self.skin_mask(frame)

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

                    if self.hasHSV:
                        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        cv2.imshow('hsv', hsv)


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
