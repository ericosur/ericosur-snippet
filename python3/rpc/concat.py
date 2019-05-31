#!/usr/bin/env python3
# coding: utf-8

''' try to concat files '''

from __future__ import print_function
import glob
#import json
import myutil

def test(fn):
    ''' test '''
    data = myutil.read_jsonfile(fn)
    if data is None:
        print('[FAIL] read json fail')
    arr = data.get('result').get('random').get('data')
    cnt = 0
    mode = 'wt'
    if myutil.isfile('data.txt'):
        print('file exists, use "at"')
        mode = 'at'

    with open('data.txt', mode) as datafile:
        for elem in arr:
            print('{}'.format(elem), file=datafile)
            cnt += 1
    print('cnt: {}'.format(cnt))

def main():
    ''' main '''
    file_arr = glob.glob('resp?.json')
    for ff in file_arr:
        test(ff)

if __name__ == '__main__':
    main()
