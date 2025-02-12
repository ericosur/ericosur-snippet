#!/bin/bash

# demo hwo to remove \n from xxd -p output

SRC=tmp_$(date +%s).bin
echo "----- prepare test data..."
dd if=/dev/urandom of=$SRC bs=16 count=4

echo -ne "----- use 'xxd -p' you will get newlines =====>\n"
echo -ne "----- and it is NG to store the content into variable...\n"
xxd -p $SRC

echo -ne "----- you need remove the newline =====>\n"
VAL=$(xxd -p $SRC | sed ':a;N;$!ba;s/\n//g')
echo $VAL

rm $SRC

