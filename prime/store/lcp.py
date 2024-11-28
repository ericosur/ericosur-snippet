#!/usr/bin/env python3
# coding: utf-8

'''
table: small.txt / big.txt / large.txt
will load/save it as pickle format

given cli argument to get lower/upper prime

requires: compress_pickle
pip install compress_pickle

'''

from time import time

try:
    import compress_pickle
except ImportError as err:
    print(f'[FAIL] {__file__}: cannot load module **compress_pickle**')
    raise ImportError(f"[FAIL] {__file__} cannot load module") from err

from .store_prime import StorePrime

# pylint: disable=invalid-name

MODNAME = "lcp.py"
__VERSION__ = "2024.03.27"

class LoadCompressPrime(StorePrime):
    '''
    this class inherits from StorePrime and overrides load_pickle() and
    save_pickle(), which are using "compress_pickle" to load/save pickle data
    '''

    tag = 'LoadCompressPrime'

    def __init__(self, txtfn="small.txt", pfn="small.p.lzma",
                debug=False, verbose=False):
        super().__init__(txtfn, pfn, debug, verbose)
        self.logd('__init__()', tag=self.tag)

    def load_pickle_impl(self):
        ''' overrides StorePrime::load_pickle_impl() '''
        self.logd('enter load_pickle_impl()...', tag=self.tag)
        start = time()
        super().try_pickle_file()
        self.primes = compress_pickle.load(self.config["pfn"])
        self.need_save = False

        self.logv(f'{self.tag}: primes from:', self.config["pfn"])
        duration = time() - start
        self.logv(f'{self.tag}: duration: {duration:.3f} sec')
        return True

    def save_pickle_impl(self):
        '''
        save primes into pickle file
        overrides class StorePrime::save_pickle_impl()
        '''
        self.logd('enter save_pickle_impl()...', tag=self.tag)
        #compress_pickle.dump(self.primes, self.pfile, compression="lzma")
        compress_pickle.dump(self.primes, self.config["pfn"])
        self.logv(f'{self.tag}: save pickle as {self.config["pfn"]}')

if __name__ == '__main__':
    print('run **run_example.py --lcp** to see the demo of this implementation...')
