#!/bin/bash


adb_options=" "
if [ "$ANDROID_SERIAL" != "" ]; then
	echo $ANDROID_SERIAL
	adb_options="-s $ANDROID_SERIAL"
fi

echo $adb_options
#exit 1

#echo "copying 1920x1080"
adb $adb_options push bbb_short/1920x1080 /mnt/sdcard/test/bbb_short/1920x1080
adb $adb_options push bbb_full/1920x1080 /mnt/sdcard/test/bbb_full/1920x1080

echo "copying 1280x720"
adb $adb_options push bbb_short/1280x720 /mnt/sdcard/test/bbb_short/1280x720
adb $adb_options push bbb_full/1280x720 /mnt/sdcard/test/bbb_full/1280x720

echo "copying 720x480"
adb $adb_options push bbb_short/720x480 /mnt/sdcard/test/bbb_short/720x480
adb $adb_options push bbb_full/720x480 /mnt/sdcard/test/bbb_full/720x480

echo "copying all others"
adb $adb_options push bbb_short/176x144 /mnt/sdcard/test/bbb_short/176x144
adb $adb_options push bbb_full/176x144 /mnt/sdcard/test/bbb_full/176x144
adb $adb_options push bbb_short/480x360 /mnt/sdcard/test/bbb_short/480x360
adb $adb_options push bbb_full/480x360 /mnt/sdcard/test/bbb_full/480x360
