# HOWTO cross compile mediainfo for raspberry pi

source for mediainfo:
https://mediaarea.net/download/binary/mediainfo/18.05/MediaInfo_CLI_18.05_GNU_FromSource.tar.bz2

toolchain for raspberry pi:
https://github.com/raspberrypi/tools.git

first build libz for arm

July 4, 2017 updated steps:

* untar source tarball
```bash
cd ~/Downloads/
tar xfvj MediaInfo_CLI_18.05_GNU_FromSource.tar.bz2
cd MediaInfo_CLI_GNU_FromSource/
export TOP=$PWD
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
cd $TOP
./build-all.sh
```
  -*- or -*-

```
cd $TOP
./linaro.sh
```


* check built binary is ARM executable

```
file MediaInfo/Project/GNU/CLI/mediainfo
arm-linux-gnueabi-strip -o mediainfo.arm.strip MediaInfo/Project/GNU/CLI/mediainfo

$HOME/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-strip \
    -o mediainfo.arm.strip MediaInfo/Project/GNU/CLI/mediainfo
```

--------------------------------------------------------------
