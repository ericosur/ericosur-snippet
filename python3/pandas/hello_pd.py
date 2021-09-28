#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' try pandas '''

from __future__ import print_function
import pandas as pd

def main():
    ''' main '''
    print(f"pd.__version__: {pd.__version__}")

    print('[WARN] This is not a current updated rates!!!')
    FILEN = 'rates.csv'
    # read csv file as dataframe
    rates = pd.read_csv(FILEN)

    # CR: currency
    #CR = '幣別'
    # CN: column name
    CN = '賣出'

    # filter values from this column
    mask1 = (rates[CN] > 30.0)
    mask2 = (rates[CN] < 1.0)
    t = rates[mask1 | mask2]
    print(f'apply mask1 | mask2 ===>\n{t}')

    mask3 = (rates['CName'].isin(['USD', 'GBP', 'EUR']))
    t = rates[mask3]
    print(f'apply mask3 ===>\n{t}')

if __name__ == '__main__':
    main()
