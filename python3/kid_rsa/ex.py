#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from random import randint

# for pythonista
#import clipboard
HAS_CONSOLE_MODULE = False
try:
    import console
    HAS_CONSOLE_MODULE = True
except ImportError:
    print('No console module of pythonista')

from kid_rsa import *

def test():
    ''' test '''
    n, e, d, M = make_pair(a=9, b=11, a1=5, b1=8)
    assert(M==98)
    assert(e==499)
    assert(d==795)
    assert(n==4048)

    print('public (n, e): ({}, {})'.format(n, e))
    print('private (d): {}'.format(d))
    print('M:', M)
    print('=' * 40)

    '''
    Note:   The plaint text has to be a number in the range of
    0 to n-1. So for this system the plaintext or blocks of
    plaintext hast to converted into numbers in the range of
    0 to n-1.
    '''

    #P = randint(0, n - 1)
    P = 538
    print('selected P:', P)
    cipher = encrypt(P, n, e)
    assert(cipher==1294)
    print('cipher:', cipher)

    plain = decrypt(cipher, n, d)
    assert(plain == P)
    print('plaintext:', plain)

    if plain == P:
        print('ok')
    print('=' * 40)

def proceed():
    ''' proceed '''
    a = randint(2, 11)
    b = randint(13, 19)
    a1 = randint(11, 19)
    b1 = randint(20, 29)
    n, e, d, M = make_pair(a, b, a1, b1)
    print('public (n, e): ({}, {})'.format(n, e))
    print('private (d): {}'.format(d))
    P = 1
    assert(P<n and P>0)
    C = encrypt(P, n, e)
    plain = decrypt(C, n, d)
    assert(P == plain)

def run_this():
    ''' run this at pythonista '''
    def prompt_input(msg: str):
        ''' prompt '''
        ret = console.input_alert(msg)
        try:
            val = int(ret)
            if val <= 0:
                raise ValueError
        except ValueError:
            print('{} not a number'.format(ret))
            val = randint(1, 99)
            print('invalid number, use random number:', val)

    a = prompt_input('input a')
    b = prompt_input('input b')
    a1 = prompt_input('input a1')
    b1 = prompt_input('input b1')

    n, e, d, M = make_pair(a, b, a1, b1)
    pub_msg = 'Your public key: (n, e): ({}, {})\n'.format(n, e)
    pri_msg = 'Your private key: (d): {}'.format(d)
    msg = pub_msg + pri_msg
    if HAS_CONSOLE_MODULE:
        console.alert(msg)

def main():
    ''' main '''
    #test()
    proceed()

if __name__ == '__main__':
    if HAS_CONSOLE_MODULE:
        run_this()
    else:
        proceed()
