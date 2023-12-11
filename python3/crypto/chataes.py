#!/usr/bin/env python3
# coding: utf-8

'''
AES encrypt / decrypt sample

https://www.pycryptodome.org/src/examples

install module Crypto by:
pip install pycryptodome
'''

import sys

try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
except ImportError:
    print('need install pycryptodome')
    sys.exit(1)

def aes_encrypt(data, key):
    ''' aes encrypt '''
    data = b'secret data'
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open("encrypted.bin", "wb") as file_out:
        _ = [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

    return ciphertext


def aes_decrypt(key):
    ''' aes decrypt '''
    with open("encrypted.bin", "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

def main():
    ''' main '''
    # Example usage
    plaintext = b"hello world"
    key = get_random_bytes(16)
    ciphertext = aes_encrypt(plaintext, key)
    print(ciphertext)  # prints the encrypted ciphertext

    decrypted_plaintext = aes_decrypt(key)
    print(decrypted_plaintext)  # prints b"hello world"

if __name__ == '__main__':
    main()
