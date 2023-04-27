#!/usr/bin/env python3
# coding: utf-8

'''
hash sample

https://www.pycryptodome.org/src/examples

install module Crypto by:
pip install pycryptodome
'''

import sys
try:
    from Crypto.Hash import SHA512
    from Crypto.Random import get_random_bytes
except ImportError:
    print('need install pycryptodome')
    sys.exit(1)

def test():
    ''' test '''
    hash_object = SHA512.new()
    repeat = 16
    for _ in range(repeat):
        chunk = get_random_bytes(128)
        hash_object.update(chunk)
    #print(hash_object.digest())

    print('name:', SHA512.__name__)
    print(f'digest_size (bytes):', hash_object.digest_size)
    print('hash:', hash_object.hexdigest())


def main():
    ''' main '''
    test()

if __name__ == '__main__':
    main()
