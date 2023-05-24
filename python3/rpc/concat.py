#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

''' try to concat files '''

import glob
import os
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)
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
    for ff in file_arr:
        test(ff)

if __name__ == '__main__':
    main()
