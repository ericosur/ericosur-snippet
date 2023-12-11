#!/usr/bin/env python3
# coding: utf-8

'''
kid RSA
https://www.cs.uri.edu/cryptography/publickeykidkrypto.htm
'''

from sta_prompt import has_console, prompt_alert, prompt_input

from kid_rsa import encrypt


def run_this():
    ''' run this at pythonista '''
    p = prompt_input('input plaintext')
    n = prompt_input('input n')
    e = prompt_input('input e')

    plain_msg = f'plain text is: {p}'
    pub_msg = f'public key: (n, e): ({n}, {e})'
    C = encrypt(p, n, e)
    cipher_msg = f"cipher: {C}"
    msg = plain_msg + '\n' + pub_msg + '\n' + cipher_msg
    prompt_alert(msg)

if __name__ == '__main__':
    if has_console():
        run_this()
    else:
        print('This script is designed to run in pythonista')
