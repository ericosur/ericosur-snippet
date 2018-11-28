#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=import-error

# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
#   This example program shows how to find frontal human faces in a webcam stream using OpenCV.
#   It is also meant to demonstrate that rgb images from Dlib can be used with opencv by just
#   swapping the Red and Blue channels.
#
#   You can run this program and see the detections from your webcam by executing the
#   following command:
#       ./opencv_face_detection.py
#
#   This face detector is made using the now classic Histogram of Oriented
#   Gradients (HOG) feature combined with a linear classifier, an image
#   pyramid, and sliding window detection scheme.  This type of object detector
#   is fairly general and capable of detecting many types of semi-rigid objects
#   in addition to human faces.  Therefore, if you are interested in making
#   your own object detectors then read the train_object_detector.py example
#   program.
#
#
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#
#   Compiling dlib should work on any operating system so long as you have
#   CMake installed.  On Ubuntu, this can be done easily by running the
#   command:
#       sudo apt-get install cmake
#
#   Also note that this example requires Numpy which can be installed
#   via the command:
#       pip install numpy

# ref: http://dlib.net/face_landmark_detection.py.html
# ref: opencv_webcam_face_detection.py

''' this script is modified from example from dlib '''
''' it could run but cannot detect any face '''

from __future__ import print_function
import cv2
import numpy as np
import dlib
from myutil import isfile

class Foo(object):
    ''' simple class to run dlib face landmarks function '''

    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        #self.tracker = dlib.correlation_tracker()
        #self.win = dlib.image_window()

        self.inited = False
        self.default_width = 640
        self.default_height = 480

        # dat download from: http://dlib.net/face_landmark_detection.py.html
        predictor_data = 'shape_predictor_68_face_landmarks.dat'
        if isfile(predictor_data):
            self.detector = dlib.get_frontal_face_detector()
            self.predictor = dlib.shape_predictor(predictor_data)
            self.inited = True
        else:
            print('need predictor data file, use the following command to fetch data file')
            print('wget {}\n'.format(predictor_data))
            return

    '''
    def tracking(self):
        # Create the correlation tracker - the object needs to be initialized
        # before it can be used

        # We will track the frames as we load them off of disk
        for k, f in enumerate(sorted(glob.glob(os.path.join(video_folder, "*.jpg")))):
            print("Processing Frame {}".format(k))
            img = dlib.load_rgb_image(f)

            # We need to initialize the tracker on the first frame
            if k == 0:
                # Start a track on the juice box. If you look at the first frame you
                # will see that the juice box is contained within the bounding
                # box (74, 67, 112, 153).
                tracker.start_track(img, dlib.rectangle(74, 67, 112, 153))
            else:
                # Else we just attempt to track from the previous frame
                tracker.update(img)

            win.clear_overlay()
            win.set_image(img)
            win.add_overlay(tracker.get_position())
    '''

    def action(self):
        '''test actions'''
        if not self.inited:
            print('no init ok, exit...')
            return

        cam = cv2.VideoCapture(0)
        if not cam.isOpened:
            print('cannot open camera...')
            return
        cam.set(3, self.default_width)
        cam.set(4, self.default_height)
        color_green = (0, 255, 0)
        line_width = 1
        while True:
            ret, img = cam.read()
            if not ret:
                break

            #rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #dets = self.detector(rgb_image)
            dets = self.detector(gray_image)
            if dets:
                cv2.putText(img, 'no dets', (10, 40), self.font, 1, (127, 0, 255), 2, cv2.LINE_AA)
            else:
                for det in dets:
                    cv2.rectangle(img, (det.left(), det.top()),
                                  (det.right(), det.bottom()), color_green, line_width)
                    landmarks = np.matrix([[p.x, p.y] for p in self.predictor(img, det).parts()])
                    for idx, point in enumerate(landmarks):
                        pos = (point[0, 0], point[0, 1])
                        cv2.circle(img, pos, 2, color=(0, 255, 0))
                        cv2.putText(img, str(idx + 1), pos, self.font, 0.2,
                                    (0, 0, 255), 1, cv2.LINE_AA)

            cv2.imshow('webcam', img)
            if cv2.waitKey(1) == 27:
                break  # esc to quit
        cv2.destroyAllWindows()


def main():
    '''main function'''
    capface = Foo()
    capface.action()

if __name__ == '__main__':
    main()
