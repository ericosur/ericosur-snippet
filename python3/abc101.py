#!/usr/bin/env python3
# coding: utf-8

'''
sns example

https://medium.com/%E6%95%B8%E6%93%9A%E4%B8%8D%E6%AD%A2-not-only-data
/%E6%B7%B1%E5%85%A5%E6%B7%BA%E5%87%BA-python-
%E8%A6%96%E8%A6%BA%E5%8C%96%E5%A5%97%E4%BB%B6-matplotlib-seaborn-
%E6%A0%B8%E5%BF%83%E6%8C%87%E5%8D%97%E8%88%87%E7%B9%AA%E8%A3%BD-44a47458912

https://seaborn.pydata.org/tutorial/relational.html
'''

#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
# pylint: disable=import-error
import seaborn as sns  # type: ignore[import]

sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)

plt.show()
