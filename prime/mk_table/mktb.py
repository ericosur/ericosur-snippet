#!/usr/bin/env python3
# coding: utf-8

'''
Format of 2T_part1.txt is ten prime number one line
Read it and save as one prime number one line
'''

import os
import sys
import pickle
from time import time

MODNAME = "mktb.py"
VERSION = "2023.10.24"

try:
    import compress_pickle
except ImportError as err:
    print(f'[FAIL] {MODNAME}: cannot load module **compress_pickle**')
    raise ImportError(f"[FAIL] {MODNAME} cannot load module") from err


sys.path.insert(0, '../')
from load_myutil import GetConfig

class Solution():
    ''' test date is a prime '''
    def __init__(self):
        obj = GetConfig()
        self.ppath = obj.get_full_ppath()
        self.d = obj.get_small_config()
        print(self.d)
        self.p = []

    @staticmethod
    def show_duration(duration):
        ''' show duration '''
        print(f'{MODNAME}: duration: {duration:.3e} sec')

    def input_txtfile(self, itxtfn):
        ''' process file '''
        cnt = 0
        print(f'read from {itxtfn}...')
        with open(itxtfn, "rt", encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                ln.strip()
                cnt += 1
                try:
                    self.p.append(int(ln))
                except ValueError:
                    print('[FAIL] invalid ln:', ln)

    def input_txtfile_re(self, itxtfn):
        ''' process file '''
        cnt = 0
        r = re.compile(r'\b\d+\b')
        print(f'read from {itxtfn}...')
        with open(itxtfn, "rt", encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                ln.strip()
                cnt += 1
                m = r.findall(ln)
                if m:
                    if cnt < 3:
                        print(m)
                    else:
                        print(f'{cnt}\r', end='')

                    t = [ int(x) for x in m ]
                    self.p.extend(t)

                    # dry run
                    print('[INFO] Dry run...')
                    if cnt > 10:
                        break

    def load_pickle_file(self, pfn) -> bool:
        ''' load pickle implementation '''
        #print(f'{MODNAME}: load_pickle_impl()')
        start = time()
        self._try_pickle_file()
        with open(pfn, "rb") as inf:
            p = pickle.load(inf)

        duration = time() - start
        print(f'[INFO] {MODNAME}: load_pickle_impl() from {pfn}')
        Solution.show_duration(duration)
        return True

    def save_pickle_file(self, pfn):
        ''' implementation of save pickle '''
        with open(pfn, 'wb') as outf:
            pickle.dump(self.p, outf)
        print(f'[INFO] {MODNAME} save pickle as {pfn}')

    def load_compress_pickle(self, pcfn):
        ''' load primes from compressed pickle '''
        start = time()
        self.p = compress_pickle.load(pcfn)
        print(f'{MODNAME}: primes from:', pcfn)
        duration = time() - start
        Solution.show_duration(duration)
        return True

    def save_compress_pickle(self, pcfn):
        ''' save primes into compressed pickle file '''
        start = time()
        compress_pickle.dump(self.p, pcfn)
        duration = time() - start
        print(f'[INFO] {MODNAME} save pickle as {pcfn}')
        Solution.show_duration(duration)

    def action(self):
        ''' action '''
        files = [
            "small.txt"
        ]
        # input ...
        start = time()
        for f in files:
            fn = os.path.join(self.ppath, f)
            #print(fn)
            self.input_txtfile(fn)
            print('len:', len(self.p))
        duration = time() - start
        Solution.show_duration(duration)

        pfn = os.path.join(self.ppath, "small.p")
        self.save_pickle_file(pfn)
        pcfn = os.path.join(self.ppath, "small.p.lzma")
        self.save_compress_pickle(pcfn)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        #print(obj)
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
