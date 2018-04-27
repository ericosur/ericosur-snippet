#!/bin/bash

# get epoch from date
testdate=$(date +%s)
echo "epoch: ${testdate}"

# convert epoch to local readable date/time string
# it may show date string to follow system locale settings
date -d @${testdate}

# -R, --rfc-2822 output date and time in RFC 2822 format
date -R -d @${testdate}
