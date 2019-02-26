#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' split image into multiple channels '''

from __future__ import print_function
import os
import cv2
import numpy as np
import myutil

THUMBNAIL_HEIGHT = 300
THUMBNAIL_WIDTH = 300

def output_img(fn, img):
    ''' imshow specified image file '''
    #print("output to: {}".format(fn))
    #cv2.imwrite(fn, img)
    cv2.imshow(fn, img)

def preprocess(src):
    ''' resize image and minus mean value '''
    img = cv2.resize(src, (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    img = img - 127.5
    #img = img * 0.007843
    return img

def apply_mean(src):
    ''' apply some mean values '''
    img = cv2.resize(src, (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    b, g, r = cv2.split(img)
    #104,117,123
    b = np.subtract(b, 104)
    g = np.subtract(g, 117)
    r = np.subtract(r, 123)
    #zeros = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
    img = cv2.merge([b, g, r])
    return img

def setup_windows():
    ''' setup showing windows '''
    cv2.namedWindow('red')
    cv2.moveWindow('red', 0, 0)
    cv2.namedWindow('green')
    cv2.moveWindow('green', THUMBNAIL_WIDTH, 0)
    cv2.namedWindow('blue')
    cv2.moveWindow('blue', THUMBNAIL_WIDTH * 2, 0)
    cv2.namedWindow('merged.png')
    cv2.moveWindow('merged.png', 0, THUMBNAIL_HEIGHT+50)
    cv2.namedWindow('preproc.png')
    cv2.moveWindow('preproc.png', THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT+50)


def split_and_show(img):
    ''' split into multiple channels and show '''
    img = cv2.resize(img, (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    b, g, r = cv2.split(img)
    zeros = np.zeros(img.shape[:2], dtype=img.dtype)
    cv2.imshow('red', cv2.merge([zeros, zeros, r]))
    cv2.imshow('blue', cv2.merge([b, zeros, zeros]))
    cv2.imshow('green', cv2.merge([zeros, g, zeros]))

def main():
    '''main function'''
    app_name = 'split.py'
    data = myutil.read_setting('setting.json')

    home = os.environ["HOME"]
    image = home + '/' + data[app_name]['image_file']

    if not os.path.exists(image):
        print("image not found {}!".format(image))
        exit(1)

    setup_windows()

    img = cv2.imread(image)
    split_and_show(img)

    mrg = apply_mean(img)
    output_img('merged.png', mrg)

    newimg = preprocess(img)
    output_img('preproc.png', newimg)

    print('press any key to quit...')
    cv2.waitKey()
    # When everything done, release the capture
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
