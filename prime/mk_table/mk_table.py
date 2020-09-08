#!/usr/bin/env python3
# coding: utf-8

'''
load prime numbers from table and output to a xlsx file
'''

import sys
import sympy

sys.path.insert(0, '../')

# try to import StorePrime class
try:
    # larger and slower for loading pickle
    from sip import LoadCompressPrime as StorePrime
    print('mk_table: use **LoadCompressPrime**')
except ImportError:
    # smaller and quicker for loading pickle
    from store_prime import StorePrime
    print('mk_table: use **store_prime**')

XLSWRITER_OK = False
try:
    import xlsxwriter
    XLSWRITER_OK = True
except ImportError:
    print('cannot import module xlsxwriter, WILL NOT output to xlsx file')

# pylint: disable=invalid-name
class Solution():
    ''' test date is a prime '''
    def __init__(self, upper=1000):
        self.sp = StorePrime(txtfn='../small.txt')
        if not self.sp.load_pickle():
            print('mk_table: load_pickle() failed')
            sys.exit(1)
        self.arr = list()
        self.upper = upper

    def _check(self):
        ''' check '''
        if not self.arr:
            print('mk_table: arr is empty')
            sys.exit(1)

    def output(self):
        ''' show result of list '''
        self._check()
        #print('size of arr:', len(self.arr))
        # for ii in arr:
        #     print('{:8d}'.format(ii), end='')
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
        print('output to {}'.format(fn))

    def run(self):
        ''' run '''
        self.arr = self.sp.get_primes_less_than(self.upper)

        # double confirm
        prime_n = sympy.ntheory.generate.primepi(self.upper)
        assert prime_n == len(self.arr)

        print('[INFO] There are {} primes under {}'.format(prime_n, self.upper))
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
            #print('arr:{:6d} vs sympy:{:6d}'.format(len(self.arr), int(prime_n)))
            assert len(self.arr) == prime_n

def main():
    ''' main '''
    s = Solution(10000)
    # s.test()
    s.run()

if __name__ == '__main__':
    main()
