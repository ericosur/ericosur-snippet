#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mypy: ignore-errors
# pylint: skip-file
#

'''
try to import _ctypes
'''

import sys

try:
    import _ctypes
except ImportError as err:
    print('Import Error:', err)

from basic_common import prt, get_logd

logd = get_logd(warn_msg="[warn] cannot import loguru", warn_printer=prt, use_loguru=True)

def test():
    ''' test '''
    logd('test')
    pass

if __name__ == "__main__":
    if len(sys.argv)>1 and sys.argv[1] == "test":
        test()
    else:
        prt(f'{sys.argv[0]} is a module, not a standalone script')
        sys.exit(1)
