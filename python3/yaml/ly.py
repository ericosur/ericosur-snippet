#!/usr/bin/env python3
# coding: utf-8

''' loading yaml '''

import json

import yaml


def main():
    ''' main '''
    with open('invoice.yaml', 'rt', encoding='utf8') as f:
        #data = yaml.load(f)
        data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print('type:', type(data))
    try:
        # The data type "date" could not be converted from yaml to json directly
        print(json.dumps(data, indent=2, sort_keys=False))
    except TypeError as te:
        print('TypeError:', te)

if __name__ == '__main__':
    main()
