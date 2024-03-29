#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=wrong-import-position

'''
get apikey for random.org
'''

import sys

sys.path.insert(0, "..")
from myutil import read_jsonfile, DefaultConfig


def get_randomorg_apikey():
    ''' get apikey of random.org from json file '''
    FN = 'random-org.json'
    keypath = DefaultConfig(FN).get_default_config()
    if not keypath:
        raise FileNotFoundError(FN)

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
