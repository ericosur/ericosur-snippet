#!/bin/bash

TOP=/home/pi/record-temperature
LOG=$TOP/data.log

TIMESTAMP=`date +"%m%d %H%M%S,%s,"`
echo $TIMESTAMP >> $LOG
python $TOP/AdafruitDHT.py 11 18  >> $LOG

#$TOP/callUpload.sh

