#!/bin/bash

MY_DATE=`date +%m%d%H%M`
MY_TAG=`cat ap-tag`
MY_OLD_TAG=`cat ap-prev-tag`
MY_OUTFILE=hc-$MY_DATE-git.log

echo OLDTAG: $MY_OLD_TAG
echo TAG: $MY_TAG
echo OUTPUT: $MY_OUTFILE

repo forall -p -c git log --pretty=oneline $MY_OLD_TAG..$MY_TAG > $MY_OUTFILE


