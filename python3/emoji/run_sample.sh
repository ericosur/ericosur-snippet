#!/bin/bash

FILE=sample.json

TARGET=jq
which ${TARGET}
STATUS=$?


if [ -e ${FILE} ] ; then
    echo "cat ${FILE}..."
    cat ${FILE}

    if [ $STATUS -eq 0 ]; then
        echo "${TARGET} ${FILE}..."
        ${TARGET} . ${FILE}

        echo
        # extract string and strip double quotes
        ICONS=$(jq .sample ${FILE} | sed 's/\"//g')
        echo "extracted string: ${ICONS}"
    else
        echo "${TARGET} not found"
    fi
else
    echo "${FILE} not found"
fi
