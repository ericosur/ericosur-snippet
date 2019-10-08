#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' read driving data and make stastics '''

from __future__ import print_function
import os
import sys
import re
from math import floor
#from datetime import time
import numpy as np
import pandas as pd
import myutil

# pylint: disable=useless-object-inheritance
class DrivingData(object):
    ''' fetch driving data from gdrive or local csv '''
    def __init__(self, csvfile='/tmp/driving_data.csv'):
        self.debug = True
        self.jsonpath = ''
        self.jsondata = None
        self.csvfile = csvfile
        self.docid = ''
        self.sheetid = ''
        self.url = ''

    def read_setting(self):
        ''' read setting '''
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

    def dump_setting(self):
        ''' dump settings '''
        print('jsonpath:', self.jsonpath)
        print('docid:', self.docid)
        print('sheetid', self.sheetid)
        print('url:', self.url)

    def request_data(self):
        ''' request data '''
        csvdata = myutil.query_url_for_data(self.url)
        #print('csvdata: ', csvdata)
        with open(self.csvfile, 'wb') as ofile:
            ofile.write(csvdata)
            if self.debug:
                print('output csv to {}'.format(self.csvfile))

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
                print('[ERROR] at {} on {}, invalid format: {}'.format(ii, ds, duration[ii]))
                return

        if len(dates) != len(secs):
            print('[ERROR] not the same length {} vs {}'.format(len(dates), len(secs)))
            return

        ndict = {"date": dates, "seconds": secs}
        res = pd.DataFrame(ndict)

        # show details of res
        # print('res.info?')
        # res.info()
        # print_sep()
        des = res.describe()
        # print('all description...', des)
        # print_sep()

        queries = ['count', 'max', 'min', 'mean', '50%', 'std']
        for qq in queries:
            ans = peek_target(des, qq)
            # if not isinstance(ans, str):
            #     print('peek not a string:', ans)
            #     break
            if qq != 'count':
                result = sec2str(ans)
            else:
                result = str(int(floor(ans)))
            print('{:5s}: {:20s}'.format(qq, result.rjust(10, ' ')))
        print_sep()

# return: float64
def str2sec(timestr: str):
    ''' translate mm:ss.nn into float64 numeric '''
    if not isinstance(timestr, str):
        print('str2sec: not a string?', timestr)
        raise ValueError
    m = re.match(r'\d\d:\d\d\.\d\d', timestr)
    if m is None:
        print('invalid format for', timestr)
        raise ValueError

    minutes = 0.0
    seconds = 0.0
    total = 0.0
    try:
        arr = timestr.split(':')
        #print('in:{} out:{}'.format(timestr, arr))
        if len(arr) == 2:
            minutes = float(arr[0]) * 60.0
            seconds = float(arr[1])
            total = minutes + seconds
    except ValueError as e:
        print('ValueError with {}: {}'.format(timestr, e.args))
    return total

def strify(nn):
    ''' strify '''
    return '{:02}'.format(nn)

def sec2str(sec: str):
    ''' seconds to string '''
    # if not isinstance(sec, str):
    #     print('{} is not a string'.format(sec))
    #     return ''
    ss = []
    try:
        nn = int(sec)
    except ValueError:
        print('ValueError at {}'.format(sec))
        nn = 0
    while nn >= 60:
        qq = nn / 60
        rr = nn % 60
        ss.append(strify(rr))
        nn = int(qq)
    ss.append(strify(nn))
    ss.reverse()
    res = ':'.join(ss)
    return res

def print_sep():
    ''' print seperator '''
    print('-' * 50)

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
        print('WARN: ValueError: {}'.format(e.args))
        return ''


def load_data_from_gdrive():
    ''' load data from google drive '''
    dd = DrivingData()
    dd.read_setting()
    #dd.dump_setting()
    dd.request_data()
    dd.action()

def load_data_from_file(fn):
    ''' load data from file '''
    dd = DrivingData(fn)
    dd.action()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        FN = sys.argv[1]
        print('load csv data from: {}'.format(FN))
        load_data_from_file(FN)
    else:
        print('will request data from gdrive...')
        load_data_from_gdrive()
