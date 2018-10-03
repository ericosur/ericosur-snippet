#!/bin/bash

# will list file count for each folder (one level down only)

for D in *
do
    if [ -d $D ] ; then
        echo "folder $D:"
        find $D -type f | wc -l
    fi
done
