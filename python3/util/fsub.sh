#!/bin/bash
TOP=$PWD
SRC=../
LIST=$TOP/fsub_out.txt

cd $TOP/$SRC/
#find . -type d -not -path '*/\.*'
echo "start collecting sub directories..."
find . -type d -exec sh -c 'cd "$0" && echo "$(pwd) $(find . -type f | wc -l)"' {} \; > $LIST

WTF=$TOP/mkrep.py
echo "finish, then call $WTF ..."
python3 $WTF $LIST

# sudo date -s "2024-07-05 15:30:00"
# sudo hwclock --systohc
