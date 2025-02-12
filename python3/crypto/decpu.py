#!/usr/bin/env python3
#coding:UTF-8

'''
decrypt and get the data

reference:
https://typer.tiangolo.com/tutorial/options/
'''

import os
import sys
from typing import Annotated
from passutil import PassUtil
import typer

class Demo():
    ''' demo '''
    DATA = 'The quick smart fox jumps over the lazy dog'

    def __init__(self, jsonfile: str, verbose: bool, debug: bool):
        self.jsonfile = jsonfile
        self.verbose = verbose
        self.debug = debug

    def encrypt(self) -> None:
        ''' how to use PassUtil to encrypt and output to a json '''
        fn = self.jsonfile
        if self.verbose:
            print(f'[INFO] will output to: {fn}')
        passobj = PassUtil(fn, self.debug)
        passobj.encrypt(self.DATA.encode())
        passobj.save()

    def decrypt(self, demo: bool = False) -> None:
        ''' how to use PassUtil to decrypt and get the plain text '''
        fn = self.jsonfile
        if not os.path.isfile(fn):
            print(f'[FAIL] file not found: {fn}')
            sys.exit(1)
        if self.verbose:
            print(f'[INFO] decrypt {fn}')
        decobj = PassUtil(fn, self.debug)
        decobj.load()
        res = decobj.decrypt()
        res_str = res.decode()
        print(res_str)

        # demo: assert the result
        if demo:
            assert res_str==self.DATA

    def run_demo(self) -> None:
        ''' run demo '''
        print(f'demo: generate: {self.jsonfile}')
        self.encrypt()
        print(f'demo: decrypt: {self.jsonfile}')
        self.decrypt(demo=True)

def main(fn: Annotated[str, typer.Argument(help="assign file to decrypt")] = "my.json",
         debug: Annotated[bool, typer.Option("--debug", help="toggle debug info")] = False,
         demo: Annotated[bool, typer.Option("--demo", help="demo from scratch")] = False,
         verbose: Annotated[bool, typer.Option("--verbose", "-v",
                                               help="verbose info")] = False) -> None:
    '''
    Decrypts the specified json file, and show plain text.

    To generate specific json:

    passutil.py -o my.json THE_PLAIN_TEXT

    '''

    if demo:
        obj = Demo(jsonfile="demo.json", verbose=verbose, debug=debug)
        obj.run_demo()
    else:
        obj = Demo(jsonfile=fn, verbose=verbose, debug=debug)
        obj.decrypt()

if __name__ == "__main__":
    typer.run(main)
