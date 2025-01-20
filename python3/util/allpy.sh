#!/bin/bash

function die() {
  local message="$1"
  echo "ERROR: $message" >&2
  exit 1
}

OUT=list.txt

TOP=$PWD
SRC=$HOME/src/ericosur-snippet/python3

cd $SRC || die "folder not found"
echo "allpy.sh find..."
find -type f -name '*.py' > $TOP/$OUT
echo "allpy.sh run collect_import.py..."
python3 $TOP/collect_import.py $TOP/$OUT 2> /dev/null

