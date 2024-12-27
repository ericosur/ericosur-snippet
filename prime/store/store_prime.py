#!/usr/bin/env python3
# coding: utf-8

'''
provide a basic interface/class for load/save/search primes
'''

import errno
import os
import pickle
from time import time
from .query_prime import QueryPrime
from .load_myutil import MyDebug, MyVerbose
from .textutil import read_textfile
from .load_myutil import dbg, do_nothing

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

MODNAME = "StorePrime"
__VERSION__ = "2024.03.27"
LOCAL_DEBUG = False

prt = rprint if USE_RICH else print
dbg = dbg if LOCAL_DEBUG else do_nothing

def show(v, p, q):
    ''' show the result related to primes '''
    if p is None and q is None:
        return
    if q is None:
        prt(f'{v} is a prime {p}')
    else:
        lhs = abs(v - p)
        rhs = abs(v - q)
        if lhs <= rhs:
            arrow = "<-----"
        else:
            arrow = "----->"
        prt(f'{v} is in the range of ({p} {arrow} {q})')

class StorePrime(MyDebug, MyVerbose, QueryPrime):
    ''' class will help to handle read pickle file '''

    tag = 'StorePrime'

    def __init__(self, txtfn="small.txt", pfn="small.p",
                debug=False, verbose=False):
        # super init
        MyDebug.__init__(self, debug)
        MyVerbose.__init__(self, verbose)
        QueryPrime.__init__(self)

        self.need_save = False
        self.config = {'pfn': pfn, 'txtfn': txtfn}
        dbg(f'__init__(): debug:{self.debug}, verbose:{self.verbose}')
        dbg(f'{self.config=}')

    def __enter__(self):
        dbg("__enter__")
        self.__load_pickle()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        dbg("__exit__")
        if self.primes and not os.path.exists(self.config.get('pfn')):
            self.save_pickle()

    def __str__(self):
        if self.primes is None:
            msg = "Prime numbers are not loaded"
            return msg
        psize = self.get_count()
        pmax = self.get_maxprime()
        msg = f'min: 2, max: {pmax:,}, total primes: {psize:,}'
        return msg

    def logv(self, *args, **wargs):
        ''' print verbose '''
        if not self.verbose:
            return
        prt(*args, **wargs)

    def get_ready(self):
        ''' load prime data '''
        dbg("get_ready")
        if self.primes is None:
            dbg("call self.__load_pickle")
            self.__load_pickle()

    def get_local_data_path(self):
        ''' get data file from local '''
        p =  os.path.join(os.getenv('HOME'), '.prime')
        if os.path.exists(p):
            self.logv(f'[INFO] {MODNAME}: get_local_data_path: {p}')
            return p
        return ''

    def try_pickle_file(self):
        ''' confirm pfn exists '''
        dbg('try_pickle_file()')
        if not os.path.exists(self.config['pfn']):
            p = self.get_local_data_path()
            f = os.path.join(p, self.config['pfn'])
            if os.path.exists(f):
                self.config['pfn'] = f
        if not os.path.exists(self.config['pfn']):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.config['pfn'])

    def try_text_file(self):
        ''' confirm txtfn exists '''
        dbg('try_text_file()')
        if not os.path.exists(self.config['txtfn']):
            p = self.get_local_data_path()
            f = os.path.join(p, self.config['txtfn'])
            if os.path.exists(f):
                self.config['txtfn'] = f
        if not os.path.exists(self.config['txtfn']):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.config['txtfn'])

    def load_pickle_impl(self) -> bool:
        ''' load pickle implementation '''
        dbg("load_pickle_impl()")
        start = time()
        #dbg('call try_pickle_file()...')
        self.try_pickle_file()
        with open(self.config['pfn'], "rb") as inf:
            self.primes = pickle.load(inf)
            self.need_save = False
        duration = time() - start

        self.logv(f'[INFO][{MODNAME}]: load_pickle_impl() from {self.config["pfn"]}')
        self.logv(f'[INFO][{MODNAME}]: duration: {duration:.3f} sec')
        return True

    def __load_pickle(self):
        ''' load pickle file, or from text '''
        dbg("__load_pickle()")
        try:
            dbg("call self.load_pickle_impl()")
            return self.load_pickle_impl()
        except FileNotFoundError:
            print(f'[INFO] {MODNAME}: pickle not found, try to load text file')
            self.primes = []

        dbg("call self.try_text_file")
        self.try_text_file()
        self.need_save = True
        start = time()
        self.primes = read_textfile(self.config['txtfn'], debug=self.debug)
        duration = time() - start
        self.logv(f'[INFO][{MODNAME}]: load from text file {self.config["txtfn"]}', end=' ')
        self.logv(f'duration: {duration:.3f} sec')
        return True

    def save_pickle_impl(self):
        ''' implementation of save pickle '''
        dbg("save_pickle_impl()")
        with open(self.config['pfn'], 'wb') as outf:
            pickle.dump(self.primes, outf)
        prt(f'[INFO][{MODNAME}] save pickle as {self.config["pfn"]}')

    def save_pickle(self):
        ''' save primess into pickle file '''
        dbg("save_pickle()")
        if self.primes is None:
            return
        if self.need_save:
            self.save_pickle_impl()
        else:
            prt(f'[INFO][{MODNAME}] no need to save')

    def test(self, v: int):
        ''' test '''
        (p, q) = self.bisect_between_idx(v)
        if p is None:
            prt('\tno answer for this')
            return
        show(v, self.at(p), self.at(q))

if __name__ == '__main__':
    prt('run **run_example.py** to see the demo...')
