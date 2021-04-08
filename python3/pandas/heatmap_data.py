#!/usr/bin/python3.6
# coding: utf-8

'''
brief description for this script
reference: https://pythonbasics.org/seaborn-heatmap/#heatmap-data
'''

import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
import seaborn as sns

def test():
    ''' test '''
    sns.set()
    flights = sns.load_dataset("flights")
    flights = flights.pivot("month", "year", "passengers")
    _ = sns.heatmap(flights)
    plt.show()


def main():
    ''' main '''
    test()

if __name__ == '__main__':
    main()
