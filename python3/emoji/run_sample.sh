#!/bin/bash
#
# this scripts reads sample.json by jq
# and demo how to process the return string in bash script
#
#

function die() {
    local message="$1"
    echo "ERROR: $message" >&2
    exit 1
}

function assertExist() {
    local fn="$1"
    if [ ! -e ${fn} ] ; then
        die "${fn} not found"
    fi
}

FILE=sample.json
CLI=/usr/bin/jq

assertExist ${FILE}
assertExist ${CLI}

echo "cat ${FILE}..."
cat ${FILE}

echo "${CLI} ${FILE}..."
${CLI} . ${FILE}
echo

# extract string and strip double quotes
ICONS=$(jq .sample ${FILE} | sed 's/\"//g')
echo "extracted string: ${ICONS}"
