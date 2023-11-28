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
sys.path.insert(0, "..")

from myutil import read_jsonfile, query_url_for_data
from strutil import print_sep, str2sec, sec2mmss

class DrivingData():
    ''' fetch driving data from gdrive or local csv '''
    debug = False
    simpleout = False
    default_fn = 'driving_data.json'
    tmp_csv = '/tmp/__driving_datasheet__.csv'

    def __init__(self):
        self.jsonpath = ''
        self.jsondata = None
        self.csvfile = ''
        self.docid = ''
        self.sheetid = ''
        self.url = ''

    def set_csvfile(self, csvfile):
        ''' setter csvfile '''
        if csvfile:
            self.csvfile = csvfile
        else:
            self.csvfile = DrivingData.tmp_csv

    def set_simpleout(self, simpleout):
        ''' simple out '''
        self.simpleout = simpleout

    def get_default_config(self):
        ''' search config file in default paths '''
        home = os.getenv('HOME')
        dfn = DrivingData.default_fn
        paths = []
        # 1. home/Private/
        tmp = os.path.join(home, 'Private', dfn)
        paths.append(tmp)
        # 2. home
        tmp = os.path.join(home, dfn)
        paths.append(tmp)
        # 3. local
        tmp = os.path.join('./', dfn)
        paths.append(tmp)
        for q in paths:
            if os.path.exists(q):
                return q
        return None

    def read_setting(self, conf_file):
        ''' read setting '''
        if self.debug:
            print('read_setting()')

        if conf_file:
            self.jsonpath = conf_file
        else:
            self.jsonpath = self.get_default_config()
        if self.jsonpath is None or not os.path.exists(self.jsonpath):
            print('[ERROR] no config is specified, exit...')
            sys.exit(1)
        print(f'[INFO] using config: {self.jsonpath}')

        self.jsondata = read_jsonfile(self.jsonpath)
        self.docid = self.jsondata.get('docid', '')
        self.sheetid = self.jsondata.get('sheetid', '')
        self.compose_url()
        if self.debug:
            self.dump_setting()

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
    def get_between_dates(start, end) -> str:
        ''' get dates between
            [in] str start date 2020-01-01
            [out] str end date 2020-02-29
        '''
        start_date = DrivingData.str2date(start)
        end_date = DrivingData.str2date(end)
        ddiff = end_date - start_date
        return str(ddiff.days)

    def extra_data(self, d0, d1):
        ''' show extra data info '''
        print(f'[INFO]    first date: {d0}')
        print(f'[INFO]     last date: {d1}')
        print(f'[INFO]   during days: {DrivingData.get_between_dates(d0, d1)}')
        print('[INFO] for 2021, total working days are 239')
        print('[INFO] for 2022, total working days are 242')
        print('[INFO] for 2023, total working days are 241')

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
        if not self.simpleout:
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

        self.show_details(des)

    def show_details(self, des):
        ''' show details of res² '''
        queries = ['count', 'max', '75%', 'mean', '50%', '25%', 'min', 'std']
        print_sep()
        if self.simpleout:
            print(date.today())
        for qq in queries:
            ans = peek_target(des, qq)
            if qq == 'count':
                result = str(int(floor(ans)))
                if self.simpleout:
                    j = f'"{result}"'
                else:
                    j = result.rjust(10, ' ')
            else:
                mmss = sec2mmss(ans)
                if self.simpleout:
                    j = f'"{mmss}"'
                else:
                    result = f'{mmss}  ({ans:4d})'
                    j = result.rjust(20, ' ')
            if self.simpleout:
                print(j)
            else:
                print(f'{qq:10s}: {j:20s}')
        print_sep()

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


def perform_show_driving_data(in_file=None, out_file=None, conf_file=None, simpleout=False):
    ''' universal starter '''
    obj = DrivingData()
    obj.set_simpleout(simpleout)

    # use local file (higher priority), no need out_file and conf_file
    if in_file:
        print('[INFO] input file from:', in_file)
        obj.set_csvfile(in_file)
    else:   # request remote file
        print('[INFO] request data from google drive...')
        obj.set_csvfile(out_file)
        obj.read_setting(conf_file)
        obj.request_data()

    obj.action()

def show_parameters(parser):
    ''' show parameters content '''
    print('[INFO] show parameters only, add **-r** to real run, dump...\n')
    args = parser.parse_args()
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
    if args.excel:
        print('excel:', args.excel)
        has_parameter = True

    # to show help message directly
    if has_parameter is False:
        parser.print_help()


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
    parser.add_argument("-x", "--excel", action='store_true', default=False,
        help='just print data, easy to paste to spreadsheets')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')

    #parser.parse_args(['-i input.csv -o out.csv'])
    args = parser.parse_args()

    if not args.run:
        show_parameters(parser)
        return

    perform_show_driving_data(in_file=args.input, out_file=args.output,
        conf_file=args.conf, simpleout=args.excel)



if __name__ == '__main__':
    main()
