#!/usr/bin/env python3
# coding: utf-8

'''
handle key and iv
'''

import binascii
import os
import re
from Crypto.Random import get_random_bytes
from loguru import logger

logd = logger.debug

def from_file(fn: str) -> bytes:
    ''' load key from binary file '''
    with open(fn, 'rb') as fobj:
        data = fobj.read()
    #logd(f'data: {data}')
    return data

def save_bin(fn: str, data: bytes) -> None:
    ''' save binary to file '''
    with open(fn, 'wb') as fobj:
        fobj.write(data)
    #logd(f'save to: {fn}')

def from_env(name: str, size: int) -> bytes:
    ''' get value from environment'''
    def do_generate(size: int) -> bytes:
        logd(f'generate new value for {name}')
        val = get_random_bytes(size)
        return val

    the_env = os.getenv(name)
    if the_env is None:
        logd(f'env {name} is None')
        return do_generate(size)

    pattern = re.compile(r'^[A-Fa-f0-9]+$')
    if pattern.match(the_env):
        val = binascii.unhexlify(the_env)
        if len(val) == size:
            # ok
            return val
        # fall through
        logd(f"size mismatch, expect {size}, got {len(val)}")

    return do_generate(size)
