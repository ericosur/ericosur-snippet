#!/bin/bash

if [ "$HOSTNAME" == "x220" ] ; then
	echo "machine x220"
	TOP=/home/ericosur
	SRC=$TOP/Dropbox/src/rebootlog
fi
if [ "$HOSTNAME" == "rpi3" ] ; then
    echo "machine rpi3"
	TOP=/home/pi
	SRC=$TOP/rebootlog
fi

LOG=$TOP/gspread.txt

date >> $LOG

ping -c 3 8.8.8.8 > /dev/null
rc=$?
if [[ $rc != 0 ]]; then
    echo "ping nok" >> $LOG
    exit 1
fi

echo -e "\tcalling rebootlog..." >> $LOG

cd $TOP
source my_env/bin/activate

cd $SRC
python update_worksheet.py >> $LOG

date >> $LOG
echo -e "\trebootlog updated..." >> $LOG

