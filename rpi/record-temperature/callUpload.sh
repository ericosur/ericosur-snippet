#!/bin/bash

TOP=/home/pi/record-temperature
LOG=$TOP/data.log

TIMESTAMP=`date +"%m%d %H%M%S,%s,"`
#echo $TIMESTAMP >> $LOG

ping -c 3 8.8.8.8 >> /dev/null
rc=$?
if [[ $rc != 0 ]]; then
    echo "ping nok"
    exit 1
fi

echo "call upload-log.sh"
$TOP/upload-log.sh

