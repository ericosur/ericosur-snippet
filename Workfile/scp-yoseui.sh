#!/bin/bash

DATESTR=`date +%Y-%m-%d`
TIMESTR=`date +%H:%M:%S`
sed "s/PLEASEREPLACEME/date \"${DATESTR} ${TIMESTR}\"/" input.txt  > /tmp/o.sh

