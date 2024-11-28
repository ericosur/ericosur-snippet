#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=wrong-import-position
#

'''
read json and list
'''


import sys

sys.path.insert(0, "..")
from myutil import read_jsonfile


def main():
    ''' main '''
    data = read_jsonfile('periodic-table-lookup.json')
    for n in data['order']:
        t = data[n]
        num = t['number']
        if num >= 82:
            print(f"{t['number']:3d} {t['symbol']:3s} {t['name']:22s}")

if __name__ == '__main__':
    main()
