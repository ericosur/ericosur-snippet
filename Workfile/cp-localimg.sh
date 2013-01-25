#!/bin/sh

TOP=$PWD
OUTDIR=img-arc-`date +%y%m%d`
PRODUCT=arcadia
SRC=out

cd $TOP
mkdir -p $OUTDIR
echo output to $OUTDIR
cd $OUTDIR

echo src dir: $TOP/$SRC/target/product/$PRODUCT/
find $TOP/$SRC/target/product/$PRODUCT/ -maxdepth 1 -name '*.zip' -prune -o -type f -name '*' -exec cp {} ./ \;
# find . -path './.svn' -prune -o -name '*txt' -print

cp $TOP/$SRC/host/linux-x86/bin/nvflash ./
#cp $TOP/dl-cpimg.sh ./

du
cd $TOP
