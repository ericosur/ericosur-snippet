# opencv using python

practice for python / opencv
using module cv2

[TOC]

## sample worthy to refer

[python cv2 module](https://www.programcreek.com/python/index/2663/cv2)

## notes

how to know outdated python modules by pip?

refer from: https://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip

```
pip list --outdated --format=freeze
```


## setting

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

