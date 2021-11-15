'''
common function to read json file
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
    with open(fn, 'r', encoding='utf8') as fstream:
        data = json.load(fstream)
    return data
