#!/usr/bin/python3
# coding: utf-8

'''
- example to read config.toml
    https://docs.python.org/zh-tw/dev/library/tomllib.html

- [hands on python library toml](https://www.legendu.net/en/blog/hands-on-python-library-toml/)

- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)
'''

import sys
import datetime

from load_toml import LoadToml

def test0():
    ''' test0 '''
    # Load data from a TOML file
    obj = LoadToml.get_class('date.toml')
    dates = obj.get_data()

    try:
        start = dates['start']
        end = dates['end']
        for i in range(start, end+1):
            k = f'odt{i}'
            print(f'{dates[k]}\n{dates[k]=}')
            dt = dates[k]

    except TomlDecodeError as e:
        print(e)

    try:
        start = dates['from']
        end = dates['to']
        for i in range(start, end+1):
            k = f'ldt{i}'
            print(f'{dates[k]=}')
    except TomlDecodeError as e:
        print(e)

def main():
    ''' main '''
    test0()

if __name__ == '__main__':
    main()
