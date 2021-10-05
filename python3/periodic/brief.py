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
        print(f'load json from {fn}')
    if not os.path.exists(fn):
        print('file not found')
        return None
    # read from json file

    # method #1
#    with open(filename) as sec_file:
#        data = json.load(sec_file)

    # kiss method #2
    with open(fn, 'rt', encoding='utf8') as fobj:
        data = json.load(fobj)
    return data


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
