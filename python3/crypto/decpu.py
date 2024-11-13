#!/usr/bin/python3
#coding:UTF-8

'''
decrypt and get the data

reference:
https://typer.tiangolo.com/tutorial/options/
'''

import os
import sys
#from typing import Optional
from typing_extensions import Annotated
from passutil import PassUtil
import typer

DATA = 'The quick smart fox jumps over the lazy dog'

def __encrypt(verbose: bool) -> str:
    ''' how to use PassUtil to encrypt and output to a json '''
    fn = '__tmp__.json'
    if verbose:
        print(f'[INFO] will output to: {fn}')
    obj = PassUtil(fn)
    obj.encrypt(DATA.encode())
    obj.save()
    return fn

def __decrypt(fn: str, verbose: bool, demo: bool = False) -> None:
    ''' how to use PassUtil to decrypt and get the plain text '''
    if not os.path.isfile(fn):
        print(f'[FAIL] file not found: {fn}')
        sys.exit(1)
    if verbose:
        print(f'[INFO] decrypt {fn}')
    decpu = PassUtil(fn)
    decpu.load()
    p = decpu.decrypt()
    print(p.decode())

    # demo: assert the result
    if demo:
        assert p.decode()==DATA

def __demo(verbose: bool) -> None:
    ''' do demo '''
    fn = __encrypt(verbose)
    __decrypt(fn, verbose, True)

def main(fn: Annotated[str, typer.Argument(help="assign file to decrypt")] = "my.json",
         demo: Annotated[bool, typer.Option("--demo", "-d", help="demo from scratch")] = False,
         verbose: Annotated[bool, typer.Option("--verbose", "-v",
                                               help="verbose info")] = False) -> None:
    '''
    decrypt specified file, if no necessary file, use:

    passutil.py -o my.json THE_PLAIN_TEXT
    '''
    if demo:
        __demo(verbose)
        return

    __decrypt(fn, verbose)

if __name__ == "__main__":
    typer.run(main)
