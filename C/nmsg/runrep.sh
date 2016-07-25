#!/bin/bash -x

DATE=`date`

./reqrep node0 ipc:///tmp/reqrep.ipc & node0=$! && sleep 1
./reqrep node1 ipc:///tmp/reqrep.ipc "$DATE"
kill $node0
