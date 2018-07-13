#!/bin/bash

function remove_quote() {
    result=$(echo $1 | sed 's/\"//g')
}


function translate() {
    result=$(echo $1)
}

str=大中至正

echo "utf-8 to big5"
echo $str | iconv -f UTF-8 -t BIG5 |hexdump -C

str=商业银行
translate $str
echo "return: $result"
