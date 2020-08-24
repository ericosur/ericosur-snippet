#!/bin/bash
#
# encrypt $ifn to $ofn and send it out via gmail
#

# load passphrase
jsonf=$HOME/Private/mktable_ggmail.json
if [ -e $jsonf ]; then
    pass=$(jq '.passphrase' ${jsonf})
else
    echo 'sendit.sh: cannot load passphrase'
    exit 1
fi

#echo $pass
#exit 2

ifn=smallprimes.xlsx
ofn=sp.gpg

rm -f $ofn

if [ -e $ifn ]; then

    echo "encrypting..."
    gpg2 -a -c --batch --yes --passphrase $pass -o $ofn $ifn && \
    echo "sending..."  && \
    python3 ggmail.py

else

    echo "error: $ifn not found"

fi

# use gpg2 -d --batch --passphrase 651108 -o $ofn $ifn
