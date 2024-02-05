#!/usr/bin/env python

'''
USAGE:
python auto_canny.py --images images
'''

# import the necessary packages
import argparse
import glob
import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
    ''' auto canny with default sigma '''
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    #print('lower:{} upper:{}'.format(lower, upper))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

def downscale(img, scale):
    ''' down scale the image, respect to original ratio
        scale from 0.1 to 0.99
    '''
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
    return resized

def main():
    ''' main '''
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", required=True,
        help="path to input dataset of images")
    args = vars(ap.parse_args())

    # loop over the images
    for imagePath in glob.glob(args["images"] + "/*.jpg"):
        # load the image, convert it to grayscale, and blur it slightly
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)

        # apply Canny edge detection using a wide threshold, tight
        # threshold, and automatically determined threshold
        wide = cv2.Canny(blurred, 10, 200)
        tight = cv2.Canny(blurred, 225, 250)
        auto = auto_canny(blurred)

        # do we need resize?
        size_limit = 400
        if image.shape[1] > size_limit:
            scale = size_limit / image.shape[1]
            wide = downscale(wide, scale)
            tight = downscale(tight, scale)
            auto = downscale(auto, scale)

        # show the images
        cv2.imshow("Original", image)
        cv2.imshow("Edges", np.hstack([wide, tight, auto]))

        key = cv2.waitKey()
        if key == 0x1B:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
