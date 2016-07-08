#!/bin/bash

TOP=/home/pi/record-temperature
AUTHPATH=$HOME/Private/auth.json
KEYPATH=$HOME/Private/spreadsheet_key

TIMESTAMP=`date +"%Y-%m-%d %H:%M:%S"`
echo $TIMESTAMP

ping -c 3 8.8.8.8 >> /dev/null
rc=$?
if [[ $rc != 0 ]]; then
    echo "ping nok"
    exit 1
fi

cd $TOP
echo "call convLogCsv.pl: convert log to csv"
cat $TOP/data.log | ./convLogCsv.pl > $TOP/d.csv

source $HOME/my_env/bin/activate

cd $TOP
echo "call uploadCsv.py --auth=$AUTHPATH --key=$KEYPATH --file=$TOP/d.csv"
./uploadCsv.py --auth=$AUTHPATH --key=$KEYPATH --file=$TOP/d.csv


