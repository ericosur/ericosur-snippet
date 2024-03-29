#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
list all sys.path

python will search for the modules and/or packages from
these paths

you may run it via python2 or python3 (or anaconda python)
to see the difference
'''

from __future__ import print_function

import sys

def main():
    ''' list each item of sys.path '''
    for idx, pp in enumerate(sys.path):
        print(f'[{idx:02d}]: {pp}')

if __name__ == '__main__':
    print(__doc__)
    main()
