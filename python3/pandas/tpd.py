#!/usr/bin/env python3

''' use dataframe of pandas to read csv file '''

from __future__ import print_function

import os

from perfect_square import gen_csv

import pandas as pd


def main():
    ''' main '''
    FILEN = 'perfect_s.csv'

    if not os.path.isfile(FILEN):
        print('[INFO] file not found, call perfect_square to generate:', FILEN)
        gen_csv(FILEN)

    df = pd.read_csv(FILEN)
    select_df = pd.DataFrame(df)
    print('shape:', select_df.shape)
    print('describe:\n', select_df.describe())
    print('info:\n', select_df.info())


if __name__ == '__main__':
    main()
