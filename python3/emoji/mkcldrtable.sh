#!/bin/bash

LOCALPATH=/bs2/Dropbox/unicode/cldr/36.1/unicode.org/Public/cldr/36.1
CLDRFILE=cldr-common-36.1.zip
ENXML=en.xml

# check local cldr file
if [ -e "$LOCALPATH/$CLDRFILE" ] ; then
    echo "local cldr file exists..."
    CLDRFILE=$LOCALPATH/$CLDRFILE
else
    echo "fetch cldr file from unicode.org..."
    curl -O http://unicode.org/Public/cldr/36.1/$CLDRFILE
fi

if [ -e "$CLDRFILE" ] ; then
    unzip -j $CLDRFILE common/annotations/en.xml
    echo "en.xml extracted"
else
    echo "failed to download $CLDRFILE"
    exit 1
fi

if [ ! -e "$ENXML" ] ; then
    echo "$ENXML not found, fatal error..."
    exit 1
else
    echo "$ENXML already exists, will use it..."
fi


echo "calling cldr_xml2csv.pl ..."
perl cldr_xml2csv.pl

echo "calling cldr_insert_cp.py ..."
python3 cldr_insert_cp.py
