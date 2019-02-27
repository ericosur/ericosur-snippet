#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
get current path setting and split it
then list them
'''

# single line alias version:
# alias path='echo $PATH | sed "s/:/\n/g"'

from __future__ import print_function
import os

PATH = os.environ['PATH']
# or this way:
#    str = os.getenv('path')

for i in PATH.split(os.pathsep):
    print(i)
