#!/bin/sh

g++ -o Blur -O3 \
    `pkg-config --cflags opencv` \
    cvcli/main.cpp \
    `pkg-config --libs opencv` \
    -lstdc++

