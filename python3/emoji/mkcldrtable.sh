#!/bin/bash

LOCALPATH=/home/rasmus/Dropbox/unicode/cldr/37
CLDRFILE=cldr-common-37.0.zip
ENXML=en.xml

# check local cldr file
if [ -e "$LOCALPATH/$CLDRFILE" ] ; then
    echo "local cldr file exists..."
    CLDRFILE=$LOCALPATH/$CLDRFILE
else
    echo "fetch cldr file from unicode.org..."
    curl -O http://unicode.org/Public/cldr/37/$CLDRFILE
fi

if [ -e "$CLDRFILE" ] ; then
    unzip -j $CLDRFILE common/annotations/en.xml
    echo "annotations/en.xml extracted..."
    mv en.xml en-basic.xml
    unzip -j $CLDRFILE common/annotationsDerived/en.xml
    echo "annotationsDerived/en.xml extracted..."
    mv en.xml en-derived.xml
else
    echo "failed to download $CLDRFILE"
    exit 1
fi

python3.6 read_enxml.py
