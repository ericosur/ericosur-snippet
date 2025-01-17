#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=unused-import
#

'''
compare digest to hashlib
'''

from hashlib import file_digest
import sys

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    USE_LOGGER = False
logd = logger.debug if USE_LOGGER else print

sys.path.insert(0, "./")
sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
sys.path.insert(0, "python3/b64")
# if python 3.11+, we may use file_digest, instaed sha512sum() ...
from myutil import md5sum, sha512sum, sha3_256sum, sha3_512sum  # type: ignore[import]
from myutil import get_python_versions, run_command  # type: ignore[import]
# setup CLI cmd and function name in the dgst.py
from dgst import digests  # type: ignore[import]

FN = 'a.txt'

def sep():
    ''' sep '''
    prt('-' * 60)

def run_clicmd(item):
    ''' cli cmd '''
    cmd = f'{item['cmd']} {FN}'
    logd(cmd)
    prt(run_command(cmd))

def test2():
    ''' for python 3.11+ '''
    logd("test against file_digest...")
    for d in digests:
        run_clicmd(d)
        hash_cmd = d["hash"]
        with open(FN, 'rb') as f:
            logd(f"try {hash_cmd}...")
            the_digest = file_digest(f, hash_cmd)
        if the_digest:
            prt(the_digest.hexdigest())
        sep()

def test():
    ''' test '''
    for d in digests:
        #logd(d)
        run_clicmd(d)
        # Using eval to call the corresponding function dynamically
        func_name = d['func']
        logd(f'func_name: {func_name}')
        func = globals().get(func_name)
        if func:
            r2 = func(FN)
            prt(r2)
        else:
            logd(f'function not found: {func_name}')
        sep()

def main():
    ''' main '''
    try:
        (major, minor) = get_python_versions()
        logd(f"{major=}, {minor=}")
        if major==3 and int(minor) >= 11:
            prt('[info] use file_digest')
            test2()
        else:
            prt('[info] use my own wrapper functions')
            test()
    except ValueError:
        pass

if __name__ == "__main__":
    main()
