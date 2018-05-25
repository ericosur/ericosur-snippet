#!/bin/bash

# setup environment and run CLI_Compile.sh

# using linaro gcc i686 for arm cross compiler
TOP=$HOME/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf
CC=$TOP/bin/arm-linux-gnueabihf-gcc
CXX=$TOP/bin/arm-linux-gnueabihf-g++
LD=$TOP/bin/arm-linux-gnueabihf-ld
CFLAGS=-I$TOP/arm-linux-gnueabihf/include
LDFLAGS=-L$TOP/arm-linux-gnueabihf/lib
PATH=$TOP/bin:$PATH

./CLI_Compile.sh --host=arm-linux-gnueabihf \
  --prefix=$TOP
