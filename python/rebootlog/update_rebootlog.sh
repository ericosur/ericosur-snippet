#!/bin/bash

if [ "$HOSTNAME" == "x220" ] ; then
	echo "machine x220"
	TOP=/home/ericosur
	SRC=$TOP/rebootlog
fi
if [ "$HOSTNAME" == "rpi3" ] ; then
    echo "machine rpi3"
	TOP=/home/pi
	SRC=$TOP/rebootlog
fi

ping -c 3 8.8.8.8 >> /dev/null
rc=$?
if [[ $rc != 0 ]]; then
    echo "ping nok"
    exit 1
fi

cd $TOP
source my_env/bin/activate

DATE=`date -R`
echo -e "$DATE\tcalling rebootlog..."
cd $SRC
python update_worksheet.py

DATE=`date -R`
echo -e "$DATE\trebootlog updated..."

