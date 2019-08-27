#!/usr/bin/python3
# coding: utf-8

'''
provide a basic interface/class for load/save/search primes
'''

import os
import pickle
import re
from bisect import bisect_left, bisect_right

# pylint: disable=invalid-name

def index(a: list, x: int):
    ''' return index of the leftmost value exactly equal to x '''
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

def find_lt(a: list, x: int):
    ''' Find rightmost value less than x '''
    i = bisect_left(a, x)
    if i:
        return a[i-1], i-1
    raise ValueError

def find_le(a: list, x: int):
    ''' Find rightmost value less than or equal to x '''
    i = bisect_right(a, x)
    if i:
        return a[i-1], i-1
    raise ValueError

def find_gt(a: list, x: int):
    ''' Find leftmost value greater than x '''
    i = bisect_right(a, x)
    if i != len(a):
        return a[i], i
    raise ValueError

def find_ge(a: list, x: int):
    ''' Find leftmost item greater than or equal to x '''
    i = bisect_left(a, x)
    if i != len(a):
        return a[i], i
    raise ValueError

class StorePrime():
    ''' class will help to handle read pickle file '''
    def __init__(self, txtfn='small.txt', pfn='small.p'):
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
        msg = 'min: {}, max: {}, '.format(self.pvalues[0], self.pvalues[-1])
        msg = msg + 'total primes: {}'.format(self.init_size)
        return msg

    def get_count(self):
        ''' get length of pickle '''
        return len(self.pvalues)

    def load_pickle_impl(self):
        ''' load pickle implementation '''
        with open(self.pfile, "rb") as inf:
            self.pvalues = pickle.load(inf)
            self.need_save = False
            return True

    def load_pickle(self):
        '''
        load pickle file, or from text
        '''
        try:
            return self.load_pickle_impl()
        except IOError:
            print('pickle file not found, try to load text file')
            self.pvalues = []

        if not os.path.exists(self.txtfile):
            print('{} not found, exit'.format(self.txtfile))
            return False

        with open(self.txtfile, "rt") as txtinf:
            self.need_save = True
            error_count = 0
            while True:
                ln = txtinf.readline().strip()
                if ln == '':
                    break
                if error_count > 10:
                    print('invalid format?')
                    break
                result = re.match(r'^(\d+)$', ln)
                if result:
                    el = int(result.groups()[0])
                    self.pvalues.append(el)
                else:
                    error_count += 1
        return True

    def save_pickle_impl(self):
        ''' implementation of save pickle '''
        with open(self.pfile, 'wb') as outf:
            pickle.dump(self.pvalues, outf)

    def save_pickle(self):
        ''' save pvalues into pickle file '''
        print('save pickle')
        if self.pvalues is None:
            return
        if self.need_save:
            self.save_pickle_impl()
        else:
            print('no need to save')

    def find(self, val: int) -> int:
        ''' find val in list of primes '''
        #if val in self.pvalues:
        return self.pvalues.index(val)
        #return -1

    def index(self, val: int) -> int:
        ''' use external index() '''
        return index(self.pvalues, val)

    def get_primes_less_than(self, val: int) -> list:
        ''' get a list of primes less than given value '''
        _max = self.pvalues[-1]
        _min = self.pvalues[0]
        if val > _max or val < _min:
            print('[ERROR] out of bound')
            return None
        if val == _min:
            return [2]
        (p, _) = self.search_between_idx(val)
        if p is None:
            print('[ERROR] cannot operate')
            return None
        plist = self.pvalues[:p]
        return plist

    def bisect_between_idx(self, val: int) -> tuple:
        '''
        use bisect to search value in list return index for lower, upper bound
        '''
        if self.pvalues is None:
            print('[FAIL] predefined data not available')
            return (None, None)
        i = index(self.pvalues, val)
        if i != -1:
            return (i, None)
        # not exactly prime, search lower, upper bound
        a = self.pvalues
        x = val
        try:
            _, p = find_le(a, x)
            _, q = find_ge(a, x)
            return (p, q)
        except ValueError:
            print('something wrong for {}, OOB?'.format(x))
            return (None, None)


    def search_between_idx(self, val):
        '''
        search value within primes, return index for lower, upper bound
        '''
        if self.pvalues is None or self.pvalues == []:
            print('[FAIL] predefined data not available')
            return (None, None)
        if val in self.pvalues:
            return (val, None)
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
        except (IndexError, TypeError):
            return None

    @staticmethod
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

    def test(self, v: int):
        ''' test '''
        (p, q) = self.bisect_between_idx(v)
        if p is None:
            print('\tno answer for this')
            return
        StorePrime.show(v, self.at(p), self.at(q))

    def list_nearby(self, v: int) -> list:
        ''' print primes nearby v '''
        (p, q) = self.bisect_between_idx(v)
        #print('p, q:', p, q)
        if p is None:
            print('\tno answer for this')
            return None
        begin = 0
        count = 4
        if p > count:
            begin = p - count
        if q is None:   # pos p is a prime
            end = p + count + 1
        else:
            end = p + count + 2
        arr = self.pvalues[begin:end]
        return arr

if __name__ == '__main__':
    print('run **test_sp.py sp** to see the demo...')
