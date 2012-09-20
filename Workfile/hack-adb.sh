#!/bin/sh

PATH=out/target/product/avalon/system
FILE=build.prop


echo "persist.service.adb.enable=1" >> $PATH/$FILE
make_ext4fs -s -l 536870912 -a system system.img $PATH

