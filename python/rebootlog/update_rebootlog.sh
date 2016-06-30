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

AUTHPATH=$TOP/Private/auth.json
KEYPATH=$TOP/Private/spreadsheet_key

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
echo $PWD
echo "update_worksheet.py -a $AUTHPATH -k $KEYPATH"
./update_worksheet.py --auth=$AUTHPATH --key=$KEYPATH

DATE=`date -R`
echo -e "$DATE\trebootlog updated..."

