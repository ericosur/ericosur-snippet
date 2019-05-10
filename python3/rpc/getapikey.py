#!/usr/bin/env python3
# coding: utf-8

import os
import json
import myutil

def get_randomorg_apikey():
    home = os.environ.get('HOME')
    keypath = home + '/' + 'Private/random-org.json'
    data = myutil.read_jsonfile(keypath)
    apiKey = data.get('apiKey');
    if apiKey is None:
        print('[WARN] apiKey is None')
        return ""
    return apiKey

def main():
    print("apiKey: {}".format(get_randomorg_apikey()))

if __name__ == '__main__':
    main()
