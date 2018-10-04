#!/bin/bash

if [ $(uname) == "Darwin" ] ; then
    DATE=gdate
else
    DATE=date
fi

# get epoch from date
testdate=$($DATE +%s)
echo "epoch: ${testdate}"

# convert epoch to local readable date/time string
# it may show date string to follow system locale settings
$DATE -d @${testdate}

# -R, --rfc-2822 output date and time in RFC 2822 format
$DATE -R -d @${testdate}
