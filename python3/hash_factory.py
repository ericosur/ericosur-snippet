#!/usr/bin/env python3
# coding: utf-8

'''
randomly pick one hash algorithm and apply to a text
'''

import argparse
import hashlib
import random


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
        raise ValueError(f'algorithm ({hash_name}) is not in guaranteed list')

    m = hashlib.new(hash_name)
    m.update(data)
    return m.hexdigest()

def test():
    ''' main '''
    MSG = 'hello world'.encode('UTF-8')
    # will throw an exception here
    #get_hash(MSG, 'NO_ALGORITHM')

    a = random.choice(list(hashlib.algorithms_guaranteed))
    print(a)
    h = get_hash(MSG, a)
    print(h)

def list_algorithms():
    ''' list algorithms
        type of hashlib.algorithms_guaranteed is Set
    '''
    algos = list(hashlib.algorithms_guaranteed)
    algos.sort()
    for x in algos:
        print(x)

def init_argparse():
    ''' argparse '''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-l", "--list", action='store_true', help='list algorithms')
    args = parser.parse_args()

    if args.list:
        list_algorithms()
    else:
        test()

    # to show help message directly
    #parser.print_help()
    return parser

def main():
    ''' main '''
    init_argparse()

if __name__ == '__main__':
    main()
