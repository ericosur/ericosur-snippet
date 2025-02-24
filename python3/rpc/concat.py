#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

''' try to concat files '''

import glob
import os
import sys

# ruff: noqa: E402
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
sys.path.insert(0, 'python3/')
from myutil import read_jsonfile

def test(fn):
    ''' test '''
    data = read_jsonfile(fn)
    if data is None:
        print('[FAIL] read json fail')
        sys.exit(1)
    arr = data.get('result').get('random').get('data')
    cnt = 0
    mode = 'wt'
    if os.path.exists('data.txt'):
        print('file exists, use "at" to append')
        mode = 'at'

    with open('data.txt', mode, encoding='utf8') as datafile:
        for elem in arr:
            print(f'{elem}', file=datafile)
            cnt += 1
    print(f'cnt: {cnt}')

def main():
    ''' main '''
    file_arr = glob.glob('resp?.json')
    if file_arr is None or len(file_arr) < 1:
        print('fail: no file found')
        sys.exit(1)
    for ff in file_arr:
        test(ff)

if __name__ == '__main__':
    main()
