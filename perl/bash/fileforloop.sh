#!/bin/bash

for ff in ./*JPG
do
#    MYCMD="mogrify -resize 50% ${ff}"
#    echo ${MYCMD}
#    ${MYCMD}
    LCFF=`echo ${ff} | sed 's/JPG/jpg/'`
    echo ${LCFF}
    mv ${ff} ${LCFF}
done
