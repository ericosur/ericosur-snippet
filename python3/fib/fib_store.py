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

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

DEBUG = True
if DEBUG:
    logd = logger.debug if USE_LOGURU else print
else:
    logd = do_nothing

class CalcFib():
    ''' class will help to handle read pickle file '''
    def __init__(self, fn='fib.p'):
        logd("__init__")
        # init values
        self.fibvalues = {}
        self.cache_hit = 0
        self.pfile = fn
        self.init_size = len(self.fibvalues)

    def __enter__(self):
        logd('__enter__')
        self.load_pickle()
        self.init_size = len(self.fibvalues)
        logd(f'size={self.init_size}')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logd('__exit__')
        logd(f'size={len(self.fibvalues)}')
        if len(self.fibvalues) > self.init_size:
            self.save_pickle()

    def __str__(self):
        ''' size in str '''
        return f'{len(self.fibvalues)}'

    def fib(self, n: int) -> int:
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

    def get_pickle_len(self) -> int:
        ''' get length of pickle '''
        return len(self.fibvalues)

    def load_pickle(self) -> None:
        ''' load pickle, or default value '''
        logd(f'load_pickle: {self.pfile}')
        try:
            with open(self.pfile, "rb") as inf:
                self.fibvalues = pickle.load(inf)
        except IOError:
            # not a fatal exception
            print(f'warn: IOError while opening {self.pfile}')

    def save_pickle(self) -> None:
        ''' save values into pickle '''
        logd(f'save_pickle: {self.pfile}')
        # store into pickle file
        with open(self.pfile, "wb") as ouf:
            pickle.dump(self.fibvalues, ouf)


def demo():
    ''' demo function '''
    prt('demo of CalcFib()')
    MIN_LIMIT = 499
    MAX_LIMIT = 1000
    MAX_REPEAT = 3

    with CalcFib() as fibv:
        prt(f'before loop, fibvalues has {fibv.get_pickle_len()} entries')
        #prt(fibv)

        for _ in range(MAX_REPEAT):
            n = random.randint(MIN_LIMIT, MAX_LIMIT)
            prt(f'fib({n}) = {fibv.fib(n)}')

        prt(f'after loop, fibvalues has {fibv.get_pickle_len()} entries')

if __name__ == '__main__':
    demo()
