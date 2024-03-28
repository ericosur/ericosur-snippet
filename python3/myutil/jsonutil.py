#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful functions for json '''


__VERSION__ = "2024.03.28"

import json


def read_jsonfile(fn:str, debug=False):
    '''
    specify json filename and return whole json object
    '''
    # read from json file
    if debug:
        print(f'[DEBUG] read json file from: {fn}')

    # method #1
    with open(fn, 'r', encoding='utf8') as fstream:
        data = json.load(fstream)
    # kiss method #2
    #data = json.load(open(fn))
    return data


def read_textfile(fn: str, debug=False) -> str:
    ''' read specified file and return file content '''
    if debug:
        print(f'[DEBUG] read text file content from: {fn}')
    content = None
    with open(fn, 'rt', encoding='utf8') as fh:
        content = fh.read()
    return content


# in order not to break client scripts
def read_setting(fn):
    '''get json object from file'''
    return read_jsonfile(fn)


def request_value(data, key, default_value=None):
    '''
    given json object and request key, if key does not exist, return None
    if default_value is specified, will return default value if value not
    found
    '''
    ret = default_value
    try:
        ret = data[key]
    except KeyError:
        print(f'key "{key}" not found, will use default_value')
    return ret


def write_jsonfile(fn, data):
    ''' write json into specified file '''
    with open(fn, 'w', encoding='utf8') as ofile:
        ofile.write(json.dumps(data))
        print(f'output json to {fn}')
