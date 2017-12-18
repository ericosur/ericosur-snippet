#!/bin/bash

FILE=sample.json
OFILE=out.json

# degree C in one unicode code point
#CEL=$'\xe2\x84\x83'
#echo $CEL

echo "read from $FILE"

QPATH='["query"]["results"]["channel"]'
#jq '.["query"]["results"]["channel"]["description"]' ${FILE}
CITY=$(jq '.'$QPATH'["location"]["city"]' ${FILE})
TEXT=$(jq '.'$QPATH'["item"]["condition"]["text"]' ${FILE})
TEMP=$(jq '.'$QPATH'["item"]["condition"]["temp"]' ${FILE})
UNIT=$(jq '.'$QPATH'["units"]["temperature"]' ${FILE})

# remove "" using sed
T1=$(echo $TEMP|sed 's/\"//g')
U1=$(echo $UNIT|sed 's/\"//g')

# will be "17°C"
DEGREE=$'\x22'$T1$'\xC2\xB0'$U1$'\x22'
echo $DEGREE

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

echo "output to $OFILE"
jq '.' $OFILE
