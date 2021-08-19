#!/usr/bin/env python3.6
# coding: utf-8

''' read ods practice '''

import argparse
from pandas_ods_reader import read_ods
import pandas as pd

# pylint: disable=invalid-name
# pylint: disable=abstract-class-instantiated

class Solution():
    ''' class to process ods file and output into xlsx file '''

    classes = ['Supers', 'Sports', 'SUVs', 'Sports Classics', 'Off-Road', 'Muscle']

    def __init__(self, input_file, output_file):
        self.fn = input_file
        self.ofn = output_file
        self.df_lap = None
        self.df_key = None
        self.df_first20 = None
        self._readfile()

    def _readfile(self):
        ''' _readfile '''
        # load specific sheet, and remove first two rows
        sheet_name = 'By Class (Lap Time)'
        tmp = read_ods(self.fn, sheet_name, columns=["overall", "rank", "class", "vehicle"])
        self.df_lap = tmp.drop([0,1])

        # load specific sheet, and remove some columns, and rows
        sheet_name = 'Key Vehicle Info'
        tmp = read_ods(self.fn, sheet_name, columns=['classA','name','C','D',
            'Manufacturer','F','G','H','I','J','K','Retailer','Price',
            'N','O','P','Q','R','Date','Year','DLC'])
        tmp.drop(columns=['C','D','F','G','H','I','J','K','N','O','P','Q','R'],
                inplace=True)
        self.df_key = tmp.drop(index=[0, 1])

    def _category(self):
        ''' show category '''

        #print(self.df_lap.head())
        # supers = t1['class'].isin(['Supers'])
        # res = t1[supers]
        # print(res)

        # some new vehicles has no overall data
        m0 = self.df_lap['overall'].notnull()
        m1 = self.df_lap['rank'] <= 20
        t1 = self.df_lap[m0 & m1]

        q = t1['class'].isin(self.classes)
        self.df_first20 = t1[q]
        #print(self.df_first20.shape)

    def _mixup(self):
        ''' mixup '''
        #cars = self.df_first20['vehicle']
        df1 = self.df_first20
        df2 = self.df_key

        res = pd.DataFrame(columns=["overall", "rank", "class", "vehicle",
                            "classA", "name", "Manufacturer", "Retailer", "Price", "Date",
                            "Year", "DLC"])
        #print(res)
        #print(df1.shape)

        for ii in range(df1.shape[0]):
            name = df1.iloc[ii, 3]  # name of vehicle

            s1 = df1.iloc[ii]   # current row (type: pandas.Series)
            q = df2['name'].eq(name) # query it in "key info" table
            s2 = df2[q].iloc[0] # the row contains the same vehicle name (type: pandas.Series)
            combined_series = pd.concat([s1, s2])

            res = res.append(combined_series, ignore_index=True)

        res.drop(columns=['classA', 'vehicle'], inplace=True)
        #print(res)
        self._write_file(res)

    def _write_file(self, df):
        ''' output the dataframe to file '''
        #print('save file to:', self.ofn)
        print('size: ', df.shape)
        with pd.ExcelWriter(self.ofn) as writer:
            df.to_excel(writer, sheet_name='merged')
            #res.to_excel(writer, sheet_name='keyinfo')
            #self.df_first20.to_excel(writer, sheet_name='rank')

    def run(self):
        ''' run this function '''
        self._category()
        self._mixup()


def process(inp, outp):
    ''' process '''
    proc = Solution(inp, outp)
    proc.run()


def main():
    ''' main '''
    desc = '''
    fetch necessary data from GTA vehicle data sheet,
    input ODS format, output XLSX format
    '''
    # exit_on_error=False (after py3.9)
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument("strings", metavar='str', type=str, nargs='*',
    #     help="show these strings")
    parser.add_argument('-o', '--output', help='Output file name', default='out.xlsx')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

    args = parser.parse_args()
    print(args)

    if args.input:
        print('input:', args.input)
    if args.output:
        print('output:', args.output)

    process(args.input, args.output)

if __name__ == '__main__':
    main()
