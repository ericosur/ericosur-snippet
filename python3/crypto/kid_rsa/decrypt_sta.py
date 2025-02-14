#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from sta_prompt import has_console, prompt_alert, prompt_input

from kid_rsa import decrypt


def run_this():
    ''' run this at pythonista '''
    c = prompt_input('input cipherext')
    n = prompt_input('input n')
    d = prompt_input('input d')

    cipher_msg = f'cipher text is: {c}'
    priv_msg = f'private key: (n, d): ({n}, {d})'
    p = decrypt(c, n, d)
    plain_msg = f"plain: {p}"
    msg = cipher_msg + '\n' + priv_msg + '\n' + plain_msg
    prompt_alert(msg)

if __name__ == '__main__':
    if has_console():
        run_this()
    else:
        print('This script is designed to run in pythonista')
