#!/usr/bin/python3
# coding: utf-8

'''
table: small.txt / big.txt / large.txt
will load/save it as pickle format

given cli argument to get lower/upper prime

requires: compress_pickle
pip install compress_pickle

'''

import sys
from time import time

try:
    import compress_pickle
except ImportError:
    print('cannot load module **compress_pickle**')
    sys.exit(0)

from store_prime import StorePrime

# pylint: disable=invalid-name

class LoadCompressPrime(StorePrime):
    '''
    this class inherits from StorePrime and overrides load_pickle() and
    save_pickle(), which are using "compress_pickle" to load/save pickle data
    '''
    def __init__(self, txtfn='large.txt', pfn='large.p.lzma'):
        super().__init__(txtfn, pfn)
        #print('__init__')

    def __str__(self):
        if self.pvalues is None:
            self.init_size = 0
        else:
            self.init_size = len(self.pvalues)
        msg = "LoadCompressPrime: "
        msg = msg + f'min: {self.pvalues[0]} '
        msg = msg + f'max: {self.pvalues[-1]} '
        msg = msg + f'total primes: {self.init_size}'
        return msg

    def load_pickle_impl(self):
        ''' overrides StorePrime::load_pickle_impl() '''
        start = time()
        #self.pvalues = compress_pickle.load(self.pfile, compression="lzma")
        super()._try_pickle_file()
        self.pvalues = compress_pickle.load(self.pfile)
        self.need_save = False
        print('load_pickle_impl pvalues from:', self.pfile)
        duration = time() - start
        print(f'load_pickle_impl duration: {duration:.3f} sec')
        return True

    def save_pickle_impl(self):
        '''
        save pvalues into pickle file
        overrides class StorePrime::save_pickle_impl()
        '''
        #compress_pickle.dump(self.pvalues, self.pfile, compression="lzma")
        compress_pickle.dump(self.pvalues, self.pfile)

if __name__ == '__main__':
    print('run **run_example.py -l** to see the demo of this implementation...')
