#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''demo fetch image from imgur'''

from __future__ import print_function
import os
import sys
import json
import urllib2

__version__ = '0.0.2'

def read_jsonfile(fn):
    '''
    specify json filename and return whole json object
    '''
    print('load json from {}'.format(fn))
    if not os.path.exists(fn):
        print('file not found')
        return None
    # read from json file

    # method #1
#    with open(filename) as sec_file:
#        data = json.load(sec_file)

    # kiss method #2
    data = json.load(open(fn))

    return data

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
        print('key "{}" not found, will use default_value'.format(key))
    return ret

def insert_syspath(p):
    if is_path_exist(p):
        print('insert {} into sys path'.format(p))
        sys.path.insert(0, p)
    return

def is_path_exist(p):
    return os.path.exists(p)

def isfile(url):
    '''test file exists'''
    return os.path.isfile(url)

def isdir(url):
    '''test dir exists'''
    return os.path.isdir(url)


def query_url(url):
    ''' query url and return data '''
    debug = False
    if debug:
        print(url)
    result = urllib2.urlopen(url).read()
    data = json.loads(result)
    return data

def write_json(fn, data):
    ''' write json into specified file '''
    with open(fn, 'w') as ofile:
        ofile.write(json.dumps(data))
        print('output json to {0}'.format(fn))


def main():
    '''main function'''
    fn = 'nosuchfile'
    data = read_jsonfile(fn)
    if data:
        print('skipped...')
        return

def test():
    '''test function'''
    print('test')
    jdata = read_jsonfile('setting.json')
    data = jdata['myutil.py']
    ret = request_value(data, 'name')
    print('ret:', ret)

if __name__ == '__main__':
    test()
