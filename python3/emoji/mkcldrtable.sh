#!/bin/bash

SCRIPT_DIR=$PWD
VER=42
LOCALPATH=/home/rasmus/Dropbox/unicode/cldr/${VER}
CLDRFILE=cldr-common-${VER}.0.zip
ENXML=en.xml

if [ -d ${LOCALPATH} ] ; then
    echo "local path exists - OK"
else
    echo "local path not exists - mkdir..."
    mkdir -p ${LOCALPATH}
fi

TOP=${LOCALPATH}
cd $TOP

# check local cldr file
if [ -e "$LOCALPATH/$CLDRFILE" ] ; then
    echo "local cldr file exists..."
    CLDRFILE=$LOCALPATH/$CLDRFILE
else
    echo "fetch cldr file from unicode.org..."
    curl -O http://unicode.org/Public/cldr/${VER}/${CLDRFILE}
fi

if [ -e "$CLDRFILE" ] ; then
    unzip -j $CLDRFILE common/annotations/en.xml
    echo "annotations/en.xml extracted..."
    mv en.xml $SCRIPT_DIR/en-basic.xml
    unzip -j $CLDRFILE common/annotationsDerived/en.xml
    echo "annotationsDerived/en.xml extracted..."
    mv en.xml $SCRIPT_DIR/en-derived.xml
else
    echo "failed to download $CLDRFILE"
    exit 1
fi

# stupid try and error on python version
#
# $1 is the name of executable like "python"
# may use another executable to check version
# result like:
# 27
# 35
# 36
function get_python_version() {
    result=$( $1 -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
    #echo "get_python_version: $result"
}


function try_this_python() {
    prog=$1
    get_python_version $prog

    # compare it as numbers
    if [ "$result" -ge "36" ] ; then
        #echo "OK: use $prog"
        result=$prog
    else
        #echo "FAIL: need python >= 3.6"
        result=
    fi
}

try_this_python python
if [ "$result" != "" ] ; then
    PY=$result
else
    try_this_python python3
    if [ "$result" != "" ] ; then
        PY=$result
    else
        try_this_python python3.6
        if [ "$result" != "" ] ; then
            PY=$result
        fi
    fi
fi

cd $SCRIPT_DIR
echo parsing xml, composing table and output
${PY} read_enxml.py
${PY} parse_enxml.py
