#!/usr/bin/env python3
# coding: utf-8
# pylint: disable=wrong-import-position

'''
A package "primesieve" of ubuntu that could generate a list of primes
in a very short time and no need to prepare huge table

list several prime around the given input number
'''

import bisect
import math
import os
import re
import sys
from random import randint
from time import time

sys.path.insert(0, '../')
from make_arrow import make_arrow

MODNAME = "use_primesieve"
VERSION = "2023.10.30"

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3e} sec')


class Solution():
    ''' test date is a prime '''
    TMPFN = f'/tmp/{MODNAME}.txt'
    NUM = 3
    DRY_RUN = False
    # set a upper limit for this script, maybe primesieve could handle it
    MYMAX = 9_999_999_999_999_999_999 # 19 digits or 1e18 - 1

    def __init__(self):
        self.p = []
        self.target = None
        self.n_start = None
        self.n_stop = None
        self.is_prime = None

    def set_target(self, val):
        ''' set target or use the default '''
        if val < 2:
            print(f'[FAIL] {val} is smaller than 2')
            sys.exit(-1)
        if val > self.MYMAX:
            print(f'[FAIL] {val} is too large to handle')
            sys.exit(-1)
        _d = math.ceil(math.log10(val))
        if _d > 6:
            print(f'[INFO] digits of {val} is {_d}')
        self.target = val
        self.is_prime = False
        self.p.clear()
        self.get_range()

    def get_range(self):
        ''' determine the range for upper/lower bound '''
        LOW_LIMIT = 10000
        if 1 < self.target < LOW_LIMIT:
            self.n_start = 1
            self.n_stop = LOW_LIMIT
            return

        # for larger target
        _range = LOW_LIMIT - 1
        self.n_start = max(self.target - _range, 1)
        self.n_stop = self.target + _range

    def _index(self):
        'Locate the leftmost value exactly equal to x'
        a = self.p
        x = self.target
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return -1

    def read_text_file(self, itxtfn):
        ''' process file '''
        cnt = 0
        #print(f'read from {itxtfn}...')
        with open(itxtfn, "rt", encoding='UTF-8') as fin:
            for ln in fin.readlines():
                ln = ln.strip()
                if len(ln) == 0:
                    continue
                if ln.find("#") >= 0:
                    continue
                cnt += 1
                #print(f'{cnt},{ln}')
                try:
                    n = int(ln)
                    self.p.append(n)
                except ValueError:
                    print(f'error at: {cnt}: {ln}')
                    continue
        # remove the temp file
        os.unlink(itxtfn)

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


    def show_results(self):
        ''' show results '''
        idx = self.p.index(self.target)
        lenp = len(self.p)
        _start, _stop = 0, 0
        try:
            _start = max(0, idx - self.NUM)
            _stop = min(idx + self.NUM, lenp - 1)
            if idx-1 <= 0 or idx+1>=lenp:
                arr = ''
            else:
                arr = make_arrow(self.p[max(idx-1,0)], self.target, self.p[min(idx+1,lenp-1)])
        except IndexError:
            print(f'[FAIL] IndexError {idx=}, {lenp=} {_start=} {_stop=}')
            sys.exit(-1)

        s = slice(_start, _stop+1)
        for n in self.p[s]:
            if n == self.target:
                print(self.target, arr, end='')
                if self.is_prime:
                    print(" <<< PRIME")
                else:
                    print()
            else:
                print(n)


    def action(self):
        ''' action '''
        start = time()
        cmd = f'primesieve {self.n_start} {self.n_stop} --print > {self.TMPFN}'
        if self.DRY_RUN:
            print(f'{cmd=}')
            return

        os.system(cmd)
        self.read_text_file(self.TMPFN)
        if len(self.p) == 0:
            print(f'[WARN] picked range is too small to use for {self.target}')

        # if target does not exist in the list, insert it into primes list
        if self._index() == -1:
            self.is_prime = False
            bisect.insort(self.p, self.target)
        else:
            self.is_prime = True

        duration = time() - start
        show_duration(duration)
        self.show_results()

    @classmethod
    def run(cls, targets):
        ''' run me '''
        obj = cls()
        for t in targets:
            obj.set_target(t)
            obj.action()

def main(argv):
    ''' main '''
    inputs = []
    for i in argv:
        try:
            n = int(i)
            inputs.append(n)
        except ValueError:
            pass
    # demo mode
    if len(inputs) == 0:
        for _ in range(3):
            # pick the radix of 10, MUST be < 19
            rad = randint(5, 18)
            inputs.append(randint(10**(rad-1), 10**rad))
    Solution.run(inputs)

if __name__ == '__main__':
    main(sys.argv[1:])
