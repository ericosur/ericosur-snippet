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
import os
import math
import cv2
import numpy as np
from imgconfig import read_image_config

# pylint: disable=too-many-locals
class MyCap():
    ''' class to do video capturing '''

    # pylint: disable=too-many-instance-attributes
    # I DO know what I am doing

    def __init__(self, useDefault=False, name='hough.py'):
        ''' init function '''
        self.name = name

        # default values
        self.width = 640
        self.height = 480
        self.win_count = 0
        if not useDefault:
            self.read_config()

    def read_config(self):
        ''' read settings from json '''
        app_name = self.name
        data = read_image_config()
        try:
            self.width = data[app_name]['width']
            self.height = data[app_name]['height']
        except KeyError:
            print('no such key, fallback using default values')
        print('config read...')

    @staticmethod
    def init_window():
        ''' init multiple showing windows '''
        #cv2.namedWindow('rgb', flags=cv2.WINDOW_AUTOSIZE)
        #cv2.moveWindow('rgb', 0, 0)
        cv2.namedWindow('test', flags=cv2.WINDOW_AUTOSIZE)
        #cv2.moveWindow('test', 0, int(self.height*1.5))
        cv2.moveWindow('test', 0, 0)
        print('init_window...')

    def action(self):
        ''' invoking entry function '''
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print('ERROR: cannot open video capture device...')
            cap.release()
            return

        MyCap.init_window()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cap.set(cv2.CAP_PROP_FPS, 30)
        print("press 'q' to quit")
        while True:
            e0 = cv2.getTickCount()
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break

            #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = frame
            #cv2.imshow('rgb', rgb)

            ifrm = frame.copy()
            cvimg = hough_lines(ifrm)

            e1 = cv2.getTickCount()
            elapsed = (e1 - e0) / cv2.getTickFrequency()
            show_fps(rgb, elapsed)
            result_img = np.concatenate((rgb, cvimg), axis=1)
            #blue = self.split_blue(ifrm)
            cv2.imshow('test', result_img)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key == 27:
                break
            if key == ord('s'):
                self.save_image(result_img)

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def save_image(img):
        ''' save image '''
        cnt = 0
        while True:
            fn = f'hough{cnt:03d}.jpg'
            if not os.path.exists(fn):
                break
            cnt += 1

        cv2.imwrite(fn, img)


def show_fps(img, elapsed_time):
    ''' put text of elapse time and FPS from input image '''
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.75
    #baseline = 0
    #thickness = 2
    fps = 1.0 / elapsed_time
    msg = f"elapsed: {elapsed_time:.3f} fps({fps:.1f})"
    cv2.putText(img, msg, (10, 30), fontface, scale, (255, 0, 255), 1, cv2.LINE_AA)
    return img

def auto_canny(image, sigma=0.33):
    ''' auto determine the parameters of canny '''
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    #print('lower:{} upper:{}'.format(lower, upper))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


def hough_lines(src):
    ''' reference from opencv python examples houghlines.py '''
    #dst = cv2.Canny(src, 50, 200)
    dst = auto_canny(src, sigma=0.5)

    #cv2.imshow('test', dst)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    #cdst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    use_houghlinep = True
    if use_houghlinep: # HoughLinesP
        threshold = 75
        min_line_len = 80
        max_line_gap = 30
        lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, threshold, np.array([]),
            min_line_len, max_line_gap)
        try:
            a, b, _ = lines.shape
            for i in range(a):
                p1 = (lines[i][0][0], lines[i][0][1])
                p2 = (lines[i][0][2], lines[i][0][3])
                cv2.line(cdst, p1, p2, (0, 0, 255), 2, cv2.LINE_AA)

        except AttributeError:
            print('.', end='')

    else:    # HoughLines
        threshold = 150
        lines = cv2.HoughLines(dst, 1, math.pi/180.0, threshold, np.array([]), 0, 0)
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
