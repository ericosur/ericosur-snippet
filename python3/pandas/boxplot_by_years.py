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

import pandas as pd
import matplotlib.pyplot as plt

def draw_boxplot():
    ''' draw boxplot '''
    # Read the CSV file
    df = pd.read_csv('by_years.csv')

    # Draw boxplot: group by 'year', plot 'seconds'
    df.boxplot(column='seconds', by='year', grid=False)
    plt.title('Boxplot of Commute Driving Times by Year')
    plt.suptitle('')  # Remove the default subtitle
    plt.xlabel('Year')
    plt.ylabel('Seconds')
    plt.show()

def main():
    ''' main function '''
    draw_boxplot()

if __name__ == "__main__":
    main()
