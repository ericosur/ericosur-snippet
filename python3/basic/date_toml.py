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

try:
    # tomllib is standard library provided by python 3.11
    import tomllib as tml
except ImportError:
    print("cannot import tomllib, try toml")
    try:
        # pip install toml
        import toml as tml
    except ImportError:
        print("cannot import toml")
        sys.exit(1)

def test0():
    ''' test0 '''
    # Load data from a TOML file
    with open('dates.toml', 'rb') as f:
        dates = tml.load(f)

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
