#!/usr/bin/env python3
# coding: utf-8

'''
get apikey for random.org
'''

from __future__ import print_function
import os
#import json
import myutil

def get_randomorg_apikey():
    ''' get apikey of random.org from json file '''
    home = os.environ.get('HOME')
    keypath = home + '/' + 'Private/random-org.json'
    if not myutil.isfile(keypath):
        print(f'[FAIL] key file not exist: {keypath}')
        return ""
    data = myutil.read_jsonfile(keypath)
    apiKey = data.get('apiKey')
    if apiKey is None:
        print('[WARN] apiKey is None')
        return ""
    return apiKey

def main():
    ''' main '''
    key = get_randomorg_apikey()
    print(f"apiKey: {key}")

if __name__ == '__main__':
    main()
