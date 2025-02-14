#!/usr/bin/env python3
# coding: utf-8

'''
AES encrypt / decrypt sample

https://www.pycryptodome.org/src/examples

install module Crypto by:
pip install pycryptodome
'''

import argparse
import sys
from typing import Any
try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
except ImportError:
    print('need install pycryptodome')
    sys.exit(1)
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

prt = rprint if USE_RICH else print

class Main():
    ''' main '''
    CIPHER_FILE = "chataes_demo.bin"
    KEY_SIZE = 32  # must be 16, 24 or 32 for AES
    IV_SIZE = 16   # must be 16 for AES
    TAG_SIZE = 16

    def __init__(self, debug: bool):
        self.logd = logger.debug if debug and USE_LOGGER else do_nothing

    def aes_encrypt(self, data: bytes, key: bytes, iv: bytes) -> bytes:
        ''' aes encrypt '''
        logd = self.logd
        if isinstance(data, str):
            logger.warning("data is str, will convert to bytes...")
            data = data.encode()
        cipher = AES.new(key, AES.MODE_EAX, iv)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        logd(f'len of tag: {len(tag)}')
        assert len(tag) == Main.TAG_SIZE
        # note: still need to save the nonce (IV) for later decryption
        fn = Main.CIPHER_FILE
        with open(fn, "wb") as file_out:
            _ = [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
        logd(f"output cipher to: {fn}")
        return ciphertext

    def aes_decrypt(self, key: bytes) -> bytes:
        ''' aes decrypt '''
        fn = Main.CIPHER_FILE
        logd = self.logd
        with open(fn, "rb") as file_in:
            nonce, tag, ciphertext = [ file_in.read(x) for x in (Main.IV_SIZE, Main.TAG_SIZE, -1) ]
        logd(f"read cipher from: {fn}")

        # let's assume that the key is somehow available again
        # note: the nonce (IV) is required for decryption
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        logd(f'data: {data!r}')
        return data

    def run_test(self):
        ''' run a test to encrypt a piece of text and decrypt it '''
        logd = self.logd
        plaintext = b"hello world"
        key = get_random_bytes(Main.KEY_SIZE)
        iv = get_random_bytes(Main.IV_SIZE)
        encrypted_text = self.aes_encrypt(plaintext, key, iv)
        logd(f'encrypted text:\n{encrypted_text!r}')
        decrypted_text = self.aes_decrypt(key)
        logd(f"decrypted text:\n{decrypted_text!r}")
        assert plaintext == decrypted_text
        prt("pass")

    @classmethod
    def run(cls) -> None:
        ''' run '''
        parser = do_parser()
        args = parser.parse_args()
        obj = cls(args.debug)
        obj.run_test()

def do_parser() -> Any:
    ''' make parser '''
    parser = argparse.ArgumentParser(description='chataes demo encrypt/decrypt')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("-d", "--debug", dest='debug', action='store_true',
        default=False, help='debug mode')
    return parser

if __name__ == '__main__':
    Main.run()
