#!/usr/bin/env python3

'''
handle key and iv
'''

import binascii
import os
import re
import sys

try:
    from Crypto.Random import get_random_bytes
except ImportError:
    print('warn: need install pycryptodome')
    print('info: use os.urandom instead')
    from os import urandom as get_random_bytes

try:
    from exchange_common import do_nothing, logd
except ImportError as e:
    print('failed to import module: ', e)
    sys.exit(1)


def from_file(fn: str) -> bytes:
    ''' load key from binary file '''
    with open(fn, 'rb') as fobj:
        data = fobj.read()
    return data

def save_bin(fn: str, data: bytes) -> None:
    ''' save binary to file '''
    with open(fn, 'wb') as fobj:
        fobj.write(data)


def from_env(name: str, size: int, debug=False) -> bytes:
    ''' get value from environment'''
    _logd = logd if debug else do_nothing

    def do_generate(size: int) -> bytes:
        _logd(f'generate new value for {name}')
        val = get_random_bytes(size)
        return val

    the_env = os.getenv(name)
    if the_env is None:
        _logd(f'env {name} is None')
        return do_generate(size)

    pattern = re.compile(r'^[A-Fa-f0-9]+$')
    if pattern.match(the_env):
        val = binascii.unhexlify(the_env)
        if len(val) == size: # ok
            return val
        # fall through
        _logd(f"size mismatch, expect {size}, got {len(val)}")

    return do_generate(size)

if __name__ == "__main__":
    print('keyiv.py is a module, not a standalone script')
