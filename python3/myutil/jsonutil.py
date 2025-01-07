#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful functions for json '''

from typing import Any

__VERSION__ = "2024.03.28"

import json
from .commonutil import isfile

def read_jsonfile(fn:str, debug: bool=False) -> Any:
    '''
    specify json filename and return whole json object
    '''
    # read from json file
    if debug:
        print(f'[DEBUG] read json file from: {fn}')

    if not isfile(fn):
        raise FileNotFoundError

    # method #1
    with open(fn, 'r', encoding='utf8') as fstream:
        try:
            data = json.load(fstream)
        except json.decoder.JSONDecodeError as e:
            print('error while processing:', fn)
            print('json.decoder.JSONDecodeError:', e)
            return None
    return data


def read_textfile(fn: str, debug=False) -> str | None:
    ''' read specified file and return file content '''
    if debug:
        print(f'[DEBUG] read text file content from: {fn}')

    if not isfile(fn):
        raise FileNotFoundError

    content = None
    with open(fn, 'rt', encoding='utf8') as fh:
        content = fh.read()
    return content


# in order not to break client scripts
def read_setting(fn: str) -> Any:
    '''get json object from file'''
    return read_jsonfile(fn)


def request_value(data: dict[str, Any], key: str, default_value=None) -> Any:
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


def write_jsonfile(fn: str, data: dict[str, Any]) -> None:
    ''' write json into specified file '''
    if not isfile(fn):
        raise FileNotFoundError

    with open(fn, 'w', encoding='utf8') as ofile:
        ofile.write(json.dumps(data))
        print(f'output json to {fn}')
