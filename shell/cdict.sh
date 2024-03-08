#!/bin/bash

# from: http://linuxtoy.org/archives/gdict.html

# Command line Google's dictionary
echo "----------------------------"
echo ' '$1 | /usr/bin/curl -s -A 'Mozilla/4.0' 'http://www.google.com.hk/dictionary?aq=f&langpair=en|zh-CN&q='$1'&hl=en' \
| html2text -ascii -nobs -style compact -width 1000 | sed -n -e '/^ /p'| sed '1,4d' | head -n -1
#EOF
