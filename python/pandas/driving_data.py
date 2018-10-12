#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' read driving data and make stastics '''

from __future__ import print_function
import os
import pandas as pd
from datetime import time
import myutil

class driving_data(object):
    def __init__(self):
        self.debug = True
        self.jsonfile = 'driving_data.json'
        self.jsondir = 'apikey/'
        self.jsonpath = self.jsonfile
        self.jsondata = None
        self.csvfile = '/tmp/driving_data.csv'
        self.docid = ''
        self.sheetid = ''
        self.url = ''

    def read_setting(self):
        home = os.getenv('HOME')
        self.jsonpath = home + '/' + self.jsondir + self.jsonfile
        if not myutil.isfile(self.jsonpath):
            print('setting file not found', self.jsonpath)
            os.exit(-1)
        self.jsondata = myutil.read_jsonfile(self.jsonpath)
        self.docid = self.jsondata.get('docid', '')
        self.sheetid = self.jsondata.get('sheetid', '')
        self.url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(self.docid, self.sheetid)

    def dump_setting(self):
        print('jsonpath:', self.jsonpath)
        print('docid:', self.docid)
        print('sheetid', self.sheetid)
        print('url:', self.url)

    def request_data(self):
        csvdata = myutil.query_url_for_data(self.url)
        #print('csvdata: ', csvdata)
        with open(self.csvfile, 'w') as ofile:
            ofile.write(csvdata)
            if self.debug:
                print('output json to {}'.format(self.csvfile))

    def action(self):
        ''' main function '''
        #print("pd.__version__: {}".format(pd.__version__))

        # read csv file as dataframe
        data = pd.read_csv(self.csvfile)

        s1 = data['duration']
        dates = []
        secs = []
        for ii, ds in enumerate(data['date']):
            dates.append(ds)
            secs.append(str2sec(s1[ii]))

        ndict = {"date": dates, "seconds": secs}
        res = pd.DataFrame(ndict)
        #print(res.info())

        print_sep()
        des = res.describe()
        #print('all description...', des)
        #print_sep()

        queries = ['count', 'max', 'min', 'mean', '50%', 'std']
        for qq in queries:
            ans = peek_target(des, qq)
            print('{:5s}: {:20s}'.format(qq, ans.rjust(10,' ')))
        print_sep()


def str2sec(timestr):
    arr = timestr.split(':')
    sec = 0.0
    if len(arr) == 2:
        sec = float(arr[0]) * 60.0 + float(arr[1])
    return sec

def strify(nn):
    return '{:02}'.format(nn)

def sec2str(sec):
    ss = []
    nn = int(sec)
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
    print('-' * 40)

def peek_target(desc_table, target):
    #print('desc_table:', desc_table)
    desc_list = desc_table.index.tolist()
    try:
        midx = desc_list.index(target)
        mean_value = desc_table.iloc[midx, 0]
        result = sec2str(mean_value)
        return result
    except ValueError:
        return ''



def test():
    dd = driving_data()
    dd.read_setting()
    #dd.dump_setting()
    dd.request_data()
    dd.action()

if __name__ == '__main__':
    test()
