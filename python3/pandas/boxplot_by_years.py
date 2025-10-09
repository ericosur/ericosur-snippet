#!/usr/bin/env python3
# coding: utf-8

''' draw boxplot from by_years.csv
    no need to calculate statistics (Q1,Q2,Q3...), just give raw data
    the format of by_years.csv:
year,seconds
2018,3255.96
2018,3129.26
2018,2809.03
    ...
'''

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
try:
    from rich.console import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print

class Solution():
    ''' solution class '''
    alldata_csv = 'by_dates.csv'

    def __init__(self):
        ''' init '''
        self.df = None
        self.__readdata__()

    def __readdata__(self):
        ''' read data '''
        if not os.path.isfile(Solution.alldata_csv):
            logd(f'[FAIL] need data file: {Solution.alldata_csv}')
            logd('[info] use driving_data.py --years --run to generate it')
            sys.exit(1)
        self.df = pd.read_csv('by_dates.csv', parse_dates=["date"])

    def draw_boxplot(self):
        ''' draw boxplot '''
        df = self.df.copy()
        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Extract year from date
        df['year'] = df['date'].dt.year

        # Group by year and plot boxplot for 'seconds'
        df.boxplot(column='seconds', by='year', grid=False)
        plt.title('Driving Duration by Year')
        plt.suptitle('')  # Remove default subtitle
        plt.xlabel('Year')
        plt.ylabel('Seconds')
        plt.show()


    def action(self):
        ''' action '''
        self.draw_boxplot()


if __name__ == "__main__":
    solution = Solution()
    solution.action()
