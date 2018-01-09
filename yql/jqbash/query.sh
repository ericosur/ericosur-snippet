#!/bin/bash

input_file='input.json'

function remove_quote() {
    result=$(echo $1 | sed 's/\"//g')
}

function read_setting() {
    latitude=$(jq '.input.latitude' ${input_file})
    longtitude=$(jq '.input.longtitude' ${input_file})
    # output files

    tmp=$(jq '.file.woeid' ${input_file})
    remove_quote $tmp
    woeid_result=$result

    tmp=$(jq '.file.weather' ${input_file})
    remove_quote $tmp
    weather_result=$result

    (>&2 echo "setting from: ${input_file}")
    (>&2 echo "woeid data to: ${woeid_result}")
    (>&2 echo "weather output to: ${weather_result}")
    (>&2 echo "latitude: $latitude, longtitude: $longtitude")
}

function query() {
    #q='select * from geo.places where text="('${latitude}','$longtitude')"'
    #echo $q
    #exit 1

    (>&2 echo -e "Use curl+yql to query woeid by latitude/longtitude...")
    /usr/bin/curl https://query.yahooapis.com/v1/public/yql \
        -d q='select * from geo.places where text="('${latitude}','$longtitude')"' \
        -d 'format=json' 1> ${woeid_result} 2>/dev/null

    (>&2 echo "curl output to ${woeid_result}")

    tmp=$(jq '.query.results.place.locality1.content' ${woeid_result})
    (>&2 echo "locality1: ${tmp}")

    (>&2 echo "lat: ${latitude}, lon: ${longtitude} ==>")
    woeid=$(jq '.query.results.place.woeid' ${woeid_result})
    W1=$(echo $woeid | sed 's/\"//g')
    (>&2 echo "woeid: ${W1}")

    #  and u='c'
    #  item.condition
    /usr/bin/curl https://query.yahooapis.com/v1/public/yql \
       -d q="select * from weather.forecast where woeid=${W1} and u='c'" \
       -d 'format=json' 1> ${weather_result} 2> /dev/null
    (>&2 echo "curl output to ${weather_result}")
    jq '.query.results.channel.item.condition' ${weather_result}
}

# main starts here
read_setting
query
