# use source to export...

TOP=$HOME/src/github/rpi-git/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian
export TARGETMACH=arm-linux-gnueabihf
export CC=$TOP/bin/arm-linux-gnueabihf-gcc
export CXX=$TOP/bin/arm-linux-gnueabihf-g++
export LD=$TOP/bin/arm-linux-gnueabihf-ld
export CFLAGS=-I$TOP/arm-linux-gnueabihf/include
export LDFLAGS=-L$TOP/arm-linux-gnueabihf/lib
export PATH=$TOP/bin:$PATH

