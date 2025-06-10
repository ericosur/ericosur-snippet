#!/usr/bin/python3
# coding: utf-8

''' image compare '''

# import the necessary packages
import argparse
import cv2
from skimage.measure import compare_ssim

def main():
    ''' main '''
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--first", required=True,
        help="first input image")
    ap.add_argument("-s", "--second", required=True,
        help="second")
    args = vars(ap.parse_args())

    # load the two input images
    imageA = cv2.imread(args["first"])
    imageB = cv2.imread(args["second"])

    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

if __name__ == '__main__':
    main()
