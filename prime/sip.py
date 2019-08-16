#!/usr/bin/python3
# coding: utf-8

'''
table: prime_1M.txt (with 1 million primes)
will load/save it as pickle format (need compress_pickle)

given cli argument to get lower/upper prime

pip install compress_pickle

'''

import compress_pickle
from store_prime import StorePrime

# pylint: disable=invalid-name

class LoadCompressPrime(StorePrime):
    '''
    this class inherits from StorePrime and overrides load_pickle() and
    save_pickle(), which are using "compress_pickle" to load/save pickle data
    '''
    def __init__(self, txtfn='prime_1M.txt', pfn='primes.p.lzma'):
        super().__init__(txtfn, pfn)
        #print('__init__')

    def __str__(self):
        if self.pvalues is None:
            self.init_size = 0
        else:
            self.init_size = len(self.pvalues)
        msg = "LoadCompressPrime: "
        msg = msg + 'min: {} '.format(self.pvalues[0])
        msg = msg + 'max: {} '.format(self.pvalues[-1])
        msg = msg + 'total primes: {}'.format(self.init_size)
        return msg

    def load_pickle_impl(self):
        ''' overrides StorePrime::load_pickle_impl() '''
        #self.pvalues = compress_pickle.load(self.pfile, compression="lzma")
        self.pvalues = compress_pickle.load(self.pfile)
        self.need_save = False
        print('load_pickle_impl pvalues:', self.pfile)
        return True

    def save_pickle_impl(self):
        '''
        save pvalues into pickle file
        overrides class StorePrime::save_pickle_impl()
        '''
        #compress_pickle.dump(self.pvalues, self.pfile, compression="lzma")
        compress_pickle.dump(self.pvalues, self.pfile)



if __name__ == '__main__':
    print('run **test_sp.py sip** to see the demo...')
