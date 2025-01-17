#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions
	md5sum, sha256sum, sha1sum

    - md5sum: ```openssl dgst -md5 a.txt```
    - sha256sum: ```openssl dgst -sha256 a.txt```

    - list all supported digests: ```openssl dgst -list```
'''

__VERSION__ = '2024.03.28'

import os
import hashlib

def hash_factory(fn: str, hash_func) -> str:
    ''' hash factory '''
    if not os.path.isfile(fn):
        return ""
    BUFSIZE = 65536
    dgst = hash_func()
    with open(fn, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break
            dgst.update(data)
    return dgst.hexdigest()

def md5sum(fn: str):
    ''' get md5sum from a file, return string of md5sum '''
    return hash_factory(fn, hashlib.md5)

def sha1sum(fn: str):
    ''' get sha1 from a file, return string of sha1sum '''
    return hash_factory(fn, hashlib.sha1)

def sha256sum(fn: str):
    ''' get sha256 from a file, return string of sha256sum '''
    return hash_factory(fn, hashlib.sha256)

def sha384sum(fn: str):
    ''' sha384 '''
    return hash_factory(fn, hashlib.sha384)

def sha512sum(fn: str):
    ''' sha384 '''
    return hash_factory(fn, hashlib.sha512)

def sha3_256sum(fn: str):
    ''' vs openssl dgst -sha3-256 '''
    return hash_factory(fn, hashlib.sha3_256)

def sha3_512sum(fn: str):
    ''' vs openssl dgst -sha3-512 '''
    return hash_factory(fn, hashlib.sha3_512)
