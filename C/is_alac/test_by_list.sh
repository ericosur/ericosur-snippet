#!/bin/bash

appname=isAlac
listfile='list.txt'

if [ -e ${appname} ] ; then
    echo -e "app not found: ${appname}\n"
    exit 1
fi

if [ -f ${listfile} ] ; then
    cat ${listfile} | \
    while read P; do
        #echo ${appname} "\"$P\""
        ${appname}  $P
    done
else
    echo -e "list file not found: ${listfile}\n"
    echo -e "please prepare it before running tests...\n"
    exit 2
fi
