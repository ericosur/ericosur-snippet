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

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile


def get_randomorg_apikey():
    ''' get apikey of random.org from json file '''
    home = os.environ.get('HOME')
    keypath = os.path.join(home, 'Private', 'random-org.json')
    if not os.path.exists(keypath):
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
