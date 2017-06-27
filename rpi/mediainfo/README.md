HOWTO cross compile mediainfo for raspberry pi
==============================================

source for mediainfo:
https://mediaarea.net/download/binary/mediainfo/0.7.92.1/MediaInfo_CLI_0.7.92.1_GNU_FromSource.tar.bz2

toolchain for raspberry pi:
https://github.com/raspberrypi/tools.git

first build libz for arm

myenv.sh
a.sh

--------------------------------------------------------------------

0. source myenv.sh
1. run ./a.sh for first time and will download zlib and build fail

----- build zlib for target -----
1. cd $TOP/Shared/Source/zlib
2. ./configure
3. make -j

----- rebuild mediainfo again -----
1. cd $TOP
2. run ./a.sh
