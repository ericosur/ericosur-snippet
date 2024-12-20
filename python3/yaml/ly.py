#!/usr/bin/env python3
# coding: utf-8

''' loading yaml '''

import json
import os
import sys
from typing import Union
sys.path.insert(0, "..")
sys.path.insert(0, "python3/")
from myutil import prt

try:
    import yaml
except ImportError as e:
    prt("cannot import module:", e)
    prt('pip install PyYAML')
    sys.exit(1)

def try_location(fn: str) -> Union[str, None]:
    ''' try to find file from current location and then
        same location of current script

        fn: only filename, without path
    '''
    dirn = os.path.dirname(os.path.abspath(__file__))
    newf = os.path.join(dirn, fn)
    if os.path.isfile(newf):
        return newf
    return None

def main():
    ''' main '''
    fn = 'invoice.yaml'
    if not os.path.isfile(fn):
        fn = try_location(fn)
        if fn is None:
            prt(f'cannot load data file ({fn}), exit...')
            sys.exit(1)
    prt(f'load: {fn}')
    with open(fn, 'rt', encoding='utf8') as f:
        #data = yaml.load(f)
        data = yaml.load(f, Loader=yaml.FullLoader)

    prt(f'type of date: {type(data)}')
    prt('-'*20)
    for k,v in data.items():
        prt(f'{k}: {v}')

    prt('try to use json.dumps(data) =====>')
    try:
        # The data type "date" could not be converted from yaml to json directly
        prt(json.dumps(data, indent=2, sort_keys=False))
    except TypeError as e:
        prt('TypeError:', e)

if __name__ == '__main__':
    main()
