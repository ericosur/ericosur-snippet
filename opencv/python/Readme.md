# opencv using python

practice for python / opencv

depends on:
opencv-python
numpy
scikit-image
dlib

--

[TOC]

--

## notes

* how to know outdated python modules by pip?
  refer from: https://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip

```
pip list --outdated --format=freeze
```

* most python scripts here could run by python3, if not, it will croak while running

## how to install

for pip2
```
sudo -H pip2 install -U opencv-python
```

> For raspberry pi, there is no python2 opencv module

for pip3
```
sudo -H pip3 install -U opencv-python
```

## sample worthy to refer

[python cv2 module](https://www.programcreek.com/python/index/2663/cv2)


## some tips

At python script, may use
```python
import cv2 as cv
```
Then refer to openCV functons by using
```
cv.imshow('image', img)
cv.waitKey()
```
Just like namespace 'cv' as C++.


## setting.json

configure setting.json for input image path/filenames

### split.py

it will split input image into three BGR channels, perform calculation, and
output to file

## vcap.py

script uses video capture, and two actions:
  * one performs BGR2GRAY,
  * the other performs minus 128 (all channels?)

## fooface.py

dlib example for:
    * face detection
    * face landmarks

Need predictor data file to make predictor work. It could be downloaded from:
http://dlib.net/face_landmark_detection.py.html

