#!/bin/bash

SIZE=536870912
#INPATH=out/host/linux-x86/cts
INPATH=/src2/chagall-ics/out/target/product/chagall/custom-GEN_wifi
OUTPATH=./mnt

out/host/linux-x86/bin/make_ext4fs -l $SIZE -a custom $OUTPATH/fuck.img $INPATH

./mk_gext -l $SIZE -a custom $OUTPATH/shit.img $INPATH

