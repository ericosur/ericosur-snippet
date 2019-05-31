#!/usr/bin/env python3

'''
    try pandas
    example from: http://bit.ly/2oKsLDB
'''

import os
import pandas as pd
from perfect_square import gen_csv

def main():
    ''' main '''
    fn = 'perfect_s.csv'
    if not os.path.isfile(fn):
        gen_csv(fn)

    df = pd.read_csv(fn)
    print(df)

    dfs = pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
    print(dfs[0])

if __name__ == '__main__':
    main()
