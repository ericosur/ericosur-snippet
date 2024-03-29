# HOWTO cross compile mediainfo for raspberry pi

## use docker

```
cd $TOP
docker pull docker pull dockcross/android-arm64
docker run --rm dockcross/android-arm64 > ./dockcross-arm64
./dockcross-arm64 bash

# in docker bash
$ make
```

```
CLI_compile.sh --host=x86_64-linux-gnu

cannot link -lpthread
```

before running,
```
export LD_LIBRARY_PATH=/data/data/com.termux/files/usr/lib
```

## toolchain

Several ways to get arm toolchains

* ubuntu package for ARM cross compiler:

```
sudo apt-get install \
  gcc-arm-linux-gnueabihf \
  g++-arm-linux-gnueabihf \
  cpp-arm-linux-gnueabihf \
  binutils-arm-linux-gnueabihf \
  pkg-config-arm-linux-gnueabihf

sudo apt-get install \
gcc-aarch64-linux-gnu \
g++-aarch64-linux-gnu \
cpp-aarch64-linux-gnu \
binutils-aarch64-linux-gnu \
pkg-config-aarch64-linux-gnu

```

* [toolchain for raspberry pi](https://github.com/raspberrypi/tools.git)

* [developer.arm.com](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
  * it's out of date?


## fetch CLI source tarball of MediaInfo:

updated on Aug 13, 2019:
```
$ cd ~/Downloads/
$ curl -O https://mediaarea.net/download/binary/mediainfo/19.07/MediaInfo_CLI_19.07_GNU_FromSource.tar.bz2
```

## first build libz for arm

July 4, 2017 updated steps:

* untar source tarball
```bash
cd ~/Downloads/
tar xfvj ~/Downloads/MediaInfo_CLI_19.04_GNU_FromSource.tar.bz2
cd MediaInfo_CLI_GNU_FromSource/
export WORKDIR=$PWD
```

* copy zlib source tree
```bash
mkdir -p Shared/Source/
cp -r ~/src/github/zlib/ Shared/Source/
```

* cp init scripts
```bash
cp ~/src/ericosur-snippet/rpi/mediainfo/rpi-tools/myenv.sh ./
cp ~/src/ericosur-snippet/rpi/mediainfo/rpi-tools/build-all.sh ./
```
  -*- or -*-
```bash
cp ~/src/ericosur-snippet/rpi/mediainfo/linaro/linaro-env.sh ./
cp ~/src/ericosur-snippet/rpi/mediainfo/linaro/linaro.sh ./
```


* build zlib first
```
source myenv.sh
cd Shared/Source/zlib
./configure
make -j
```

* build all others
```
cd $WORKDIR
./build-all.sh
```
  -*- or -*-

```
cd $WORKDIR
./linaro.sh
```


* check built binary is ARM executable

```
file MediaInfo/Project/GNU/CLI/mediainfo
arm-linux-gnueabi-strip -o mediainfo.arm.strip MediaInfo/Project/GNU/CLI/mediainfo

$HOME/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-strip \
    -o mediainfo.arm.strip MediaInfo/Project/GNU/CLI/mediainfo
```

path of strip
$HOME/src/github/rpi-git/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin/arm-linux-gnueabihf-strip


--------------------------------------------------------------
