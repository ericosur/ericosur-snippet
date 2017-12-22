#!/bin/bash

# using curl to ultilize google geocoding api to query POI

KEYFILE=$HOME/apikey/apikey.json
EMAIL=$(jq ".email" ${KEYFILE})
KEY=$(jq ".geocoding.apikey" ${KEYFILE})
#LAT=25.122772
#LOT=121.495869
CORD=${LAT},${LOT}
ADDR="台北101"

URL="https://plus.codes/api?address=${ADDR}&ekey=${KEY}&${EMAIL}"
echo $URL

/usr/bin/curl $URL
