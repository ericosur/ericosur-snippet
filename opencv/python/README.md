# opencv using python

practice for python / opencv

recommended modules:

* opencv-contrib-python
* opencv-python
* numpy
* scikit-image
* dlib

--

[TOC]

--

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


## notes

### pip

* how to know outdated python modules by pip?
  refer from: https://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip

```
pip list --outdated --format=freeze
```

* most python scripts here could run by python3, if not, it will croak while running

#### how-to

First need to confirm the version of **pip** by using ```pip -V```, ```pip2 -V```,
or ```pip3 -V```

* install

```
pip install opencv-python opencv-contrib-python
```

* upgrade

```
pip install -U numpy
```


#### sample worthy to refer

[python cv2 module](https://www.programcreek.com/python/index/2663/cv2)


### CV tips

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
