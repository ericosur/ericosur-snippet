#!/usr/bin/env python

import cv2
import numpy as np

def add_border(src):
    borderType = cv2.BORDER_DEFAULT | cv2.BORDER_ISOLATED
    #borderType = cv2.BORDER_ISOLATED
    top = 80
    bottom = 80
    left = 80
    right = 80
    dst = cv2.copyMakeBorder(src, top, bottom, left, right, borderType)
    return dst

def show_img(img):
    cv2.namedWindow('img')
    cv2.moveWindow('img', 0, 0)
    cv2.imshow('img', img)


fn = "emma.jpg"
src = cv2.imread(fn)
print(src.shape)
w = src.shape[1]
h = src.shape[0]
show_img(src)


cv2.waitKey(0)
