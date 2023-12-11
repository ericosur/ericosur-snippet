#!/usr/bin/python3
# coding: utf-8

'''
two samples to generate random string
'''

import binascii
import os
import re
import secrets


def show(s):
    ''' show '''
    print('input:', s)
    print('len:', len(s))
    print('type:', type(s))


def random_bytes(lens=15):
    ''' random bytes str [0-9a-f]'''
    r = binascii.b2a_hex(os.urandom(lens))
    return r

def get_random_str(lens=15):
    ''' get secret [a-zA-Z][0-9a-zA-Z] '''
    #r = secrets.token_hex(LENS)
    r = ''
    while len(r) < lens:
        r = secrets.token_urlsafe(lens*2)   # may contains _ or -
        r = re.sub(r'[-_]+', '', r)     # remove [-_]
        r = re.sub(r'^[0-9]+', '', r)   # remove leading digits 0-9
    return r[:lens]

def main():
    ''' main '''
    #random_bytes()
    for _ in range(10):
        s = get_random_str(10)
        print(s)

if __name__ == '__main__':
    main()
