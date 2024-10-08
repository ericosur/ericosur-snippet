#!/usr/bin/env python3
# coding: utf-8

''' loading yaml '''

import json
# pip install pyyaml
import yaml


def main():
    ''' main '''
    with open('invoice.yaml', 'rt', encoding='utf8') as f:
        #data = yaml.load(f)
        data = yaml.load(f, Loader=yaml.FullLoader)

    print('type:', type(data), '-' * 20)
    for k,v in data.items():
        print(f'{k}: {v}')

    print('try to use json.dumps(data)', '-' * 20)
    try:
        # The data type "date" could not be converted from yaml to json directly
        print(json.dumps(data, indent=2, sort_keys=False))
    except TypeError as te:
        print('TypeError:', te)

if __name__ == '__main__':
    main()
