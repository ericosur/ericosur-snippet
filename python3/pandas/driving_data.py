#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=import-error
# pylint: disable=wrong-import-order
# pylint: disable=wrong-import-position

'''
read driving data table (at google drive) and calculate stastics
(or read it from csv file offline)
'''

import argparse
import os
import sys
from datetime import date
from math import floor

import numpy as np

try:
    import pandas as pd
except ImportError:
    print('[ERROR] cannot import module pandas...')
    sys.exit(1)

# HOME = os.getenv('HOME')
# UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
# if os.path.exists(UTILPATH):
#     sys.path.insert(0, UTILPATH)
sys.path.insert(0, "..")

from myutil import query_url_for_data, read_jsonfile
from strutil import print_sep, sec2mmss, str2sec
from working_days import LoadWorkingDays

TMP_CSV = '/tmp/__driving_datasheet__.csv'

class DriveConfig():
    ''' class helps to read config '''

    DEFAULT_FN = 'driving_data.json'
    debug = False

    def __init__(self):
        self.jsonpath = None
        self.data = None
        self.url = None

    @staticmethod
    def get_default_config():
        ''' search config file in default paths '''
        home = os.getenv('HOME')
        dfn = DriveConfig.DEFAULT_FN
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

    def compose_url(self):
        ''' compose url '''
        part1 = 'https://docs.google.com/spreadsheets/d/'
        part2 = '/gviz/tq?tqx=out:csv&sheet='
        if self.data is None:
            raise ValueError
        docid = self.data.get('docid', '')
        sheetid = self.data.get('sheetid', '')
        url = part1 + docid + part2 + sheetid
        if self.debug:
            print(f'url: {url}')
        self.url = url
        return url

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

        self.data = read_jsonfile(self.jsonpath)
        self.compose_url()

        if self.debug:
            self.dump_setting()
        return self.data

    def get_data(self):
        ''' get data '''
        return self.data

    def get_url(self):
        ''' get url '''
        return self.url

    def dump_setting(self):
        ''' dump settings '''
        print('dump class DriveConfig:')
        print('jsonpath:', self.jsonpath)
        print(f'{self.data=}')
        print(f'{self.url=}')


class DrivingData():
    ''' fetch driving data from gdrive or local csv '''
    debug = False
    simpleout = False
    verbose = False

    def __init__(self):
        self.csvfile = ''
        self.url = ''
        self.outputs = {}
        (self.mu, self.sigma) = (0, 0)

    def set_csvfile(self, csvfile):
        ''' setter csvfile '''
        if csvfile:
            self.csvfile = csvfile
        else:
            self.csvfile = TMP_CSV

    def set_simpleout(self, simpleout):
        ''' simple out '''
        self.simpleout = simpleout

    def set_verbose(self, verbose):
        ''' verbose or not '''
        self.verbose = verbose

    def read_setting(self, conf_file):
        ''' read settings '''
        dc = DriveConfig()
        dc.read_setting(conf_file)
        self.url = dc.get_url()
        if self.debug:
            dc.dump_setting()

    def request_data(self):
        ''' request data and output to a csv file'''
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

    def extra_header(self):
        ''' show extra header '''
        if self.verbose:
            print(f"panda version: {pd.__version__}")
        print(f'[INFO]    first date: {self.outputs["first"]}')
        print(f'[INFO]     last date: {self.outputs["last"]}')
        print(f'[INFO]   during days: {self.outputs["during"]}')

    def show_workingdays(self):
        ''' show working days '''
        if self.verbose:
            wd = LoadWorkingDays()
            for y in range(2021,2024+1):
                print(wd.get_msg(y))

    def action(self):
        ''' main function '''
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

        self.outputs['first'] = dates[0]
        self.outputs['last'] = dates[-1]
        self.outputs['during'] = DrivingData.get_between_dates(dates[0], dates[-1])

        if len(dates) != len(secs):
            print(f'[ERROR] not the same length {len(dates)} vs {len(secs)}')
            return

        ndict = {"date": dates, "seconds": secs}
        res = pd.DataFrame(ndict)

        des = res.describe()
        self.mu = peek_target(des, "mean")
        self.sigma = peek_target(des, "std")

        if self.debug:
            print_sep()
            print('item', des)

        self.fill_outputs(des)


    def do_show(self):
        ''' do show '''
        if self.simpleout:
            self.show_simplecsv()
        else:
            self.show_details()

    def fill_outputs(self, des):
        ''' fill results in outputs (dict) '''
        self.outputs['today'] = date.today()
        ans = peek_target(des, "count")
        count = str(int(floor(ans)))
        self.outputs['count'] = count
        for q in ['max', '75%', 'mean', '50%', '25%', 'min', 'std']:
            ans = peek_target(des, q)
            mmss = sec2mmss(ans)
            self.outputs[q] = mmss

    def show_simplecsv(self):
        ''' csv output '''
        for k,v in self.outputs.items():
            print(f'"{k}", "{v}"')

    def show_details(self):
        ''' show details of res² '''
        self.extra_header()
        self.show_workingdays()
        print_sep()
        for k in ['count', 'max', '75%', 'mean', '50%', '25%', 'min', 'std']:
            v = self.outputs[k]
            if k == "count":
                result = v
                j = result.rjust(10, ' ')
            else:
                secs = str2sec(v)
                result = f'{v}  ({secs:4.0f})'
                j = result.rjust(20, ' ')
            print(f'{k:10s}: {j:20s}')
        print_sep()
        self.show_poi()

    def show_poi(self):
        ''' show some values (extra) '''
        if not self.verbose:
            return
        print(f'{self.mu=}, {self.sigma=}')
        m = self.mu
        s = self.sigma
        mm = sec2mmss(m)
        (r1, r2) = (sec2mmss(m-s), sec2mmss(m+s))
        print(f'68.2%: {r1}--{mm}--{r2}')
        (r1, r2) = (sec2mmss(m-2*s), sec2mmss(m+2*s))
        print(f'95.4%: {r1}--{mm}--{r2}')

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
        #print(f'{result=}, {type(result)=}')
        return result
    except ValueError as e:
        print(f'WARN: ValueError: {e.args}')
    return ''


def perform_show_driving_data(in_file=None, out_file=None, conf_file=None,
    simpleout=False, verbose=False):
    ''' universal starter '''
    obj = DrivingData()
    obj.set_simpleout(simpleout)
    obj.set_verbose(verbose)

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
    obj.do_show()

def show_curios():
    ''' show some readme '''
    msg = '''
# some curios for normal distribution (only right side of μ)
0~1σ = 34.1%
1σ~2σ = 13.6% (acc: 47.7%, ±2σ: 95.4%)
2σ~3σ = 2.1%  (acc: 49.8%, ±4σ: 99.6%)
3σ~   = 0.1%  (acc: 49.9%)
'''
    print(msg)

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
    parser.add_argument("-s", "--sigma", action='store_true', default=False,
        help='show some curios about normal distribution')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')

    #parser.parse_args(['-i input.csv -o out.csv'])
    args = parser.parse_args()

    if args.sigma:
        show_curios()
        return

    if not args.run:
        show_parameters(parser)
        return

    perform_show_driving_data(in_file=args.input, out_file=args.output,
        conf_file=args.conf, simpleout=args.excel, verbose=args.verbose)


if __name__ == '__main__':
    main()
