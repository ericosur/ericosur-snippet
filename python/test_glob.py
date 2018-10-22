#!/usr/bin/env python3

'''
test glob
'''

import glob

files = glob.glob('s*.py')
for ff in files:
    print(ff)
