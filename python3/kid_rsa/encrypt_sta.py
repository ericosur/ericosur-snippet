#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from kid_rsa import encrypt
from sta_prompt import prompt_input, prompt_alert, has_console

def run_this():
    ''' run this at pythonista '''
    p = prompt_input('input plaintext')
    n = prompt_input('input n')
    e = prompt_input('input e')

    plain_msg = 'plain text is: {}'.format(p)
    pub_msg = 'public key: (n, e): ({}, {})'.format(n, e)
    C = encrypt(p, n, e)
    cipher_msg = "cipher: {}".format(C)
    msg = plain_msg + '\n' + pub_msg + '\n' + cipher_msg
    prompt_alert(msg)

if __name__ == '__main__':
    if has_console():
        run_this()
    else:
        print('This script is designed to run in pythonista')
