#!/bin/bash

app_name=qcore

while true
do
    pid=$(pidof ${app_name})
    time_stamp=$(date +%H:%M:%S)

    if [ "$pid" == "" ] ; then
        echo "[${time_stamp}] pidof ${app_name} not found"
    else
        thread_num=$(grep Thread /proc/${pid}/status)
        echo "[${time_stamp}][$app_name] pid ${pid} has ${thread_num}"
    fi
    sleep 1
done
