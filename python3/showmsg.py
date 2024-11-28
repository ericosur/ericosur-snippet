#!/usr/bin/env python3
# coding: utf-8


'''
This script output one line to stdout, the other line to stderr

may test in shell to redirect stdout/stderr output

$ ./showmsg.py 2>&1 | tee file.txt

'''

import sys

print('hello stdout', file=sys.stdout)
print('hello stderr', file=sys.stderr)
