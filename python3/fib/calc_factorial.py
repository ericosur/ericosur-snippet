#!/usr/bin/env python3
# coding: utf-8

'''
to calculate factorial n!
'''

import sys
import pickle
#import random
from math import log10, ceil


class CalcFactorial():
    ''' class will help to load pickle file '''
    def __init__(self, fn='factorial.p'):
        # init values
        self.stepvalues = {}
        self.cache_hit = 0
        self.dfile = fn
        self.init_size = len(self.stepvalues)

    def __enter__(self):
        self.load_pickle()
        self.init_size = len(self.stepvalues)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print('__exit__')
        if self.get_pickle_len() > self.init_size:
            self.save_pickle()

    def get_pickle_len(self):
        ''' get length of pickle '''
        return len(self.stepvalues)

    def factorial(self, n):
        '''
        if factorial(n) is already calculated, it would not
        re-calculate it again.
        '''
        if n < 2:
            return 1
        if n in self.stepvalues:
            return self.stepvalues[n]

        self.stepvalues[n] = n * self.factorial(n - 1)
        return self.stepvalues[n]

    def load_pickle(self):
        ''' load pickle file '''
        try:
            with open(self.dfile, "rb") as inf:
                #inf = open(self.dfile, "rb")
                self.stepvalues = pickle.load(inf)
        except FileNotFoundError:
            pass

    def save_pickle(self):
        '''
        儲存 stepvalues 至 pickle
        '''
        with open(self.dfile, "wb") as ouf:
            pickle.dump(self.stepvalues, ouf)


def calc(n):
    ''' main test function '''
    with CalcFactorial() as fact:
        #print('before loop, has {} entries'.format(foo.get_pickle_len()))
        ret = fact.factorial(n)
        print(f"{n}! = {ret}, log10()={ceil(log10(ret))}")
        #sret = str(ret)
        #print(f'len:{len(sret)}')
        #print(f' after loop, has {foo.get_pickle_len()} entries')


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            for v in sys.argv[1:]:
                print(f'try v: {v}')
                calc(int(v))
        else:
            calc(170)
    except ValueError as e:
        print('shit happens at {v}, exception: {e}')
