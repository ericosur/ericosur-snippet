#!/bin/bash

(>&2 echo -e "\nUse yql to query woeid by latitude/longtitude")

latitude=-15.763
longtitude=-47.870
result=woeid_result.json

#q='select * from geo.places where text="('${latitude}','$longtitude')"'
#echo $q
#exit 1

/usr/bin/curl https://query.yahooapis.com/v1/public/yql \
    -d q='select * from geo.places where text="('${latitude}','$longtitude')"' \
    -d 'format=json' 1> ${result} 2>/dev/null

(>&2 echo "output to ${result}")
(>&2 echo "lat: ${latitude}, lon: ${longtitude} ==> woeid:")
jq '.query.results.place.woeid' ${result}
