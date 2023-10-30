#!/usr/bin/env python3
# coding: utf-8

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
from time import time
from random import randint

MODNAME = "use_primesieve"
VERSION = "2023.10.30"

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3e} sec')


class Solution():
    ''' test date is a prime '''
    TMPFN = f'/tmp/{MODNAME}.txt'
    NUM = 3

    def __init__(self):
        self.p = []
        self.target = None
        self.n_start = None
        self.n_stop = None
        self.is_prime = None

    def set_target(self, val):
        ''' set target or use the default '''
        if self.target < 2:
            raise ValueError
        self.target = val
        self.is_prime = False
        self.p.clear()
        self.get_range()

    def get_range(self):
        ''' determine the range for upper/lower bound '''
        THOUSAND = 3
        digits = int(math.log10(self.target)) + 1
        tail = digits // THOUSAND
        if tail < THOUSAND:
            drange = 99
        else:
            drange = 10**tail - 1

        #print(f'{tail=} {drange=}')
        self.n_start = self.target - drange
        self.n_start = max(self.n_start, 1)
        self.n_stop = self.target + drange

        #print(f'{self.n_start=}, {self.n_stop=}')

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
        if idx - self.NUM >= 0:
            _start = idx - self.NUM
        else:
            _start = 0
        if idx + self.NUM < lenp:
            _stop = idx + self.NUM
        else:
            _stop = lenp - 1

        s = slice(_start, _stop+1)
        for n in self.p[s]:
            if n == self.target:
                if self.is_prime:
                    print("PRIME ===>", self.target)
                else:
                    print("=========>", self.target)
            else:
                print(n)


    def action(self):
        ''' action '''
        start = time()
        cmd = f'primesieve {self.n_start} {self.n_stop} --print > {self.TMPFN}'
        #print(f'{cmd=}')
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
    if len(inputs) == 0:
        for _ in range(3):
            inputs.append(randint(10**12, 10**16))
    Solution.run(inputs)

if __name__ == '__main__':
    main(sys.argv[1:])
