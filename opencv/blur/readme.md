# blur

Simple example to "blur" deer.jpg.

## note

Here use qmake to build this sample ==> due to opencv version, LIBS not always good to work.

use cmake to build project

## setting.json
radius should be odd number
```
{
    "image": "../deer.jpg",
    "radius": 25
}
```

## old build.sh
```
#!/bin/sh

g++ -o Blur -O3 \
    `pkg-config --cflags opencv` \
    cvcli/main.cpp \
    `pkg-config --libs opencv` \
    -lstdc++
```

## sample qt project file
```
TEMPLATE = app

CONFIG += console
CONFIG += c++11
CONFIG -= app_bundle

# will not use any qt modules
CONFIG -= qt

TARGET = blur

SOURCES += main.cpp

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}

# just execute 'pkg-config --libs opencv'' and copy result for LIBS
LIBS += -lopencv_shape -lopencv_stitching -lopencv_objdetect -lopencv_superres -lopencv_videostab -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_video -lopencv_photo -lopencv_ml -lopencv_imgproc -lopencv_flann -lopencv_viz -lopencv_core
```
