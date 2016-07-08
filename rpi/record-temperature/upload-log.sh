#!/bin/bash

UPLOADER=/home/pi/apps/Dropbox-Uploader/dropbox_uploader.sh
TOP=/home/pi/record-temperature
FNAME=$TOP/data.log
DEST=rpi/record-temperature/data.log

#echo $FNAME
$UPLOADER upload $FNAME $DEST

