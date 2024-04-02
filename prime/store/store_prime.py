#!/usr/bin/python3
# coding: utf-8

'''
provide a basic interface/class for load/save/search primes
'''

import errno
import os
import pickle
import re
from time import time
from .query_prime import QueryPrime
from .load_myutil import MyDebug, MyVerbose


MODNAME = "StorePrime"
__VERSION__ = "2024.03.27"

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
        print(f'{v} is in the range of ({p} {arrow} {q})')

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
        self._info(f'__init__(): debug:{self.debug}, verbose:{self.verbose}')

    def __enter__(self):
        self._info("__enter__")
        self.__load_pickle()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._info("__exit__")
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

    def _info(self, *args, **wargs):
        ''' print info '''
        if 'tag' not in wargs:
            wargs['tag'] = MODNAME
        self.logd(*args, **wargs)

    def logv(self, *args, **wargs):
        ''' print verbose '''
        if self.verbose:
            print(*args, **wargs)

    def get_ready(self):
        ''' load prime data '''
        self._info("get_ready")
        if self.primes is None:
            self._info("call self.__load_pickle")
            self.__load_pickle()

    def get_local_data_path(self):
        ''' get data file from local '''
        p =  os.path.join(os.getenv('HOME'), '.prime')
        if os.path.exists(p):
            self.logv(f'[INFO] {MODNAME}: get_local_data_path: {p}')
            return p
        return ''

    def try_pickle_file(self):
        ''' try_pickle_file '''
        self._info('try_pickle_file()')
        if not os.path.exists(self.config['pfn']):
            p = self.get_local_data_path()
            f = os.path.join(p, self.config['pfn'])
            if os.path.exists(f):
                self.config['pfn'] = f
        if not os.path.exists(self.config['pfn']):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.config['pfn'])

    def try_text_file(self):
        ''' try_text_file '''
        self._info('try_text_file()')
        if not os.path.exists(self.config['txtfn']):
            p = self.get_local_data_path()
            f = os.path.join(p, self.config['txtfn'])
            if os.path.exists(f):
                self.config['txtfn'] = f
        if not os.path.exists(self.config['txtfn']):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.config['txtfn'])

    def load_pickle_impl(self) -> bool:
        ''' load pickle implementation '''
        self._info("load_pickle_impl()")
        start = time()
        #self._info('call try_pickle_file()...')
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
        self._info("__load_pickle()")
        try:
            self._info("call self.load_pickle_impl()")
            return self.load_pickle_impl()
        except FileNotFoundError:
            print(f'[INFO] {MODNAME}: pickle not found, try to load text file')
            self.primes = []

        self._info("call self.try_text_file")
        self.try_text_file()
        start = time()
        with open(self.config['txtfn'], "rt", encoding='utf8') as txtinf:
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
                    self.primes.append(el)
                else:
                    error_count += 1
        duration = time() - start
        self.logv(f'[INFO][{MODNAME}]: load from text file {self.config["txtfn"]}', end=' ')
        self.logv(f'duration: {duration:.3f} sec')
        return True

    def save_pickle_impl(self):
        ''' implementation of save pickle '''
        self._info("save_pickle_impl()")
        with open(self.config['pfn'], 'wb') as outf:
            pickle.dump(self.primes, outf)
        print(f'[INFO][{MODNAME}] save pickle as {self.config["pfn"]}')

    def save_pickle(self):
        ''' save primess into pickle file '''
        self._info("save_pickle()")
        if self.primes is None:
            return
        if self.need_save:
            self.save_pickle_impl()
        else:
            print(f'[INFO][{MODNAME}] no need to save')


    def test(self, v: int):
        ''' test '''
        (p, q) = self.bisect_between_idx(v)
        if p is None:
            print('\tno answer for this')
            return
        show(v, self.at(p), self.at(q))



if __name__ == '__main__':
    print('run **run_example.py** to see the demo...')
