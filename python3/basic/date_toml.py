#!/usr/bin/env python3
# coding: utf-8

'''
- example to read config.toml
    https://docs.python.org/zh-tw/dev/library/tomllib.html

- [hands on python library toml](https://www.legendu.net/en/blog/hands-on-python-library-toml/)

- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)
'''

#import datetime
#import sys
try:
    from rich.pretty import pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = pprint if USE_RICH else print

from load_toml import LoadToml


def test0():
    ''' test0 '''
    # Load data from a TOML file
    obj = LoadToml('dates.toml')
    dates = obj.get_data()

    start = dates['start']
    end = dates['end']
    for i in range(start, end+1):
        k = f'odt{i}'
        prt(f'{dates[k]}\n{dates[k]=}')
        dt = dates[k]
        prt(dt)

    start = dates['from']
    end = dates['to']
    for i in range(start, end+1):
        k = f'ldt{i}'
        prt(f'{dates[k]=}')

def main():
    ''' main '''
    test0()

if __name__ == '__main__':
    main()
