#!/bin/bash

# using curl to ultilize google geocoding api to
# query POI

KEYFILE=$HOME/apikey/apikey.json
#LAT=25.122772
#LOT=121.495869
CORD=${LAT},${LOT}
ADDR="台北101"
TMPOUTPUT=/tmp/pluscodes.json

# check if keyfile exists
if [ -e $KEYFILE ] ; then
    EMAIL=$(jq ".email" ${KEYFILE})
    KEY=$(jq ".geocoding.apikey" ${KEYFILE})
else
    echo "apikey not found: ${KEYFILE}"
    exit 1
fi

URL="https://plus.codes/api?address=${ADDR}&ekey=${KEY}&${EMAIL}"
echo $URL

/usr/bin/curl $URL 1> $TMPOUTPUT 2> /dev/null; RET=$?
if [ $RET -ne 0 ] ; then
    echo "curl unsuccessfully, ret: $RET"
else
    echo "query status:" $(jq ".status" $TMPOUTPUT)
    echo "output as file: $TMPOUTPUT"
fi
