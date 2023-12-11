#!/usr/bin/env python3
# coding: utf-8

'''
Format of 2T_part1.txt is ten prime number one line
Read it and save as one prime number one line
'''

import os
import pickle
import re
import sys
from time import time

MODNAME = "norm2t.py"
VERSION = "2023.10.24"

try:
    import compress_pickle
except ImportError as err:
    print(f'[FAIL] {MODNAME}: cannot load module **compress_pickle**')
    raise ImportError(f"[FAIL] {MODNAME} cannot load module") from err


# --pylint: disable=import-error
# --pylint: disable=unused-import
# --pylint: disable=wrong-import-position

sys.path.insert(0, '../')
from load_myutil import get_u1_path, gethome, read_setting

# try to import StorePrime class
try:
    # larger and slower for loading pickle
    from sip import LoadCompressPrime as StorePrime
    print(f'[INFO] {MODNAME}: use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker for loading pickle
    from store_prime import StorePrime
    print(f'[INFO] {MODNAME}: use **store_prime**')


# pylint: disable=invalid-name
class Solution():
    ''' test date is a prime '''
    def __init__(self):
        self.p = []
        d = read_setting("setting.json")
        self.ppath = ''
        if d is not None:
            self.ppath = os.path.join(gethome(), d['prime_path'])

    def __str__(self):
        ''' stringify '''
        return f'{self.ppath=}'

    @staticmethod
    def show_duration(duration):
        ''' show duration '''
        print(f'{MODNAME}: duration: {duration:.3e} sec')

    def input_txtfile(self, itxtfn):
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

    def output_txtfile(self, otxtfn):
        ''' output to text file '''
        with open(otxtfn, "wt", encoding='UTF-8') as fout:
            for p in self.p:
                print(p, file=fout)
        print(f'output to {otxtfn}')

    def load_pickle_file(self, pfn) -> bool:
        ''' load pickle implementation '''
        #print(f'{MODNAME}: load_pickle_impl()')
        start = time()
        with open(pfn, "rb") as inf:
            self.p = pickle.load(inf)
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
            '2T_part1.txt', '2T_part2.txt', '2T_part3.txt',
            '2T_part4.txt', '2T_part5.txt', '2T_part6.txt'
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

        # output...
        ofn = os.path.join(self.ppath, '2T_p1to6.txt')
        #print(ofn)
        self.output_txtfile(ofn)
        pfn = os.path.join(self.ppath, "2T.p")
        self.save_pickle_file(pfn)
        pcfn = os.path.join(self.ppath, "2T.p.lzma")
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
