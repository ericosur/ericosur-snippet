#!/bin/bash -x

# use nanocat send message to subscribers
# interval 1 second

# it's ipc:///tmp/pubsub.ipc
URL=/tmp/pubsub.ipc
DATE=`date`

# start client (subscriber)
./pubsub client ipc://${URL} client & client=$!

# publisher
nanocat --pub -X ${URL} -D "clock-${DATE}" -i 1 & server=$!

sleep 9
kill $client $server
