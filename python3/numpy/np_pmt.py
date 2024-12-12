#!/usr/bin/env python3
#coding: utf-8

'''
numpy_financial.pmt

https://numpy.org/numpy-financial/latest/index.html#functions
'''

import sys
import numpy_financial as npf
sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from myutil import prt

def main():
    ''' main '''
    # Parameters:
    rate = 2.2/100  # Annual interest rate
    nper = 16*12  # Number of payments (16 years, total 16*12 months)
    pv = 2_000_000  # Present value (loan amount)

    prt(f'rate: {rate*100:.4}%')
    prt(f'{nper=}')
    prt(f'{pv=}')
    # Calculate the monthly payment
    payment = npf.pmt(rate/12, nper, pv)
    prt(f'monthly payment: {payment:.2f}')

if __name__ == "__main__":
    main()
