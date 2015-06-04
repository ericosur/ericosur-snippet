#!/bin/sh

g++ -o CVCap -O3 \
    `pkg-config --cflags --libs opencv` \
    Source.cpp
