#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' read driving data and make stastics '''

from __future__ import print_function
import pandas as pd
from datetime import time


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

def main():
    ''' main function '''
    #print("pd.__version__: {}".format(pd.__version__))
    FILEN = 'driving_data.csv'
    # read csv file as dataframe
    data = pd.read_csv(FILEN)

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

    queries = ['max', 'min', 'mean', '50%', 'std']
    for qq in queries:
        ans = peek_target(des, qq)
        print('{:5s}: {:20s}'.format(qq, ans.rjust(10,' ')))
    print_sep()


if __name__ == '__main__':
    main()
