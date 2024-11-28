#!/usr/bin/env python3
# coding: utf-8

'''
provide an interface/class for query primes
'''

#from debug_verbose import MyDebug
from .findlist_func import index, find_le, find_ge


MODNAME = "QueryPrime"
__VERSION__ = "2024.03.27"

#
# initilize self.primes as None
# but all query functions use self.primes as a list
# pylint: disable=unsubscriptable-object
# pylint: disable=unsupported-membership-test
#
class QueryPrime():
    ''' provides functions to query primes '''

    def __init__(self):
        self.primes = None  # a list of prime numbers

    def get_count(self):
        ''' get length of pickle '''
        if self.primes is None:
            raise IndexError
        return len(self.primes)

    def get_maxprime(self):
        ''' return the max prime in this object '''
        return self.primes[-1]

    def at(self, idx):
        ''' get value at index '''
        try:
            return self.primes[idx]
        except (IndexError, TypeError):
            return None

    def find(self, val: int) -> int:
        ''' find val in list of primes, return index
            raise ValueError if not in the prime list
        '''
        if val > self.primes[-1]:
            raise IndexError(f'{val} is larger than the most number' \
                f'in prime table {self.primes[-1]}')
        return self.primes.index(val)

    def get_primes_less_than(self, val: int) -> list:
        ''' get a list of primes less than given value '''
        _max = self.primes[-1]
        _min = self.primes[0]
        if val > _max or val < _min:
            print(f'[ERROR] out of bound: {_min=} {val=} {_max=}')
            return None
        if val == _min:
            return [2]
        (p, _) = self.search_between_idx(val)
        if p is None:
            print('[ERROR] cannot operate')
            return None
        # ????
        plist = self.primes[:p+1]
        return plist

    def index(self, val: int) -> int:
        ''' use external index() '''
        if val > self.primes[-1]:
            raise IndexError(f'{val} is larger than the most number' \
                f'in prime table {self.primes[-1]}')
        return index(self.primes, val)

    def bisect_between_idx(self, val: int) -> tuple:
        '''
        use bisect to search value in list return index for lower, upper bound
        '''
        if self.primes is None:
            print('[FAIL] predefined data not available')
            return (None, None)
        i = index(self.primes, val)
        if i != -1:
            return (i, None)
        # not exactly prime, search lower, upper bound
        a = self.primes
        x = val
        try:
            _, p = find_le(a, x)
            _, q = find_ge(a, x)
            return (p, q)
        except ValueError:
            print(f'something wrong for {x}, OOB?')
            return (None, None)

    def search_between_idx(self, val):
        '''
        search value within primes, return index for lower, upper bound
        '''
        if self.primes is None or not self.primes:
            print('[FAIL] predefined data not available')
            return (None, None)
        if val in self.primes:
            return (val, None)
        if val < self.primes[0]:
            print(f'{val} is smaller than lower bound')
            return (None, None)
        if val > self.primes[-1]:
            print(f'{val} is larger than upper bound')
            return (None, None)

        # start to binary search
        _max = len(self.primes) - 1
        _max_repeat = _max / 4
        _min = 0
        _mid = 0
        _cnt = 0
        while True:
            _cnt += 1
            _mid = (_min + _max) // 2
            if self.primes[_mid] > val:
                _max = _mid
            else:
                _min = _mid
            if _min > _max or _min == _max - 1:
                break
            if _cnt > _max_repeat:
                print(f'{MODNAME}: exceed count')
                break
        return (_min, _max)


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
        arr = self.primes[begin:end]
        return arr


    def get_around(self, v: int) -> None:
        ''' return (p, q) (index, not the value), if p and q is none, p is a prime
            if both none, has no answer (maybe out-of-bound)
        '''
        (p, q) = self.bisect_between_idx(v)
        if p is None:
            print('\tno answer for this')
            return (None, None)
        return (p, q)
