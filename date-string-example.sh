#!/bin/bash

# get epoch from date
testdate=$(date +%s)
echo $testdate

# convert epoch to local readable date/time string
date -d @$testdate
