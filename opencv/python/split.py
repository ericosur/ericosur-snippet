#!/usr/bin/env python

import os, sys
import cv2
import numpy as np
import myutil

def output_img(file, img):
    print("output to: {}".format(file))
    cv2.imwrite(file, img)

def preprocess(src):
    img = cv2.resize(src, (300,300))
    img = img - 127.5
    #img = img * 0.007843
    return img

def apply_mean(src):
    b,g,r = cv2.split(src)
    #104,117,123
    b = np.subtract(b, 104)
    g = np.subtract(g, 117)
    r = np.subtract(r, 123)
    #zeros = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
    img = cv2.merge([b, g, r])
    return img


if __name__ == "__main__":
    app_name = 'split.py'
    data = myutil.read_setting('setting.json')

    home = os.environ["HOME"]
    image = home + '/' + data[app_name]['image_file']

    if not os.path.exists(image):
        print("image not found {}!".format(image))
        exit(1)

    img = cv2.imread(image)

    mrg = apply_mean(img)
    output_img('merged.png', mrg)

    newimg = preprocess(img)
    output_img('preproc.png', newimg)

    # When everything done, release the capture
    cv2.destroyAllWindows()
