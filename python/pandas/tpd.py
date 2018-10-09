#!/usr/bin/env python2

''' try dataframe '''

from __future__ import print_function
import pandas as pd


FILEN = 'perfect_s.csv'

df = pd.read_csv(FILEN)
select_df = pd.DataFrame(df)
print('shape:', select_df.shape)
print('describe:\n', select_df.describe())
print('info:\n', select_df.info())
