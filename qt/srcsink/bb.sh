#!/bin/bash
#

TOP=/src/snippet/qt/srcsink


# build lib...
cd $TOP/mylib/
mkdir -p b/
cd b/
qmake ..
make -j
make install

# build executable
cd $TOP/
mkdir -p b/
cd b/
qmake ..
make -j
make install

echo "executables are put at $TOP/out/"
