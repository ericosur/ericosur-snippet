#!/bin/bash

MY_DATE=`date +%m%d-%H%M`
MY_TAG=`cat ap-prev-tag`
MY_OUTFILE=hc-$MY_DATE-git.log

echo TAG: $MY_TAG
echo OUTPUT: $MY_OUTFILE

repo forall -p -c git log --pretty=oneline $MY_TAG..HEAD > $MY_OUTFILE


