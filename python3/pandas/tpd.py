#!/usr/bin/env python3

''' try dataframe '''

from __future__ import print_function
import os
import pandas as pd

def main():
    ''' main '''
    FILEN = 'perfect_s.csv'

    if not os.path.isfile(FILEN):
        from perfect_square import gen_csv
        gen_csv(FILEN)

    df = pd.read_csv(FILEN)
    select_df = pd.DataFrame(df)
    print('shape:', select_df.shape)
    print('describe:\n', select_df.describe())
    print('info:\n', select_df.info())


if __name__ == '__main__':
    main()
