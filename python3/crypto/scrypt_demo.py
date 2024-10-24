#!/usr/bin/env python3
# coding: utf-8

'''
scrypt demo
hashlib.scrypt
'''

import base64
import os
import sys
import hashlib

MODULE="scrypt_demo"

def logd(*args, **wargs):
    ''' log debug '''
    print(MODULE, *args, **wargs, file=sys.stderr)

class ScryptDemo():
    ''' demo scrypt '''

    PASSWORD = "A123456789"
    def __init__(self):
        self.a_dict = {}

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

    def run_scrypt(self, pwd):
        ''' call hashlib.scrypt '''
        salt = os.urandom(24) # 16 bytes == 128 bits
        dk = hashlib.scrypt(password=pwd.encode(), salt=salt,
                            n=16384, r=8, p=1, dklen=48)
        hx = dk.hex()
        bs = bytes.fromhex(hx)
        assert bs==dk
        self.a_dict["salt"] = base64.b64encode(salt)
        self.a_dict["dk"] = base64.b64encode(dk)

    def report(self):
        ''' report '''
        print(self.a_dict)

    def action(self):
        ''' action '''
        self.run_scrypt(self.PASSWORD)
        self.report()
        self.retrieve()

def main():
    ''' main '''
    ScryptDemo.run()

if __name__ == '__main__':
    main()
