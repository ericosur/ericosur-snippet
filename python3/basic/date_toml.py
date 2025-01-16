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
        print(f'{dates[k]}\n{dates[k]=}')
        dt = dates[k]
        print(dt)

    start = dates['from']
    end = dates['to']
    for i in range(start, end+1):
        k = f'ldt{i}'
        print(f'{dates[k]=}')

def main():
    ''' main '''
    test0()

if __name__ == '__main__':
    main()
