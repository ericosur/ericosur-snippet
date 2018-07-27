#!/usr/bin/python

# get current path setting and split it
# then list them

# single line alias version:
# alias path='echo $PATH | sed "s/:/\n/g"'

import os

path = os.environ['PATH']
# or this way:
#    str = os.getenv('path')

for i in path.split(os.pathsep):
	print( i )

