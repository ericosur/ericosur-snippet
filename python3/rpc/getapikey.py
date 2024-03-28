#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
get apikey for random.org
'''

import os
import sys

#HOME = os.getenv('HOME')
#UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
sys.path.insert(0, "..")
from myutil import read_jsonfile, get_home, isfile


def get_randomorg_apikey():
    ''' get apikey of random.org from json file '''
    home = get_home()
    keypath = os.path.join(home, 'Private', 'random-org.json')
    if not isfile(keypath):
        print(f'[FAIL] config not exist: {keypath}')
        sys.exit(1)
    data = read_jsonfile(keypath)
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
