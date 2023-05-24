#!/usr/bin/python
# coding: utf-8
#
# pylint: disable=no-member
# pylint: disable=wrong-import-position

'''
stack two different dimension images into one

if using imagemagick, (it's default background is white)
veritical:
    convert -append top.jpg bot.jpg vis.jpg
horizontally:
    convert +append top.jpg bot.jpg hoz.jpg
'''

import cv2
import numpy as np

def append_image_vertically(top_img, bottom_img):
    ''' input top_img, bottom_img, write out.png '''
    h1, w1 = top_img.shape[:2]
    h2, w2 = bottom_img.shape[:2]
    vis = np.zeros((h1+h2, max(w1,w2), 3), np.uint8)
    vis[:h1, :w1, :3] = top_img
    vis[h1:h1+h2, :w2, :3] = bottom_img
    return vis

def append_image_horizontally(left_img, right_img):
    ''' input top_img, bottom_img, write out.png '''
    h1, w1 = left_img.shape[:2]
    h2, w2 = right_img.shape[:2]
    hoz = np.zeros((max(h1,h2), w1+w2, 3), np.uint8)
    print(hoz.shape[:2])
    hoz[:h1, :w1, :3] = left_img
    hoz[:h2, w1:w1+w2, :3] = right_img
    return hoz

def main():
    ''' main, combin two images vertifcally '''
    top = cv2.imread("top.jpg")
    bot = cv2.imread("bot.jpg")
    vis = append_image_vertically(top, bot)
    hoz = append_image_horizontally(top, bot)
    cv2.imwrite('vis.jpg', vis)
    cv2.imwrite('hoz.jpg', hoz)


if __name__ == '__main__':
    main()
