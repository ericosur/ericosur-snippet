#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
pp.py will list all sys.path
this script will search for modules from these path


you may run it via python2 or python3 (or anaconda python)
to see the difference
'''

from __future__ import print_function
import sys

# list each item of sys.path
for idx, pp in enumerate(sys.path):
    print('[{:02d}]: {}'.format(idx, pp))
