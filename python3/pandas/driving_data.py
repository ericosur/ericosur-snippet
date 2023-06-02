#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
read driving data table (at google drive) and calculate stastics
(or read it from csv file offline)
'''

import argparse
import os
import sys
from math import floor
from datetime import date
import numpy as np
try:
    import pandas as pd
except ImportError:
    print('[ERROR] cannot import module pandas...')
    sys.exit(1)

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile, query_url_for_data
from strutil import print_sep, str2sec, sec2mmss

class DrivingData():
    ''' fetch driving data from gdrive or local csv '''
    def __init__(self):
        self.debug = False
        self.jsonpath = ''
        self.jsondata = None
        self.csvfile = ''
        self.docid = ''
        self.sheetid = ''
        self.url = ''

    def set_csvfile(self, csvfile):
        ''' setter csvfile '''
        if csvfile is None:
            self.csvfile = '/tmp/__driving_datasheet__.csv'
        else:
            self.csvfile = csvfile

    def read_setting(self, conf_file):
        ''' read setting '''
        if self.debug:
            print('read_setting()')

        if conf_file is None:
            home = os.getenv('HOME')
            self.jsonpath = home + '/Private/driving_data.json'
        else:
            self.jsonpath = conf_file
        if not os.path.exists(self.jsonpath):
            print('[ERROR] setting file not found', self.jsonpath)
            sys.exit(1)
        self.jsondata = read_jsonfile(self.jsonpath)
        self.docid = self.jsondata.get('docid', '')
        self.sheetid = self.jsondata.get('sheetid', '')
        self.compose_url()

    def compose_url(self):
        ''' compose url '''
        part1 = 'https://docs.google.com/spreadsheets/d/'
        part2 = '/gviz/tq?tqx=out:csv&sheet='
        self.url = part1 + self.docid + part2 + self.sheetid
        # if self.debug:
        #     print('url:', self.url)

    def dump_setting(self):
        ''' dump settings '''
        print('dump settings =====>')
        print('jsonpath:', self.jsonpath)
        print('docid:', self.docid)
        print('sheetid', self.sheetid)
        print('url:', self.url)
        print('====================')

    def request_data(self):
        ''' request data '''
        if self.debug:
            print('request_data()')
        csvdata = query_url_for_data(self.url)
        #print('csvdata: ', csvdata)
        if not self.csvfile:
            print('[ERROR] MUST specify csvfile path before calling request_data()')
            sys.exit(1)
        with open(self.csvfile, 'wb') as ofile:
            ofile.write(csvdata)
            if self.debug:
                print(f'output csv to {self.csvfile}')

    @staticmethod
    def str2date(s):
        ''' date string to date object
            [in] 2020-01-01
        '''
        arr = s.split('-')
        try:
            vals = [int(x) for x in arr]
        except ValueError:
            print('[ERROR] str2date: invalid string to integer')
            return None
        return date(vals[0], vals[1], vals[2])

    @staticmethod
    def get_between_dates(start, end):
        ''' get dates between
            [in] str start date 2020-01-01
            [out] str end date 2020-02-29
        '''
        start_date = DrivingData.str2date(start)
        end_date = DrivingData.str2date(end)
        between = end_date - start_date
        #print(type(between), repr(between))
        return between

    def extra_data(self, d0, d1):
        ''' show extra data info '''
        print(f'[INFO]    first date: {d0}')
        print(f'[INFO]     last date: {d1}')
        print(f'[INFO] dates between: {DrivingData.get_between_dates(d0, d1)}')
        print('[INFO] for 2021, total working days are 239')
        print('[INFO] for 2022, total working days are 242')

    def action(self):
        ''' main function '''
        #print("pd.__version__: {}".format(pd.__version__))

        # read csv file as dataframe
        data = pd.read_csv(self.csvfile)
        duration = data['duration']

        dates = []
        secs = []
        for ii, ds in enumerate(data['date']):
            try:
                v = duration[ii]
                if isinstance(v, float):
                    # data exists at col "date", but empty at col "duration"
                    #print('float?')
                    break
                dates.append(ds)
                secs.append(str2sec(v))
            except ValueError:
                print(f'[ERROR] at {ii} on {ds}, invalid format: {duration[ii]}')
                return

        self.extra_data(dates[0], dates[-1])

        if len(dates) != len(secs):
            print(f'[ERROR] not the same length {len(dates)} vs {len(secs)}')
            return

        ndict = {"date": dates, "seconds": secs}
        res = pd.DataFrame(ndict)

        des = res.describe()
        if self.debug:
            print_sep()
            print('item', des)
        print_sep()
        self.show_details(des)

    @staticmethod
    def show_details(des):
        ''' show details of res² '''
        queries = ['count', 'max', '75%', 'mean', '50%', '25%', 'min', 'std']
        for qq in queries:
            ans = peek_target(des, qq)
            if qq == 'count':
                result = str(int(floor(ans)))
                j = result.rjust(10, ' ')
            else:
                mmss = sec2mmss(ans)
                result = f'{mmss}  ({ans:4d})'
                j = result.rjust(20, ' ')
            print(f'{qq:10s}: {j:20s}')

# return type: numpy.float64
def peek_target(desc_table, target):
    ''' peek target '''
    #print('desc_table:', desc_table)
    desc_list = desc_table.index.tolist()
    try:
        midx = desc_list.index(target)
        mean_value = desc_table.iloc[midx, 0]
        #result = sec2str(mean_value)
        result = np.int64(mean_value)
        #print('result:{}, type:{}'.format(result, type(result)))
        return result
    except ValueError as e:
        print(f'WARN: ValueError: {e.args}')
    return ''

def process_remotefile(out_file=None, conf_file=None):
    ''' request from google drive '''
    dd = DrivingData()
    print('[INFO] request data from google drive...')
    dd.set_csvfile(out_file)
    dd.read_setting(conf_file)
    if dd.debug:
        dd.dump_setting()
    dd.request_data()
    dd.action()

def process_localfile(in_file):
    ''' use local datasheet '''
    print('input file from:', in_file)
    print_sep()
    dd = DrivingData()
    dd.set_csvfile(in_file)
    dd.action()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='parsing driving data at google drive')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument('-i', '--input', help='Specify local datasheet, '
                        'will ignore output and config files')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-c', '--conf', help='Specify config for google drive (json format)')
    parser.add_argument("-r", "--run", action='store_true', default=False,
        help='Specify this parameter to run actually')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')

    #parser.parse_args(['-i input.csv -o out.csv'])
    args = parser.parse_args()

    if args.run:
        if args.input:
            process_localfile(args.input)
        else:
            process_remotefile(out_file=args.output, conf_file=args.conf)
        return

    print('[INFO] show parameters only...')
    has_parameter = False
    if args.input:
        print('input:', args.input)
        has_parameter = True
    if args.output:
        print('output:', args.output)
        has_parameter = True
    if args.conf:
        print('conf:', args.conf)
        has_parameter = True

    # to show help message directly
    if has_parameter is False:
        parser.print_help()

if __name__ == '__main__':
    main()
