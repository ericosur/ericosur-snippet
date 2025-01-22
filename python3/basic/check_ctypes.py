#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mypy: ignore-errors
# pylint: skip-file
#

'''
try to import _ctypes
'''

try:
    import _ctypes
except ImportError as err:
    print('Import Error:', err)

#import os
#import re
import sys
try:
    from rich import print as pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = pprint if USE_RICH else print

def test():
    ''' test '''
    pass

if __name__ == "__main__":
    if len(sys.argv)>1 and sys.argv[1] == "test":
        test()
    else:
        prt(f'{sys.argv[0]} is a module, not a standalone script')
        sys.exit(1)
