#!/bin/bash

TOP=$PWD
src_dir=$HOME/src/
cldr_dir=$src_dir/github/cldr
PY=python3

function die() {
  local message="$1"
  echo "ERROR: $message" >&2
  exit 1
}

if [ -d $cldr_dir ] ; then
  echo "ok got: $cldr_dir"
else
	echo "$cldr_dir not exist, exit..."
	exit 1
fi

annot_dir=common/annotations
cp $cldr_dir/$annot_dir/en.xml        $TOP/en-basic.xml || die "not ok"
cp $cldr_dir/$annot_dir/zh_Hant.xml   $TOP/zh-basic.xml || die "not ok"
annot_dir=common/annotationsDerived
cp $cldr_dir/$annot_dir/en.xml        $TOP/en-derived.xml || die "not ok"
cp $cldr_dir/$annot_dir/zh_Hant.xml   $TOP/zh-derived.xml || die "not ok"

echo parsing xml, composing table and output
# generate csv
${PY} read_enxml.py
# generate py
${PY} parse_enxml.py
