#!/usr/bin/python3
#coding:utf-8

'''
the utility functions
'''

from datetime import date
from decimal import Decimal
from random import randint
import locale

def logd(*args, **wargs):
    ''' logd '''
    print(*args, **wargs)

def get_datetag() -> str:
    ''' string in UYYMMDD '''
    today = date.today()
    yy = today.year - 2000
    s = f'U{yy:02d}{today.month:02d}{today.day:02d}-{randint(0,99999):05d}'
    return s

def to_currency(v: str) -> Decimal:
    ''' convert str to Decimal according to locale, return "" if empty
        eg: "1,234,567.89" to 1234567.89
    '''
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    r = ""
    try:
        r = Decimal(locale.atof(v))
    except ValueError:
        #print('Value Error on:', v)
        pass
    return r

def to_float(v: str) -> float:
    ''' convert str to float, return "" if empty '''
    r = ""
    try:
        r = float(v)
    except ValueError:
        #print('Value Error on:', v)
        pass
    return r
