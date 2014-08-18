#!/bin/bash
#
# due to OTA building script only takes images under PRODUCT_OUT dir
# so I need to copy images to PRODUCT_OUT and make patch.py to build
#
# this script could be run at
# 1. build_top / project root; it would take images under product_out 
#    to build ota package
# 2. the other sub-dir which stores generated images. eg:
#    gb/out_image/0.H3000.110523
#

# need change!
BUILD_TOP=/home/rasmus/gb-bsp
LOCAL_IMG_DIR=$PWD
OTA_VER=`cat ota-ver`

echo ota ver: $OTA_VER

cd $BUILD_TOP
echo current BUILD_TOP: $BUILD_TOP
source build/envsetup.sh
choosecombo 1 1 duke 2


#cd out/target/product/duke/
if [ "$LOCAL_IMG_DIR" != "$BUILD_TOP" ]; then
	echo "Not the same, perform copying..."
	/bin/cp -f $LOCAL_IMG_DIR/* $ANDROID_PRODUCT_OUT/
fi

echo local img dir: $LOCAL_IMG_DIR
echo product out: $ANDROID_PRODUCT_OUT
echo 
# note: this script cannot run under python 2.7
python $BUILD_TOP/device/pega/common/patch.py $OTA_VER y all

mv $BUILD_TOP/update.pkg $LOCAL_IMG_DIR/$OTA_VER.pkg
mv $BUILD_TOP/update.zip $LOCAL_IMG_DIR/$OTA_VER.zip

