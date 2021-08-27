#!/usr/bin/python3
# coding: utf-8

'''
randomly pick one hash algorithm and apply to a text
'''

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

def get_hash(data: bytes, hash_name: str) -> str:
    ''' get digest hash '''
    if not hash_name in hashlib.algorithms_guaranteed:
        raise ValueError('algorithm ({}) is not in guaranteed list'.format(hash_name))

    m = hashlib.new(hash_name)
    m.update(data)
    return m.hexdigest()

def main():
    ''' main '''
    MSG = 'hello world'.encode('UTF-8')
    # will throw an exception here
    #get_hash(MSG, 'NO_ALGORITHM')

    import random
    a = random.choice(list(hashlib.algorithms_guaranteed))
    print(a)
    h = get_hash(MSG, a)
    print(h)

if __name__ == '__main__':
    print(__doc__)
    main()
