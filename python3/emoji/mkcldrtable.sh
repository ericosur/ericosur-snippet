#!/bin/bash

CLDRFILE=cldr-common-36.0.zip
ENXML=en.xml

if [ ! -e "$ENXML" ] ; then
    echo "$ENXML not found, try to download from web..."
    curl -O http://unicode.org/Public/cldr/36/$CLDRFILE
    if [ -e "$CLDRFILE" ] ; then
        unzip -c $CLDRFILE common/annotations/en.xml > $ENXML
        echo "en.xml extracted"
        rm $CLDRFILE
    else
        echo "failed to download $CLDRFILE"
        exit 1
    fi
fi

echo "calling cldr_xml2csv.pl ..."
perl cldr_xml2csv.pl

echo "calling cldr_insert_cp.py ..."
python3 cldr_insert_cp.py

