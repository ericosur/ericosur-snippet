#!/usr/bin/python3
# coding: utf-8
#

import sys

print('hello stdout', file=sys.stdout)
print('hello stderr', file=sys.stderr)


# ./showmsg.py 2>&1 | tee file.txt

