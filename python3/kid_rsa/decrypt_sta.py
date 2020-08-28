#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from kid_rsa import decrypt
from sta_prompt import prompt_input, prompt_alert, has_console

def run_this():
    ''' run this at pythonista '''
    c = prompt_input('input cipherext')
    n = prompt_input('input n')
    d = prompt_input('input d')

    cipher_msg = 'cipher text is: {}'.format(c)
    priv_msg = 'private key: (n, d): ({}, {})'.format(n, d)
    p = decrypt(c, n, d)
    plain_msg = "plain: {}".format(p)
    msg = cipher_msg + '\n' + priv_msg + '\n' + plain_msg
    prompt_alert(msg)

if __name__ == '__main__':
    if has_console():
        run_this()
    else:
        print('This script is designed to run in pythonista')
