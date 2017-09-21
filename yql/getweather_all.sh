#!/bin/bash
#

# use curl to make yql query to yahoo wather for
# all result and output to a file


# basic command:
# curl https://query.yahooapis.com/v1/public/yql \
#    -d q="select item.condition from weather.forecast where woeid=2487889" \
#    -d format=json

# current weather condition
function current_condition() {
    curl https://query.yahooapis.com/v1/public/yql \
       -d q="select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text='taipei')" \
       -d format=json

    # woeid in (select woeid from geo.places(1) where text="taipei")
}


function forecast {
    # forecast
    curl https://query.yahooapis.com/v1/public/yql \
       -d q="select item.forecast from weather.forecast where woeid in (select woeid from geo.places(1) where text='taipei')" \
       -d format=json
}

#
# parameter
# $1: output filename
#
function all {
    # forecast
    curl https://query.yahooapis.com/v1/public/yql \
       -d q="select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='Taipei') and u='c'" \
       -d format=json 1> $1.bak 2>/dev/null

    tidy_json $1.bak $1
    #select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="nome, ak")
}

#
# parameter
# $1: input file, will be deleted after running json.tool
# $2: output file
#
function tidy_json {
    python -m json.tool $1 > $2
    rm $1
}


# main flow here
OFILE=all.json
all $OFILE
echo "output to $OFILE"
