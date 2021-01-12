#!/usr/bin/python3.6
# coding: utf-8

'''
brief description for this script
'''

import os
import json

def read_jsonfile(fn, debug=False):
    '''
    specify json filename and return whole json object
    '''
    if debug:
        print('load json from {}'.format(fn))
    if not os.path.exists(fn):
        print('file not found')
        return None
    # read from json file

    # method #1
#    with open(filename) as sec_file:
#        data = json.load(sec_file)

    # kiss method #2
    data = json.load(open(fn))

    return data

def main():
    ''' main '''
    data = read_jsonfile('periodic-table-lookup.json')
    for i, n in enumerate(data['order']):
        #print(i, n)
        t = data[n]
        print('{} {} {}'.format(t['number'], t['symbol'], t['name']))


if __name__ == '__main__':
    main()
