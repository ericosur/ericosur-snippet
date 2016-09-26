#!/bin/bash

BS=isAlac

#echo "Is ALAC?:"
cat lst.txt | \
while read P; do
    echo $BS "\"$P\""
done

