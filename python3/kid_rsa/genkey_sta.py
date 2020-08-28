#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from kid_rsa import make_pair
from sta_prompt import prompt_input, prompt_alert, has_console

def run_this():
    ''' run this at pythonista '''
    a = prompt_input('input a')
    b = prompt_input('input b')
    a1 = prompt_input('input a1')
    b1 = prompt_input('input b1')

    n, e, d, _ = make_pair(a, b, a1, b1)
    pub_msg = 'Your public key: (n, e): ({}, {})\n'.format(n, e)
    pri_msg = 'Your private key: (d): {}'.format(d)
    msg = pub_msg + pri_msg
    prompt_alert(msg)

if __name__ == '__main__':
    if has_console():
        run_this()
    else:
        print('This script is designed to run in pythonista')
