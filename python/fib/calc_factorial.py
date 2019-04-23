#!/usr/bin/python3
# coding: utf-8

import sys
import pickle
import random
from math import log10, ceil

'''
to calculate factorial n!
'''

class CalcFactorial(object):
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
        return len(self.stepvalues)

    def factorial(self, n):
        '''
        if factorial(n) is already calculated, it would not
        re-calculate it again.
        '''
        if n < 2:
            return 1
        elif n in self.stepvalues:
            return self.stepvalues[n]
        else:
            self.stepvalues[n] = n * self.factorial(n - 1)
            return self.stepvalues[n]

    def load_pickle(self):
        try:
            with open(self.dfile, "rb") as inf:
                inf = open(self.dfile, "rb")
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
    with CalcFactorial() as foo:
        #print('before loop, has {} entries'.format(foo.get_pickle_len()))
        ret = foo.factorial(n)
        print("{}! = {}, log10()={}".format(n, ret, ceil(log10(ret))))
        #sret = str(ret)
        #print('len:{}'.format(len(sret)))
        #print(' after loop, has {} entries'.format(foo.get_pickle_len()))


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            for v in sys.argv[1:]:
                print('try v: {}'.format(v))
                calc(int(v))
        else:
            calc(170)
    except:
        print('shit happens:', v)
