#!/usr/bin/env python3
# coding: utf-8

'''
AES encrypt / decrypt sample

https://www.pycryptodome.org/src/examples

install module Crypto by:
pip install pycryptodome
'''

import argparse
import base64
import hashlib
import sys
import json
from typing import Any, Dict, Tuple
from loguru import logger
try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
except ImportError:
    print('need install pycryptodome')
    sys.exit(1)

MODULE = "passutil"

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing'''
    return None

class PassUtil():
    ''' password utility '''
    def __init__(self, jsonfile="passutil.json", debug=False):
        self.a_dict = {}
        self.jsf = jsonfile
        self.key: bytes = self.__get_derivedkey__()
        self.a_dict['key'] = self.b64enc(self.key)
        self.logd = logger.debug if debug else do_nothing

    def __get_derivedkey__(self) -> bytes:
        ''' generate derived key '''
        d = get_random_bytes(128)
        s = get_random_bytes(32)
        dk = hashlib.scrypt(d, salt=s, n=16384, r=8, p=1, dklen=32)
        return dk

    @staticmethod
    def b64enc(the_bytes: bytes) -> bytes:
        ''' base64.encode '''
        return base64.b64encode(the_bytes)

    @staticmethod
    def b64dec(the_bytes: bytes) -> bytes:
        ''' base64.decode '''
        val = the_bytes.decode()
        return base64.b64decode(val)

    def save(self)  -> None:
        ''' save to json file '''
        fn = self.jsf
        logd = self.logd
        # serialize to str
        d = {}
        for k,v in self.a_dict.items():
            s = "null"
            if isinstance(v, str):
                s = v
            elif isinstance(v, bytes):
                s = v.decode()
            d[k] = s
        logd(f'save json to: {fn}')
        if fn == "sys.stdout":
            print(json.dumps(d, indent=4), file=sys.stdout)
        else:
            with open(fn, "wt", encoding="UTF-8") as fobj:
                print(json.dumps(d, indent=4), file=fobj)

    def load(self) -> Dict | None:
        ''' load from json '''
        fn = self.jsf
        logd = self.logd
        logd(f'load json from {fn}')
        with open(fn, 'r', encoding='utf8') as fobj:
            try:
                data = json.load(fobj)
            except json.decoder.JSONDecodeError as e:
                logd('load: error while processing:', fn)
                logd('load: json.decoder.JSONDecodeError:', e)
                return None
        for k,v in data.items():
            self.a_dict[k] = v.encode()
            logd(f'load: {k}={v}')
        return data

    def encrypt(self, data: bytes) -> None:
        ''' aes encrypt '''
        if not isinstance(data, bytes):
            raise TypeError("type of data MUST be bytes")

        key = self.b64dec(self.a_dict['key'])
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)

        self.a_dict['cn'] = self.b64enc(cipher.nonce)
        self.a_dict['tg'] = self.b64enc(tag)
        self.a_dict['ciphertext'] = self.b64enc(ciphertext)

    def __decodeb64__(self) -> Tuple[bytes, bytes, bytes, bytes]:
        ''' load data '''
        cn = self.b64dec(self.a_dict['cn'])
        tg = self.b64dec(self.a_dict['tg'])
        ky = self.b64dec(self.a_dict['key'])
        ct = self.b64dec(self.a_dict['ciphertext'])
        return cn, tg, ky, ct

    def decrypt(self) -> bytes:
        ''' aes decrypt '''
        nonce, tag, key, ciphertext = self.__decodeb64__()
        # let's assume that the key is somehow available again
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data

def verify(in_fn: str) -> None:
    ''' verify '''
    decpu = PassUtil(in_fn)
    decpu.load()
    decpu.decrypt()

class Main():
    ''' main '''
    debug = False
    verbose = False

    def __init__(self):
        self.args = None
        self.logd = logger.debug if Main.debug else do_nothing

    def do_parser(self) -> Any:
        ''' make parser '''
        parser = argparse.ArgumentParser(description='passutil helps to store some text')
        # nargs like regexp, '*' means 0+, '+' means 1+
        parser.add_argument("strings", metavar='str', type=str, nargs='+',
            help="specify string to store")
        parser.add_argument('-o', '--output', dest='out_fn',
            help='Output file name', default='sys.stdout')
        parser.add_argument("-d", "--debug", dest='debug', action='store_true',
            default=False, help='debug mode')
        parser.add_argument("-v", "--verbose", dest='verbose', action='store_true',
            default=False, help='verbose mode')
        return parser

    @classmethod
    def run(cls) -> None:
        ''' run '''
        obj = cls()
        obj.action()

    def generate(self, the_text: str, out_fn: str) -> None:
        ''' main '''
        logd = self.logd
        logd(f"generate: {the_text}, {out_fn}")
        data = the_text.encode()    # to bytes
        pu = PassUtil(out_fn)
        pu.encrypt(data)
        pu.save()
        del pu

    def action(self) -> None:
        ''' action '''
        logd = self.logd
        parser = self.do_parser()
        self.args = parser.parse_args()
        Main.debug = self.args.debug
        Main.verbose = self.args.verbose

        logd("strings:", self.args.strings)
        if self.args.out_fn:
            logd('output:', self.args.out_fn)
        texts = ' '.join(self.args.strings)
        self.generate(texts, self.args.out_fn)

if __name__ == '__main__':
    Main.run()
