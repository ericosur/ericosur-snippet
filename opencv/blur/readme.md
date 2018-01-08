# blur

Simple example to "blur" deer.jpg.

## note

Here use qmake to build this sample.

## old build.sh
```
#!/bin/sh

g++ -o Blur -O3 \
    `pkg-config --cflags opencv` \
    cvcli/main.cpp \
    `pkg-config --libs opencv` \
    -lstdc++
```
