#!/usr/bin/python

import sys
import os

'''
    practice for getting environment variables

    The way to get env var:
        os.environ.get('path')
    OR
        os.getenv('path')
'''

if len(sys.argv) == 1:
    print("usage: %s [arg1] [arg2]..." % sys.argv[0])
    quit()

for x in range(1, len(sys.argv)):
	if sys.argv[x]:
		en = os.environ.get(sys.argv[x])
	print(sys.argv[x],"=", en)
