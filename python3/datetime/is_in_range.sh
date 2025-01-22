#!/bin/bash

start_date="2025-01-25 00:00:00"
end_date="2025-02-02 23:59:59"

start_timestamp=$(date -d "$start_date" +%s)
end_timestamp=$(date -d "$end_date" +%s)
current_timestamp=$(date +%s)

if [[ $current_timestamp -ge $start_timestamp &&  $current_timestamp -le $end_timestamp ]] ; then
    echo "in the range..."
else
    echo "out of the range..."
fi
