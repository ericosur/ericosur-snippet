#!/bin/bash


#1>all.json 2>/dev/null
echo -e "\nUse yql to query woeid by latitude/longtitude"


/usr/bin/curl https://query.yahooapis.com/v1/public/yql \
    -d q='select * from geo.places where text="(-15.763,-47.870)"' \
    -d 'format=json'

