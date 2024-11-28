#!/usr/bin/env python3
# coding: utf-8

'''
class LoadPrimeFromText

text table: prime_100k.txt
format:
1 2
2 3
3 5
4 7
...

if pickle exists, use it, or load text

given cli argument to get lower/upper prime

run_example.py is an upgraded version
'''

import os
import pickle
import random
import re
import sys
from time import time

MODNAME = __file__

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.4f} sec')

# pylint: disable=invalid-name

class LoadPrimeFromText():
    ''' class will help to handle read pickle file '''
    def __init__(self, txtfn, pfn):
        #print('__init__')
        # init values
        self.pvalues = None
        self.cache_hit = 0
        self.pfn = pfn
        self.txtfn = txtfn
        self.init_size = 0
        self.need_save = False

    def __enter__(self):
        #print('__enter__')
        self.load_pickle()
        self.init_size = len(self.pvalues)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print('__exit__')
        #print('len(self.pvalues)', len(self.pvalues))
        #print('self.init_size', self.init_size)
        if self.pvalues and not os.path.exists(self.pfn):
            self.save_pickle()

    def __str__(self):
        if self.pvalues is None:
            self.init_size = 0
        else:
            self.init_size = len(self.pvalues)
        msg = f'min: {self.pvalues[0]}, max: {self.pvalues[-1]}, '
        msg = msg + f'total primes: {self.init_size}'
        return msg

    def get_count(self):
        ''' get length of pickle '''
        return len(self.pvalues)

    def load_txtfile(self):
        ''' load primes from txt file, the format is
            1 2
            2 3
            3 5
            4 7
            5 11
        '''
        if not os.path.exists(self.txtfn):
            print(f'{self.txtfn} not found, exit')
            return False
        start = time()
        with open(self.txtfn, "rt", encoding='utf8') as txtinf:
            self.need_save = True
            while True:
                ln = txtinf.readline().strip()
                if ln == '':
                    break
                result = re.match(r'^(\d+)\s+(\d+)', ln)
                if result and len(result.groups()) == 2:
                    el = int(result.groups()[1])
                    self.pvalues.append(el)
        duration = time() - start
        print(f'[INFO] {__file__}: load from {self.txtfn}')
        show_duration(duration)
        return True

    def load_pickle(self):
        ''' load pickle file, or from text '''
        if os.path.exists(self.pfn):
            try:
                start = time()
                with open(self.pfn, "rb") as inf:
                    self.pvalues = pickle.load(inf)
                    self.need_save = False
                    print(f'[INFO] {__file__}: load from {self.pfn}')
                duration = time() - start
                show_duration(duration)
                return True
            except IOError:
                print(f'[INFO] {__file__}: pickle file not found, try to load text file')

        self.pvalues = []
        return self.load_txtfile()

    def find(self, val):
        ''' find val in list of primes '''
        #if val in self.pvalues:
        return self.pvalues.index(val)
        #return -1

    def get_primes_less_than(self, val):
        ''' get a list of primes less than given value '''
        _max = self.pvalues[-1]
        _min = self.pvalues[0]
        if val > _max or val < _min:
            print('[ERROR] out of bound')
            return None
        if val == _min:
            return [2]
        (p, _) = self.search_between(val)
        if p is None:
            print('[ERROR] cannot operate')
            return None
        # ????
        plist = self.pvalues[:p+1]
        return plist


    def search_between(self, val):
        ''' search value at index or between '''
        if self.pvalues is None:
            print('[FAIL] predefined data not available')
            return (None, None)
        if val in self.pvalues:
            return (self.pvalues.index(val), None)
        if val < self.pvalues[0]:
            print(f'{val} is smaller than lower bound')
            return (None, None)
        if val > self.pvalues[-1]:
            print(f'{val} is larger than upper bound')
            return (None, None)

        # start to binary search
        _max = len(self.pvalues) - 1
        _min = 0
        _mid = 0
        _cnt = 0
        while True:
            _cnt += 1
            _mid = (_min + _max) // 2
            if self.pvalues[_mid] > val:
                _max = _mid
            else:
                _min = _mid
            if _min > _max or _min == _max - 1:
                break
            if _cnt > 20:
                print('exceed count')
                break
        return (_min, _max)


    def at(self, idx):
        ''' get value at index '''
        try:
            return self.pvalues[idx]
        except IndexError:
            return None
        except TypeError:
            return None

    def save_pickle(self):
        ''' save pvalues into pickle file '''
        #print(f'[INFO] {__file__}: save_pickle...')
        if self.pvalues is None:
            return
        if self.need_save:
            print(f'[INFO] save pickle to {self.pfn}')
            with open(self.pfn, 'wb') as outf:
                pickle.dump(self.pvalues, outf)

def show(v, p, q):
    ''' show '''
    if p is None and q is None:
        return
    if q is None:
        print(f'{v} is a prime {p}')
    else:
        lhs = abs(v - p)
        rhs = abs(v - q)
        if lhs <= rhs:
            arrow = "<----"
        else:
            arrow = "---->"
        print(f'{v} is in the range of ({p} {arrow} {q})')


def main(argv):
    ''' main function '''
    with LoadPrimeFromText("../data/prime_100k.txt", "prime100k.p") as sp:

        print(sp)

        # inner function
        def test(v):
            ''' test '''
            (p, q) = sp.search_between(v)
            if p is None:
                print('\tno answer for this')
                return
            show(v, sp.at(p), sp.at(q))
        # inner function

        #print(sp)
        #rint(sp.get_count())

        if argv == []:
            _max = sp.at(sp.get_count() - 1)
            _min = sp.at(0)
            #print(f"max:{_max}, min:{_min}")
            REPEAT = 10
            for _ in range(REPEAT):
                r = random.randint(_min, _max)
                test(r)
        else:
            for ss in argv:
                try:
                    val = int(ss)
                    test(val)
                except ValueError:
                    print(f'{ss} is a ValueError')
                    continue


if __name__ == '__main__':
    print('NOTE: run_example.py is an upgraded version')
    main(sys.argv[1:])
