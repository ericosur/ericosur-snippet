#!/usr/bin/env python3

'''
the utility functions
'''

import locale
import sys
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from random import randint


def setup_local_paths() -> None:
    '''Add local project paths based on this file location.'''
    this_dir = Path(__file__).resolve().parent
    kana_dir = this_dir.parent
    py3_dir = kana_dir.parent
    myutil_dir = py3_dir.joinpath('myutil')
    madlog_dir = py3_dir.joinpath('madlog')
    sys.path.insert(0, str(py3_dir))
    sys.path.insert(0, str(myutil_dir))
    sys.path.insert(0, str(madlog_dir))

try:
    setup_local_paths()
    from madlog import get_logd, get_prt  # type: ignore[import]
    #from myutil import do_nothing
except ImportError:
    print('[INFO] no madlog, exit...')
    sys.exit(1)

prt = get_prt()
logd = get_logd()

REAL_COMPAIN = False

def get_datetag() -> str:
    ''' string in UYYMMDD '''
    today = datetime.now().astimezone().date()
    yy = today.year - 2000
    s = f'U{yy:02d}{today.month:02d}{today.day:02d}-{randint(0,99999):05d}'
    return s

def to_currency(v: str) -> Decimal:
    ''' convert str to Decimal according to locale, return "" if empty
        eg: "1,234,567.89" to 1234567.89
    '''
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    r = Decimal()
    try:
        r = Decimal(locale.atof(v))
    except ValueError:
        prt(f'Value Error on: {v}')
    return r

def to_float(v: str) -> float:
    ''' convert str to float, return "" if empty '''
    r = 0.0
    try:
        r = float(v)
    except ValueError:
        prt(f'Value Error on: {v}')
    return r
