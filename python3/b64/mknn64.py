#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	sha256sum
'''

import argparse
import base64
import hashlib
import re
import os
import sys
try:
    from rich.console import Console
    console = Console()
except ImportError:
    print('cannot load module rich')

def logd(*args):
    ''' logd '''
    if not MakeDirname.debug:
        return

    if console:
        console.log(*args)
    else:
        print(*args)

class MakeDirname():
    ''' make name of dir '''
    debug = False

    def __init__(self):
        ''' init '''
        self.fn = None
        self.comment = None

    def __hash_factory(self, fn, hash_func) -> bytes:
        ''' hash factory, return bytes '''
        BUFSIZE = 65536
        dgst = hash_func()
        with open(fn, 'rb') as f:
            while True:
                data = f.read(BUFSIZE)
                if not data:
                    break
                dgst.update(data)
        d = dgst.digest()
        logd(f'__hash_factory: {d}')
        return d

    def sha256sum_b64(self, fn) -> str:
        ''' sha256sum and return base64 string '''
        dgst = self.__hash_factory(fn, hashlib.sha256)
        r = base64.urlsafe_b64encode(dgst).decode()
        letterized = re.sub(r'[-_=]', '', r)
        logd(f'sha256sum+base64: {letterized}')
        return letterized

    def extract_line(self):
        ''' extract line '''
        with open(self.fn, "rt", encoding="UTF-8") as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                m = re.match(r'^#\s+([^-_ :]+)$', ln)
                if m:
                    self.comment = m[1]
                    break
        return self.comment

    def process_file(self, fn):
        ''' action '''
        if not os.path.isfile(fn):
            print('[FAIL] file not found:', fn, file=sys.stderr)
            sys.exit(1)
        logd(f'fn: {fn}')
        self.fn = fn
        r = self.sha256sum_b64(fn)
        c = self.extract_line()
        msg = f'{r[:8]}{c}'
        print(msg)

    @classmethod
    def run(cls):
        ''' run '''
        parser = argparse.ArgumentParser(description='mknn64')
        # nargs like regexp, '*' means 0+, '+' means 1+
        parser.add_argument("strings", metavar='file', type=str, nargs='*',
            help="show these strings")
        parser.add_argument("-d", "--debug", action='store_true', default=False,
            help='make dir name')
        args = parser.parse_args()

        if args.debug:
            print(f'{args.debug}')
            MakeDirname.debug = args.debug

        obj = cls()
        # if no file is specified
        DEF_FN = 'a.txt'
        if not args.strings:
            if os.path.isfile(DEF_FN):
                args.strings.append(DEF_FN)
        for f in args.strings:
            obj.process_file(f)

def main():
    ''' main '''
    MakeDirname.run()

if __name__ == '__main__':
    main()
