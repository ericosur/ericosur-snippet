#!/usr/bin/env python3
# coding: utf-8

'''
scrypt demo
hashlib.scrypt
'''

import base64
import os
import hashlib
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False

MODULE="scrypt_demo"

logd = logger.debug if USE_LOGGER else print

class ScryptDemo():
    ''' demo scrypt '''

    PASSWORD = "A123456789"

    def __init__(self):
        self.a_dict = {}

    @classmethod
    def run(cls) -> None:
        ''' run '''
        obj = cls()
        obj.action()

    def run_scrypt(self, pwd: str) -> None:
        ''' call hashlib.scrypt '''
        salt = os.urandom(24)  # bytes
        dk = hashlib.scrypt(password=pwd.encode(), salt=salt,
                            n=16384, r=8, p=1, dklen=48)
        hx = dk.hex()
        bs = bytes.fromhex(hx)
        assert bs==dk
        self.a_dict["salt"] = base64.b64encode(salt)
        self.a_dict["dk"] = base64.b64encode(dk)

    def report(self) -> None:
        ''' report '''
        print(self.a_dict)

    def action(self) -> None:
        ''' action '''
        self.run_scrypt(self.PASSWORD)
        self.report()
        #self.retrieve()

if __name__ == '__main__':
    ScryptDemo.run()
