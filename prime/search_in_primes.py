#!/usr/bin/python3
# coding: utf-8

'''
table: prime_100k.txt
will load/save it as pickle format

given cli argument to get lower/upper prime

'''

import os
import sys
import pickle
import re
import random

# pylint: disable=invalid-name

class StorePrime():
    ''' class will help to handle read pickle file '''
    def __init__(self, txtfn='prime_100k.txt', pfn='primes.p'):
        #print('__init__')
        # init values
        self.pvalues = None
        self.cache_hit = 0
        self.pfile = pfn
        self.txtfile = txtfn
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
        if self.pvalues and not os.path.exists(self.pfile):
            self.save_pickle()

    def __str__(self):
        if self.pvalues is None:
            self.init_size = 0
        else:
            self.init_size = len(self.pvalues)
        msg = 'length: {}'.format(self.init_size)
        return msg

    def get_count(self):
        ''' get length of pickle '''
        return len(self.pvalues)

    def load_pickle(self):
        '''
        load pickle file, or from text
        '''
        try:
            with open(self.pfile, "rb") as inf:
                self.pvalues = pickle.load(inf)
                self.need_save = False
                return True
        except IOError:
            print('pickle file not found, try to load text file')
            self.pvalues = []

        if not os.path.exists(self.txtfile):
            print('{} not found, exit'.format(self.txtfile))
            return False

        with open(self.txtfile, "rt") as txtinf:
            self.need_save = True
            while True:
                ln = txtinf.readline().strip()
                if ln == '':
                    break
                result = re.match(r'^(\d+)\s+(\d+)', ln)
                if result and len(result.groups()) == 2:
                    el = int(result.groups()[1])
                    self.pvalues.append(el)
        return True

    def search_between(self, val):
        ''' search value at index or between '''
        if self.pvalues is None:
            print('[FAIL] predefined data not available')
            return (None, None)
        if val in self.pvalues:
            return (self.pvalues.index(val), None)
        if val < self.pvalues[0]:
            print('{} is smaller than lower bound'.format(val))
            return (None, None)
        if val > self.pvalues[-1]:
            print('{} is larger than upper bound'.format(val))
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
        print('save pickle')
        if self.pvalues is None:
            return
        if self.need_save:
            with open(self.pfile, 'wb') as outf:
                pickle.dump(self.pvalues, outf)
        else:
            print('no need to save')

def show(v, p, q):
    ''' show '''
    if p is None and q is None:
        return
    if q is None:
        print('{} is a prime {}'.format(v, p))
    else:
        lhs = abs(v - p)
        rhs = abs(v - q)
        if lhs <= rhs:
            arrow = "<<<<<"
        else:
            arrow = ">>>>>"
        print('{} is in the range of ({} {} {})'.format(v, p, arrow, q))


def main(argv):
    ''' main function '''
    with StorePrime() as sp:

        ''' inner function '''
        def test(v):
            ''' test '''
            (p, q) = sp.search_between(v)
            if p is None:
                print('\tno answer for this')
                return
            show(v, sp.at(p), sp.at(q))
        ''' inner function '''

        #print(sp)
        #rint(sp.get_count())

        if argv == []:
            _max = sp.at(sp.get_count() - 1)
            _min = sp.at(0)
            #print("max:{}, min:{}".format(_max, _min))
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
                    print('{} is a ValueError'.format(ss))
                    continue


if __name__ == '__main__':
    main(sys.argv[1:])
