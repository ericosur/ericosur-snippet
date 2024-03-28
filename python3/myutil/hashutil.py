#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions
	md5sum, sha256sum, sha1sum
'''

__VERSION__ = '2024.03.28'

import hashlib

def hash_factory(fn, hash_func):
    ''' hash factory '''
    BUFSIZE = 65536
    dgst = hash_func()
    with open(fn, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break
            dgst.update(data)
    return dgst.hexdigest()

def md5sum(fn):
    ''' get md5sum from a file, return string of md5sum '''
    return hash_factory(fn, hashlib.md5)

def sha1sum(fn):
    ''' get sha1 from a file, return string of sha1sum '''
    return hash_factory(fn, hashlib.sha1)

def sha256sum(fn):
    ''' get sha256 from a file, return string of sha256sum '''
    return hash_factory(fn, hashlib.sha256)
