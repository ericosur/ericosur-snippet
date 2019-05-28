#!/usr/bin/env python3
# coding: utf-8

'''
    try pandas
    example from: http://bit.ly/2oKsLDB
'''

import pandas as pd

arr = [['Movies', 46], ['Sports', 8],
       ['Coding', 12], ['Fishing', 12],
       ['Dancing', 6], ['Cooking', 8]]

df = pd.DataFrame(arr, columns=["name","num"])
print(df)
print("==> df.head {}".format(df.columns))
