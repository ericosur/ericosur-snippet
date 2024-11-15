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

CIPHER_FILE = "encrypted.bin"

def logd(*args, **wargs):
    ''' log debug '''
    print("chataes.py:", *args, **wargs, file=sys.stderr)

def aes_encrypt(data: bytes, key: bytes) -> bytes:
    ''' aes encrypt '''
    data = bytes(data)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(CIPHER_FILE, "wb") as file_out:
        _ = [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    logd("output cipher to:", CIPHER_FILE)
    return ciphertext

def aes_decrypt(key: bytes) -> bytes:
    ''' aes decrypt '''
    with open(CIPHER_FILE, "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    logd("read cipher from:", CIPHER_FILE)

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    logd(f'data: {data}')
    return data

def main():
    ''' main '''
    # Example usage
    plaintext = b"hello world"
    key = get_random_bytes(16)
    ciphertext = aes_encrypt(plaintext, key)
    logd(f"ciphertext:\n{ciphertext}")

    decrypted_plaintext = aes_decrypt(key)
    logd(f"decrypted text:\n{decrypted_plaintext}")

if __name__ == '__main__':
    main()
