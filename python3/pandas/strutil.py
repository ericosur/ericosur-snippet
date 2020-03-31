#!/usr/bin/python3
# coding: utf-8

''' some useful string snippets '''

import re

def print_sep():
    ''' print seperator '''
    print('-' * 50)

def strify(nn):
    ''' strify '''
    return '{:02}'.format(nn)

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
