#!/bin/bash

# setup environment and run CLI_Compile.sh

TOP=$HOME/src/github/rpi-git/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian
CC=$TOP/bin/arm-linux-gnueabihf-gcc
CXX=$TOP/bin/arm-linux-gnueabihf-g++
LD=$TOP/bin/arm-linux-gnueabihf-ld
CFLAGS=-I$TOP/arm-linux-gnueabihf/include
LDFLAGS=-L$TOP/arm-linux-gnueabihf/lib
PATH=$TOP/bin:$PATH

./CLI_Compile.sh --host=arm-linux-gnueabihf \
  --prefix=$TOP
