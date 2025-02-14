#!/usr/bin/env python3
# coding: utf-8

'''
hashlib.scrypt demo

Scrypt is a strong, memory-hard key derivation function that improves
security against brute-force attacks, particularly those using
specialized hardware. It is especially useful in password hashing.

It is not used for encryption or decryption.

'''

import argparse
from typing import Any
import base64
import json
import os
import sys
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False

MODULE = "scrypt_demo"
prt = rprint if USE_RICH else print

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None


try:
    from run_vector import do_scrypt, ScryptVector, run_test_vector
except ImportError:
    logger.error("The module 'run_vector' could not be found")
    sys.exit(1)

class ScryptDemo():
    ''' demo scrypt '''
    # if you change the password, you need to
    #   remove the json file
    #   re-run the script
    PASSWORD = "HereIsThePassword3"

    def __init__(self, debug=False, pure=False):
        self.the_dict = {}
        self.jsonfile = f'{MODULE}.json'
        self.logd = logger.debug if debug and USE_LOGGER else do_nothing
        if pure:
            self.pure_test()
        else:
            self.action()

    def pure_test(self) -> None:
        ''' pure test '''
        w = ScryptVector(P="", S="", N=16, r=1, p=1, dklen=64)
        run_test_vector(w)
        w = ScryptVector(P="password", S="NaCl", N=1024, r=8, p=16, dklen=64)
        run_test_vector(w)
        w = ScryptVector(P="pleaseletmein", S="SodiumChloride", N=16384, r=8, p=1, dklen=64)
        run_test_vector(w)
        w = ScryptVector(P="pleaseletmein", S="SodiumChloride", N=1048576, r=8, p=1, dklen=64)
        run_test_vector(w)

    def gen_and_store(self, pwd: str) -> None:
        ''' call hashlib.scrypt, and store to json '''
        salt = os.urandom(24)  # bytes
        res = do_scrypt(pwd.encode(), salt)
        fn = self.jsonfile
        output_dict = {}
        for k,v in res.items():
            if isinstance(v, bytes):
                output_dict[k] = base64.b64encode(v).decode()
            else:
                output_dict[k] = v
        with open(fn, "wt", encoding="UTF-8") as fobj:
            print(json.dumps(output_dict, indent=4), file=fobj)
        prt(f'save to: {fn}')

    def read_and_verfify(self, pwd: str) -> bool:
        ''' read json and verify the password'''
        fn = self.jsonfile
        logd = self.logd
        salt = b''
        check_dk = b''
        input_dk = b''
        with open(fn, "rt", encoding="UTF-8") as fobj:
            d = json.load(fobj)
            salt = base64.b64decode(d.get("salt"))
            check_dk = base64.b64decode(d.get("dk"))  # raw bytes
            logd(f'check_dk.hex(): {check_dk.hex()}')
        to_verify = do_scrypt(pwd.encode(), salt)
        input_dk = to_verify.get("dk", b'\xde\xad\xbe\xef')
        logd(f'input_dk.hex(): {input_dk.hex()}')
        return input_dk == check_dk

    def get_str(self, prefix:str, idx: int) -> str:
        ''' get string '''
        return f'{prefix}{idx}'

    def action(self) -> None:
        ''' action '''
        fn = self.jsonfile
        if not os.path.isfile(fn):
            self.gen_and_store(self.PASSWORD)

        for i in range(1,6):
            p = self.get_str('HereIsThePassword', i)
            r = self.read_and_verfify(p)
            msg = "pass" if r else "fail"
            prt(f'input({i}): {p}: {msg}')

    @classmethod
    def run(cls) -> None:
        ''' run '''
        args = do_parser()
        _ = cls(debug=args.debug, pure=args.pure)

def do_parser() -> Any:
    ''' make parser '''
    parser = argparse.ArgumentParser(description='chataes demo encrypt/decrypt')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("-d", "--debug", dest='debug', action='store_true',
        default=False, help='debug mode')
    parser.add_argument("-p", "--pure", dest='pure', action='store_true', default=False)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    ScryptDemo.run()
