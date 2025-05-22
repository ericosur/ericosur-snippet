#!/usr/bin/env python3
# coding: utf-8

''' some useful string snippets '''

from datetime import date
import re


def strify(nn):
    ''' strify '''
    return f'{nn:02}'

# return: float64
def str2sec(timestr: str) -> float:
    ''' translate mm:ss.nn into float64 numeric '''
    if not isinstance(timestr, str):
        print('str2sec: not a string?', timestr)
        raise ValueError
    # mm:ss.ss (mm part could be 3 digits)
    m = re.match(r'\d+:\d\d(\.\d\d)?', timestr)
    if m is None:
        print('invalid format for', timestr)
        raise ValueError

    minutes = 0.0
    seconds = 0.0
    total = 0.0
    try:
        arr = timestr.split(':')
        if len(arr) == 2:
            minutes = float(arr[0]) * 60.0
            seconds = float(arr[1])
            total = minutes + seconds
    except ValueError as e:
        print(f'ValueError with {timestr}: {e.args}')
    # if total < 1000:
    #     print(f'[warn] str2sec: {timestr=} {total=}')
    return total

def sec2str(sec: str):
    ''' seconds to string '''
    ss = []
    try:
        nn = int(sec)
    except ValueError:
        print(f'ValueError at {sec}')
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

def sec2mmss(sec: str):
    ''' seconds to mm:ss string '''
    ss = []
    try:
        nn = int(sec)
    except ValueError:
        print(f'ValueError at {sec}')
        nn = 0

    if nn >= 60:
        qq = nn / 60
        rr = nn % 60
        ss.append(strify(rr))
        nn = int(qq)
    ss.append(strify(nn))
    ss.reverse()
    res = ':'.join(ss)
    return res

def str2date(s: str) -> date:
    ''' date string to date object
        [in] 2020-01-01
    '''
    arr = s.split('-')
    try:
        vals = [int(x) for x in arr]
    except ValueError:
        print('[ERROR] str2date: invalid string to integer:', s)
        return None
    return date(vals[0], vals[1], vals[2])

def get_between_dates(start: str, end: str) -> str:
    ''' get dates between
        [in] str start date 2020-01-01
        [out] str end date 2020-02-29
    '''
    start_date = str2date(start)
    end_date = str2date(end)
    ddiff = end_date - start_date
    return str(ddiff.days)
