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

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

class MakeDirname():
    ''' make name of dir '''

    def __init__(self, log=do_nothing):
        ''' init '''
        self.fn = None
        self.comment = None
        self.log = log

    def __hash_factory(self, fn, hash_func) -> bytes:
        ''' hash factory, return bytes '''
        BUFSIZE = 65536
        logd = self.log
        dgst = hash_func()
        with open(fn, 'rb') as f:
            while True:
                data = f.read(BUFSIZE)
                if not data:
                    break
                dgst.update(data)
        d = dgst.digest()
        logd(f'__hash_factory: digest in bytes: {d}')
        return d

    def sha256sum_b64(self, fn) -> str:
        ''' sha256sum and return base64 string '''
        logd = self.log
        dgst = self.__hash_factory(fn, hashlib.sha256)
        r = base64.urlsafe_b64encode(dgst).decode()
        letterized = re.sub(r'[-_=]', '', r)
        logd(f'sha256sum+base64: {letterized}')
        return letterized

    def extract_line(self):
        ''' extract line '''
        logd = self.log
        with open(self.fn, "rt", encoding="UTF-8") as fobj:
            cnt = 0
            for ln in fobj.readlines():
                ln = ln.strip()
                cnt += 1
                m = re.match(r'^#(.+)$', ln)
                if m:
                    s = re.sub(r'[-_= ]', '', m[1])
                    logd(f"extract_line: [yellow]{s}")
                    self.comment = s
                    break
        return self.comment

    def process_file(self, fn):
        ''' action '''
        logd = self.log
        logd(f'process_file: fn: {fn}')
        if not os.path.isfile(fn):
            print('[FAIL] file not found:', fn, file=sys.stderr)
            sys.exit(1)
        self.fn = fn
        r = self.sha256sum_b64(fn)
        c = self.extract_line()
        msg = f'{r[:8]}{c}'
        print(msg)

    @classmethod
    def run(cls):
        ''' run '''
        parser = argparse.ArgumentParser(description='mknn64, small tool to generate '
                                         'non-sense filename')
        # nargs like regexp, '*' means 0+, '+' means 1+
        parser.add_argument("files", type=str, nargs='*',
            help="show these strings")
        parser.add_argument("-d", "--debug", action='store_true', default=False,
            help='make dir name')
        args = parser.parse_args()

        logd = do_nothing
        if args.debug:
            if console:
                logd = console.log
            else:
                logd = print
            logd(f'{args.debug=}')

        logd("run...")
        obj = cls(logd)
        # if no file is specified
        DEF_FN = 'a.txt'
        if args.files == []:
            logd('args.files is empty')
            if os.path.isfile(DEF_FN):
                args.files.append(DEF_FN)
            else:
                logd('no suitable files')
                sys.exit(1)
        #logd(args.strings)
        for f in args.files:
            obj.process_file(f)

def main():
    ''' main '''
    MakeDirname.run()

if __name__ == '__main__':
    main()
