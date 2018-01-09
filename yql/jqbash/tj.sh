#!/bin/bash

input_file='input.json'

function remove_quote() {
    result=$(echo $1 | sed 's/\"//g')
}

function read_setting() {
    tmp=$(jq '.file.weather' ${input_file})
    remove_quote $tmp
    FILE=$result
    tmp=$(jq '.file.tjoutput' ${input_file})
    remove_quote $tmp
    OFILE=$result

    (>&2 echo "setting from: ${input_file}")
    (>&2 echo "read data from: ${FILE}")
    (>&2 echo "will output to: ${OFILE}")
}

function all() {
    (>&2 echo "read from $FILE")

    #jq '.["query"]["results"]["channel"]["description"]' ${FILE}
    CITY=$(jq '.query.results.channel.location.city' ${FILE})
    TEXT=$(jq '.query.results.channel.item.condition.text' ${FILE})
    TEMP=$(jq '.query.results.channel.item.condition.temp' ${FILE})
    UNIT=$(jq '.query.results.channel.units.temperature' ${FILE})

    # remove "" using sed
    T1=$(echo $TEMP|sed 's/\"//g')
    U1=$(echo $UNIT|sed 's/\"//g')

    # will be "17°C"
    DEGREE=$'\x22'$T1$'\xC2\xB0'$U1$'\x22'
    (>&2 echo $DEGREE)

    # output result...
    cat <<EOL > ${OFILE}
    {
        "weather": {
            "info": $CITY,
            "type": $TEXT,
            "temp": $DEGREE,
            "unit": $UNIT
        }
    }
EOL

    (>&2 echo "output to $OFILE")
    jq '.' $OFILE
}

# main starts here

read_setting
if [ -f ${FILE} ] ; then
    all
    (>&2 echo "ok")
else
    (>&2 echo "${FILE} not found, may run query_woeid.sh first")
    exit 100
fi

# degree C in one unicode code point
#CEL=$'\xe2\x84\x83'
#echo $CEL
