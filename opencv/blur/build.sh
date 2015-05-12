#!/bin/sh

g++ -o Blur -O3 \
    `pkg-config --cflags --libs opencv` \
    cvcli/main.cpp
