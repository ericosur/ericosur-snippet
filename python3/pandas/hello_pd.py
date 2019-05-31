#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' try pandas '''

from __future__ import print_function
import pandas as pd

def main():
    ''' main '''
    print("pd.__version__: {}".format(pd.__version__))
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
    print('apply mask1 | mask2 ===>\n{}'.format(rates[mask1 | mask2]))

    mask3 = (rates['CName'].isin(['USD', 'GBP', 'EUR']))
    print('apply mask3 ===>\n{}'.format(rates[mask3]))

if __name__ == '__main__':
    main()
