#!/usr/bin/python

# get current path setting and split it
# then list them

import os

path = os.environ['PATH']
# or this way:
#    str = os.getenv('path')

for i in path.split(os.pathsep):
	print i

