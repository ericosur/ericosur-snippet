#!/usr/bin/env python3
# coding: utf-8

'''
handle key and iv
'''

import os
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
    val = os.getenv(name)
    if val:
        #val = base64.b64decode(val)
        val = binascii.unhexlify(val)
        if len(val) != size:
            logd(f"size mismatch, expect {size}, got {len(val)}")
        else:
            logd(f'get {name} from environment')
        return val
    val = get_random_bytes(size)
    return val
