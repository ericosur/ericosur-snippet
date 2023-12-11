#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from random import randint

from sta_prompt import has_console, prompt_alert, prompt_input

from kid_rsa import decrypt, encrypt, make_pair


def test():
    ''' test '''
    n, e, d, M = make_pair(a=9, b=11, a1=5, b1=8)
    assert M==98
    assert e==499
    assert d==795
    assert n==4048

    print(f'public (n, e): ({n}, {e})')
    print(f'private (d): {d}')
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
    assert cipher==1294
    print('cipher:', cipher)

    plain = decrypt(cipher, n, d)
    assert plain == P
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
    n, e, d, _ = make_pair(a, b, a1, b1)
    print(f'public (n, e): ({n}, {e})')
    print(f'private (d): {d}')
    P = randint(101, 999)
    assert 0 < P < n
    C = encrypt(P, n, e)
    plain = decrypt(C, n, d)
    assert P == plain

def run_in_pythonista():
    ''' run this at pythonista '''

    a = prompt_input('input a')
    b = prompt_input('input b')
    a1 = prompt_input('input a1')
    b1 = prompt_input('input b1')

    n, e, d, _ = make_pair(a, b, a1, b1)
    pub_msg = f'Your public key: (n, e): ({n}, {e})\n'
    pri_msg = f'Your private key: (d): {d}'
    msg = pub_msg + pri_msg
    prompt_alert(msg)

def main():
    ''' main '''
    #test()
    proceed()

if __name__ == '__main__':
    if has_console():
        run_in_pythonista()
    else:
        main()
