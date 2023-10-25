#!/usr/bin/python3
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

from store_prime import StorePrime

# pylint: disable=invalid-name

MODNAME = "lcp.py"

class LoadCompressPrime(StorePrime):
    '''
    this class inherits from StorePrime and overrides load_pickle() and
    save_pickle(), which are using "compress_pickle" to load/save pickle data
    '''
    def __init__(self, txtfn="small.txt", pfn="small.p.lzma"):
        super().__init__(txtfn, pfn)
        #print('__init__')

    def __str__(self):
        if self.pvalues is None:
            self.init_size = 0
        else:
            self.init_size = len(self.pvalues)

        msg = f'''
{MODNAME}: min: {self.pvalues[0]} max: {self.pvalues[-1]:,} total primes: {self.init_size:,}
'''
        msg = msg.strip()
        return msg

    def load_pickle_impl(self):
        ''' overrides StorePrime::load_pickle_impl() '''
        start = time()
        super()._try_pickle_file()
        self.pvalues = compress_pickle.load(self.pfn)
        self.need_save = False
        print(f'{MODNAME}: pvalues from:', self.pfn)
        duration = time() - start
        print(f'{MODNAME}: duration: {duration:.3f} sec')
        return True

    def save_pickle_impl(self):
        '''
        save pvalues into pickle file
        overrides class StorePrime::save_pickle_impl()
        '''
        #compress_pickle.dump(self.pvalues, self.pfile, compression="lzma")
        compress_pickle.dump(self.pvalues, self.pfn)
        print(f'[INFO] {MODNAME} save pickle as {self.pfn}')

if __name__ == '__main__':
    print('run **run_example.py --lcp** to see the demo of this implementation...')
