# blend

Simple example to blend "LinuxLogo.jpg" and "WindowsLogo.jpg" into one image.

## note

Use cmake and "CMakeLists.txt".

## old build.sh
```
#!/bin/sh

g++ -o Blend -O3 \
    `pkg-config --cflags --libs opencv` \
    blend.cpp
```
