HOWTO cross compile mediainfo for raspberry pi
==============================================

source for mediainfo:
https://mediaarea.net/download/binary/mediainfo/0.7.97/MediaInfo_CLI_0.7.97_GNU_FromSource.tar.bz2

toolchain for raspberry pi:
https://github.com/raspberrypi/tools.git

first build libz for arm

July 4, 2017 updated steps:

* untar source tarball
```bash
cd ~/Downloads/
tar xfvj MediaInfo_CLI_0.7.97_GNU_FromSource.tar.bz2
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
cp ~/src/snippet/rpi/mediainfo/myenv.sh ./
cp ~/src/snippet/rpi/mediainfo/a.sh ./
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
./a.sh
```

--------------------------------------------------------------
