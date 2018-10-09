#!/usr/bin/env python2

'''
    try pandas
    example from: http://bit.ly/2oKsLDB
'''

import pandas as pd

df = pd.read_csv('perfect_s.csv')
print(df)

dfs = pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
print(dfs[0])
