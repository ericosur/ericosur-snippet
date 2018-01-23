#!/usr/bin/env python

import os, sys
import cv2
import numpy as np
import myutil

thumbnail_height = 300
thumbnail_width = 300

def output_img(file, img):
    #print("output to: {}".format(file))
    #cv2.imwrite(file, img)
    cv2.imshow(file, img)

def preprocess(src):
    img = cv2.resize(src, (thumbnail_width, thumbnail_height))
    img = img - 127.5
    #img = img * 0.007843
    return img

def apply_mean(src):
    img = cv2.resize(src, (thumbnail_width, thumbnail_height))
    b,g,r = cv2.split(img)
    #104,117,123
    b = np.subtract(b, 104)
    g = np.subtract(g, 117)
    r = np.subtract(r, 123)
    #zeros = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
    img = cv2.merge([b, g, r])
    return img

def setup_windows():
    cv2.namedWindow('red')
    cv2.moveWindow('red', 0, 0)
    cv2.namedWindow('green')
    cv2.moveWindow('green', thumbnail_width, 0)
    cv2.namedWindow('blue')
    cv2.moveWindow('blue', thumbnail_width*2, 0)
    cv2.namedWindow('merged.png')
    cv2.moveWindow('merged.png', 0, thumbnail_height+50)
    cv2.namedWindow('preproc.png')
    cv2.moveWindow('preproc.png', thumbnail_width, thumbnail_height+50)


def split_and_show(img):
    img = cv2.resize(img, (thumbnail_width, thumbnail_height))
    b,g,r = cv2.split(img)
    zeros = np.zeros(img.shape[:2], dtype=img.dtype)
    cv2.imshow('red', cv2.merge([zeros, zeros, r]))
    cv2.imshow('blue', cv2.merge([b, zeros, zeros]))
    cv2.imshow('green', cv2.merge([zeros, g, zeros]))

if __name__ == "__main__":
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

    cv2.waitKey()
    # When everything done, release the capture
    cv2.destroyAllWindows()
