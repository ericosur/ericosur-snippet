#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' read driving data and make stastics '''

from __future__ import print_function
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

import myutil
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
        self.csvfile = csvfile

    def read_setting(self):
        ''' read setting '''
        if self.debug:
            print('read_setting()')

        home = os.getenv('HOME')
        self.jsonpath = home + '/Private/driving_data.json'
        if not myutil.isfile(self.jsonpath):
            print('setting file not found', self.jsonpath)
            sys.exit(1)
        self.jsondata = myutil.read_jsonfile(self.jsonpath)
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
        csvdata = myutil.query_url_for_data(self.url)
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

    def action(self):
        ''' main function '''
        #print("pd.__version__: {}".format(pd.__version__))

        # read csv file as dataframe
        data = pd.read_csv(self.csvfile)
        #print(type(data))
        #print_sep()
        duration = data['duration']
        #print(duration)
        #print(data['date'])
        #print_sep()

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

        print(f'[INFO]    first date: {dates[0]}')
        print(f'[INFO]     last date: {dates[-1]}')
        print(f'[INFO] dates between: {DrivingData.get_between_dates(dates[0], dates[-1])}')
        print('[INFO] for 2021, total working days are 239')
        print('[INFO] for 2022, total working days are 242')

        if len(dates) != len(secs):
            print(f'[ERROR] not the same length {len(dates)} vs {len(secs)}')
            return

        ndict = {"date": dates, "seconds": secs}
        res = pd.DataFrame(ndict)

        # show details of res
        # print('res.info?')
        # res.info()
        # print_sep()
        des = res.describe()
        if self.debug:
            print_sep()
            print('item', des)
        print_sep()
        self.show_details(des)

    @staticmethod
    def show_details(des):
        ''' show details of res² '''
        queries = ['count', 'max', '75%', 'mean(μ)', '50%', '25%', 'min', 'stddev(σ)']
        for qq in queries:
            ans = peek_target(des, qq)
            # if not isinstance(ans, str):
            #     print('peek not a string:', ans)
            #     break
            if qq != 'count':
                #result = sec2str(ans)
                result = sec2mmss(ans)
            else:
                result = str(int(floor(ans)))
            j = result.rjust(10, ' ')
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


def main(files):
    ''' main '''
    dd = DrivingData()

    # request from google drive
    if files == []:
        print('will request file from google drive...')
        dd.set_csvfile('/tmp/driving_data.csv')
        dd.read_setting()
        if dd.debug:
            dd.dump_setting()
        dd.request_data()
        dd.action()
        return

    # file list from CLI
    print('file list from CLI...')
    for ff in files:
        print_sep()
        print(f'load csv data from: {ff}')
        dd.set_csvfile(ff)
        dd.action()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print('will request data from gdrive...')
        main([])
