#!/usr/bin/env python3
# coding: utf-8

'''
Fibonacci number

to demo a fib function which would store calculated fib(n)
to elimate unnecessary recursive and calculation

using pickle as cache
'''

import pickle
import random

class CalcFib():
    ''' class will help to handle read pickle file '''
    def __init__(self, fn='fib.p'):
        #print('__init__')
        # init values
        self.fibvalues = {}
        self.cache_hit = 0
        self.pfile = fn
        self.init_size = len(self.fibvalues)

    def __enter__(self):
        #print('__enter__')
        self.load_pickle()
        self.init_size = len(self.fibvalues)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print('__exit__')
        if len(self.fibvalues) > self.init_size:
            self.save_pickle()

    def fib(self, n):
        '''
        if fib(n) is already calculated, it would not
        re-calculate it again.
        '''
        if n <= 2:
            return 1
        if n in self.fibvalues:
            self.cache_hit += 1
            return self.fibvalues[n]
        #print("n:", n)
        self.fibvalues[n] = self.fib(n-1) + self.fib(n-2)
        return self.fibvalues[n]

    def get_pickle_len(self):
        ''' get length of pickle '''
        return len(self.fibvalues)

    def load_pickle(self):
        ''' load pickle, or default value '''
        #print('load_pickle', self.pfile)
        try:
            with open(self.pfile, "rb") as inf:
                self.fibvalues = pickle.load(inf)
        except IOError:
            print('IOError')

    def save_pickle(self):
        ''' save values into pickle '''
        #print('save_pickle')
        # store into pickle file
        with open(self.pfile, "wb") as ouf:
            pickle.dump(self.fibvalues, ouf)


def main():
    ''' main function '''
    MAX_UPPER_LIMIT = 1000
    MAX_REPEAT_TIME = 10

    with CalcFib() as fibv:
        print(f'before loop, fibvalues has {fibv.get_pickle_len()} entries')

        for _ in range(MAX_REPEAT_TIME):
            n = random.randint(1, MAX_UPPER_LIMIT)
            print(f'fib({n}) = {fibv.fib(n)}')

        print(f'after loop, fibvalues has {fibv.get_pickle_len()} entries')


if __name__ == '__main__':
    main()
