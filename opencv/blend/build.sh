#!/bin/sh

g++ -o Blend -O3 \
    `pkg-config --cflags --libs opencv` \
    blend.cpp
