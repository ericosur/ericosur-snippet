#!/usr/bin/env python3
# coding: utf-8
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
load prime numbers from table and output to a xlsx file
'''

import sys
import sympy

XLSWRITER_OK = False
try:
    import xlsxwriter
    XLSWRITER_OK = True
except ImportError:
    print('cannot import module xlsxwriter, WILL NOT output to xlsx file')

sys.path.insert(0, '../')
from store import GetConfig

USE_LCP = False
try:
    # larger and slower for loading pickle
    from store import LoadCompressPrime as StorePrime
    USE_LCP = True
    print(f'[INFO] {__file__}: use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker for loading pickle
    from store import StorePrime
    print(f'[INFO] {__file__}: use **store_prime**')


def get_smallconfig():
    ''' return small txt path '''
    obj = GetConfig()
    obj.set_configkey("small")
    txtfn = obj.get_full_path("txt")
    if USE_LCP:
        pfn = obj.get_full_path("compress_pickle")
    else:
        pfn = obj.get_full_path("pickle")
    return txtfn, pfn


class Solution():
    ''' test date is a prime '''
    def __init__(self, upper=1000):
        self.islcp = False
        self.sp = None
        self._getobj()
        self.arr = None
        self._upper = upper

    def _getobj(self):
        ''' get prime storage class '''
        # try to import StorePrime class
        txtfn, pfn = get_smallconfig()
        self.sp = StorePrime(txtfn=txtfn, pfn=pfn)
        self.sp.get_ready()

    @property
    def upper(self) -> int:
        ''' getter '''
        return self._upper
    @upper.setter
    def upper(self, val: int):
        ''' setter'''
        self._upper = val

    def _check(self):
        ''' check '''
        if not self.arr:
            print(f'[INFO] {__file__}: arr is empty')
            sys.exit(1)

    def output(self):
        ''' show result of list '''
        self._check()
        #print('size of arr:', len(self.arr))
        # for ii in arr:
        #     print(f'{ii:8d}', end='')
        # print()

    def output_xls(self):
        ''' output data to xls '''
        self._check()
        fn = 'smallprimes.xlsx'
        wb = xlsxwriter.Workbook(fn)
        # font: Calibri, Consolas
        cell_format = wb.add_format({'font_name': 'Calibri Light', 'font_size': 12})
        ws = wb.add_worksheet('small primes')
        ws.set_column('A:AZ', 6.4) # width of column
        max_item_one_row = 50
        for i, d in enumerate(self.arr):
            ws.write(i%max_item_one_row, i//max_item_one_row, d, cell_format)
        wb.close()
        print(f'[INFO] output to {fn}')

    def action(self):
        ''' action '''
        self.arr = self.sp.get_primes_less_than(self.upper)
        if not self.arr:
            print('[WARN] no result...')
            return

        # double confirm
        prime_n = sympy.ntheory.generate.primepi(self.upper)
        assert prime_n == len(self.arr)

        print(f'[INFO] There are {prime_n} primes under {self.upper}')
        self.output()
        if XLSWRITER_OK:
            self.output_xls()

    def test(self):
        ''' test '''
        for n in [10, 100, 1000, 10000]:
            self.arr = self.sp.get_primes_less_than(n)
            #print(self.arr)
            prime_n = sympy.ntheory.generate.primepi(n)
            #print(type(prime_n))
            #print(f'arr:{len(self.arr):6d} vs sympy:{int(prime_n):6d}'))
            assert len(self.arr) == prime_n

    @classmethod
    def run(cls, upper):
        ''' run me '''
        obj = cls(upper)
        obj.action()

def main():
    ''' main '''
    Solution.run(10000)

if __name__ == '__main__':
    main()
