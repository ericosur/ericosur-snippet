#!/bin/bash -x

./pubsub client ipc:///tmp/pubsub.ipc client0 & client0=$!
#./pubsub server ipc:///tmp/pubsub.ipc & server=$! && sleep 1
#./pubsub server ipc:///tmp/pubsub.ipc & server=$!
./pubsub client ipc:///tmp/pubsub.ipc client1 & client1=$!
#./pubsub client ipc:///tmp/pubsub.ipc client2 & client2=$!
sleep 20
#kill $server $client0 $client1 $client2
kill $server $client0 $client1
