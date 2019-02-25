#!/usr/bin/env python3

import cv2
import numpy as np
from loadimgur import load_image

def add_border(src):
    #borderType = cv2.BORDER_DEFAULT | cv2.BORDER_ISOLATED
    borderType = cv2.BORDER_ISOLATED
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

def main():
    # load sample image from imgur
    img = load_image('https://i.imgur.com/Dd30pDt.jpg')
    print(img.shape) # height, width, channel
    #show_img(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    dst = add_border(img)
    show_img(dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
