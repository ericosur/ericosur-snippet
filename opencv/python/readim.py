#!/usr/bin/env python
#

import json
import os
import myutil
import cv2
import matplotlib
import numpy as np


def cv_drawline():
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)

    # Draw a diagonal blue line with thickness of 5 px
    img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.imshow("foobar", img)
    cv2.waitKey(0)

def cv_test(filename):
    #img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("foobar", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    app_name = 'readim.py'
    data = myutil.read_setting('setting.json')
    home = os.environ['HOME']
    picpath = home + '/' + data[app_name]['path']
    print(picpath)

    cv2.namedWindow("foobar")
    cv2.moveWindow("foobar", 50, 50)

    if False:
        for img_file in data[app_name]['images']:
            pic1 = picpath + '/' + img_file
            print(pic1)
            if not os.path.isfile(pic1):
                print("file not found")
            else:
                cv_test(pic1)

    cv_drawline()
    cv2.destroyAllWindows()
