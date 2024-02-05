#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# pylint: disable=line-too-long
#

'''
further reading: https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object

refer: https://www.programcreek.com/python/example/70440/cv2.findContours
refer: https://stackoverflow.com/questions/17124381/determine-skeleton-joints-with-a-webcam-not-kinect/17375222#17375222
refer: https://www.researchgate.net/publication/262371199_Explicit_image_detection_using_YCbCr_space_color_model_as_skin_detection
'''


from __future__ import print_function
import math
from time import sleep
import cv2
import numpy as np
from imgconfig import read_image_config


class MyCap():
    ''' class to do video capturing '''

    # pylint: disable=too-many-instance-attributes
    # I DO know what I am doing

    def __init__(self, useDefault=False, name='vcap.py'):
        ''' init function '''
        self.name = name

        # default values
        self.width = 640
        self.height = 480
        self.video_index = 0
        self.has_gray = False
        self.has_bgr = False
        self.has_rgb = False
        self.has_hsv = False
        self.has_skin = False
        self.has_test = True
        self.win_count = 0
        if not useDefault:
            self.read_config()

    def read_config(self):
        ''' read settings from json '''
        app_name = self.name
        data = read_image_config()
        try:
            #self.foobar = data[app_name]['foo_bar']
            self.video_index = data[app_name]['video_index']
            print(f"video input from: {self.video_index}")
            self.width = data[app_name]['width']
            self.height = data[app_name]['height']
            self.has_gray = data[app_name]['gray']
            self.has_rgb = data[app_name]['rgb']
            self.has_test = data[app_name]['test']
        except KeyError:
            print('no such key, fallback using default values')
        print('config read...')

    def init_window(self):
        ''' init multiple showing windows '''
        print('window init...')
        if self.has_gray:
            cv2.namedWindow('gray', flags=cv2.WINDOW_AUTOSIZE)
            self.win_count += 1
            cv2.moveWindow('gray', int(self.width * 1.5), 0)
        if self.has_rgb:
            cv2.namedWindow('rgb', flags=cv2.WINDOW_AUTOSIZE)
            self.win_count += 1
            cv2.moveWindow('rgb', 0, 0)
        if self.has_test:
            cv2.namedWindow('test', flags=cv2.WINDOW_AUTOSIZE)
            cv2.moveWindow('test', 0, int(self.height*1.5))
        if self.has_skin:
            cv2.namedWindow('skin')
            cv2.moveWindow('skin', 0, 300)
        print('window initialized...')

    @staticmethod
    def split_blue(img):
        ''' split blue from image '''
        #img = cv2.resize(img, (self.width, self.height))
        b, g, r = cv2.split(img)    # pylint: disable=unused-variable
        zeros = np.zeros(img.shape[:2], dtype=img.dtype)
        #cv2.imshow('red', cv2.merge([zeros, zeros, r]))

        no_blue_img = cv2.merge([zeros, g, r])
        return no_blue_img
        #cv2.imshow('green', cv2.merge([zeros, g, zeros]))

    @staticmethod
    def skin_mask(img):
        ''' test skin mask '''

        im2 = img.copy()
        # Constants for finding range of skin color in YCrCb
        min_YCrCb = np.array([80, 130, 80], np.uint8)
        max_YCrCb = np.array([255, 183, 120], np.uint8)
        imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        skin = cv2.inRange(imgYCrCb, min_YCrCb, max_YCrCb)

        # Do contour detection on skin region
        # pylint: disable=line-too-long
        # pylint: disable=unused-variable
        cimage, contours, hierarchy = cv2.findContours(skin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #foo, contours, hierarchy = cv2.findContours(skin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # pylint: enable=line-too-long
        # pylint: enable=unused-variable

        #cv2.drawContours(im2, contours,-1,(127,255,0),1)

        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            if area > 400:
                cv2.drawContours(im2, contours, i, (128, 255, 0), 1)

        cv2.imshow('skin', im2)

        # # apply erosions and dilations to the mask
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
        # skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        # skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
        # skinMask = cv2.GaussianBlur(skinMask, (3,3), 0)
        # skin = cv2.bitwise_and(img, img, mask=skinMask)
        # #cv2.imshow('skin mask', np.hstack([img, skin]))


    def action(self):
        ''' invoking entry function '''
        cap = cv2.VideoCapture(self.video_index)
        if not cap.isOpened():
            print('ERROR: cannot open video capture device...')
            cap.release()
            return

        self.init_window()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        print("press 'q' to quit")
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print('.')
                sleep(0.05)
                break

            if self.has_skin:
                self.skin_mask(frame)

            if self.win_count == 0:
                #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.imshow('frame', frame)

            else:
                # Our operations on the frame come here
                if self.has_gray:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('gray', gray)

                if self.has_rgb:
                    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    rgb = frame
                    cv2.imshow('rgb', rgb)

                if self.has_test:
                    ifrm = frame.copy()
                    e0 = cv2.getTickCount()
                    cvimg = hough_lines(ifrm)
                    e1 = cv2.getTickCount()
                    elapsed = (e1 - e0) / cv2.getTickFrequency()
                    show_fps(cvimg, elapsed)
                    #blue = self.split_blue(ifrm)
                    cv2.imshow('test', cvimg)

                if self.has_hsv:
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    cv2.imshow('hsv', hsv)


            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key == 27:
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


def show_fps(img, elapsed_time):
    ''' put text of elapse time and FPS from input image '''
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.75
    #baseline = 0
    #thickness = 2
    fps = 1.0 / elapsed_time
    msg = f"elapsed: {elapsed_time:.3f} fps({fps:.1f})"
    cv2.putText(img, msg, (10, 35), fontface, scale, (127, 0, 255), 1, cv2.LINE_AA)
    return img


def hough_lines(src):
    ''' reference from opencv python examples houghlines.py '''
    dst = cv2.Canny(src, 50, 200)
    #cv2.imshow('test', dst)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    #cdst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    use_houghlinep = True
    if use_houghlinep: # HoughLinesP
        lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 40, np.array([]), 50, 10)
        try:
            a, b, _ = lines.shape
            for i in range(a):
                cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]),
                         (0, 0, 255), 3, cv2.LINE_AA)
        except AttributeError:
            print('.', end='')

    else:    # HoughLines
        lines = cv2.HoughLines(dst, 1, math.pi/180.0, 50, np.array([]), 0, 0)
        if lines is not None:
            a, b, _ = lines.shape
            for i in range(a):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0, y0 = a*rho, b*rho
                pt1 = (int(x0+1000*(-b)), int(y0+1000*(a)))
                pt2 = (int(x0-1000*(-b)), int(y0-1000*(a)))
                cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
    #cv2.imshow("test", cdst)
    return cdst


def main():
    '''main function'''
    #print('using opencv version: {}'.format(cv2.__version__))
    mycap = MyCap()
    mycap.action()
    print()

if __name__ == '__main__':
    main()
