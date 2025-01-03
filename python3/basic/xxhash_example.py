#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
xxhash example

compare to xxh32sum:
xxh32sum <file>
'''

import xxhash  # type: ignore


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

def xxh32sum(fn):
    ''' xxhash 32 '''
    return hash_factory(fn, xxhash.xxh32)

def xxh64sum(fn):
    ''' xxhash 32 '''
    return hash_factory(fn, xxhash.xxh64)

def main():
    ''' main '''
    fn = 'dates.toml'
    dg = xxh32sum(fn)
    print(f'{dg}\t{fn}')
    dg = xxh64sum(fn)
    print(f'{dg}\t{fn}')

if __name__ == '__main__':
    main()
