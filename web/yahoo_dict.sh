#!/bin/sh
curl -sd "p=$1" http://tw.dictionary.yahoo.com/search  | \
         awk "/pexplain/{ print } \
         /peng/{ print } \
         /pchi/{ print ; print \"\n\" }" | \
         sed -e :a -e 's/<[^>]*>//g;/</N;//ba'
