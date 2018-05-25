TOP=$HOME/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf
export TARGETMACH=arm-linux-gnueabihf
export CC=$TOP/bin/arm-linux-gnueabihf-gcc
export CXX=$TOP/bin/arm-linux-gnueabihf-g++
export LD=$TOP/bin/arm-linux-gnueabihf-ld
export CFLAGS=-I$TOP/arm-linux-gnueabihf/include
export LDFLAGS=-L$TOP/arm-linux-gnueabihf/lib
export PATH=$TOP/bin:$PATH

