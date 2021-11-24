#!/usr/bin/python3
# coding: utf-8

'''
provide a basic interface/class for load/save/search primes
'''

import errno
import os
import pickle
import re
from findlist_func import index, find_le, find_ge

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
        msg = f'min: {self.pvalues[0]}, max: {self.pvalues[-1]}, '
        msg = msg + f'total primes: {self.init_size}'
        return msg

    def get_count(self):
        ''' get length of pickle '''
        return len(self.pvalues)

    @staticmethod
    def get_local_data_path():
        ''' get data file from local '''
        p = os.getenv('HOME') + '/.prime/'
        if os.path.exists(p):
            return p
        return None

    def _try_pickle_file(self):
        ''' _try_pickle_file '''
        if not os.path.exists(self.pfile):
            p = self.get_local_data_path()
            if p:
                f = p + self.pfile
                if os.path.exists(f):
                    self.pfile = f
        if not os.path.exists(self.pfile):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.pfile)

    def _try_text_file(self):
        ''' _try_text_file '''
        if not os.path.exists(self.txtfile):
            p = self.get_local_data_path()
            if p:
                f = p + self.txtfile
                if os.path.exists(f):
                    self.txtfile = f
        if not os.path.exists(self.txtfile):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.txtfile)

    def load_pickle_impl(self):
        ''' load pickle implementation '''
        print('store_prime: load_pickle_imple()')

        self._try_pickle_file()
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
        except FileNotFoundError:
            print('store_prime: pickle file not found, try to load text file')
            self.pvalues = []

        self._try_text_file()

        with open(self.txtfile, "rt", encoding='utf8') as txtinf:
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
        if val > self.pvalues[-1]:
            raise IndexError(f'{val} is larger than the most number' \
                f'in prime table {self.pvalues[-1]}')
        return self.pvalues.index(val)

    def index(self, val: int) -> int:
        ''' use external index() '''
        if val > self.pvalues[-1]:
            raise IndexError(f'{val} is larger than the most number' \
                f'in prime table {self.pvalues[-1]}')
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
        # ????
        plist = self.pvalues[:p+1]
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
            print(f'something wrong for {x}, OOB?')
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
        except (IndexError, TypeError):
            return None

    @staticmethod
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
                arrow = "<-----"
            else:
                arrow = "----->"
            print(f'{v} is in the range of ({p} {arrow} {q})'.format(v, p, arrow, q))

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
    print('run **run_example.py sp** to see the demo...')
