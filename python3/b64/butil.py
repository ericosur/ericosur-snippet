#!/usr/bin/env python3
#codeing:utf-8

'''
some common functions for int/bytes conversion
'''

import sys
from pathlib import Path

try:
    import numpy as np
except ImportError as e:
    print('failed to import module', e)
    sys.exit(1)


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent
    py3_dir = this_dir.parent
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(madlog_dir))

try:
    setup_local_paths()
    from madlog import get_logd, get_prt
except ImportError as e:
    print('failed to import module', e)
    sys.exit(1)

prt = get_prt()
logd = get_logd()


def fill_bytearray(size: int = 24) -> bytes:
    ''' fill byte array '''
    return np.random.bytes(size)

def int_to_bytes(x: int) -> bytes:
    ''' int to bytes '''
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    ''' int from bytes '''
    r = int.from_bytes(xbytes, byteorder='big')
    return r

def sep():
    ''' print sep '''
    print('-' * 60)
