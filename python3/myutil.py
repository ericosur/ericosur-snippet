#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions '''

from __future__ import print_function
import os
import sys
import json

# pylint: disable=no-member
# pylint: disable=import-outside-toplevel

__version__ = '0.0.2'

def read_jsonfile(fn, debug=False):
    '''
    specify json filename and return whole json object
    '''
    if debug:
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

def get_python_version():
    ''' return version string of python '''
    py_ver = ".".join(map(str, sys.version_info[:2]))
    return py_ver

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
    ''' help to insert path into module search path '''
    if is_path_exist(p):
        print('insert {} into sys path'.format(p))
        sys.path.insert(0, p)

def is_path_exist(p):
    ''' true if specified path exists '''
    return os.path.exists(p)

def isfile(url):
    '''test file exists'''
    return os.path.isfile(url)

def isdir(url):
    '''test dir exists'''
    return os.path.isdir(url)


def query_url_for_data(url):
    ''' query url and return data
    refer to: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
    '''
    result = None
    debug = False
    if debug:
        print(url)
    py_ver = get_python_version()
    try:
        if float(py_ver) >= 3.0:
            #print("python >= 3.0")
            import urllib.request
            result = urllib.request.urlopen(url).read()
        else:
            #print("python < 3.0")
            import urllib
            result = urllib.urlopen(url).read()
    except ImportError:
        print('[ERROR] import error!')
    return result


def query_url_for_json(url):
    ''' query url and return json data
    refer to: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
    '''
    result = query_url_for_data(url)
    data = json.loads(result)
    return data


def write_json(fn, data):
    ''' write json into specified file '''
    with open(fn, 'w') as ofile:
        ofile.write(json.dumps(data))
        print('output json to {0}'.format(fn))

def print_stderr(*args, **kwargs):
    '''
    from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
    '''
    print(*args, file=sys.stderr, **kwargs)

def read_from_stdin(func):
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        args.append(line.strip())
    func(args)


def main():
    '''main function'''
    fn = 'nosuchfile'
    data = read_jsonfile(fn)
    if data:
        print('skipped...')
        return

def test():
    '''test function'''
    print('test() of myutil.py')
    fn = 'setting.json'
    if isfile(fn):
        jdata = read_jsonfile(fn)
        data = jdata['myutil.py']
        ret = request_value(data, 'name')
        print('ret:', ret)
    else:
        print('file not found: {}'.format(fn))

if __name__ == '__main__':
    test()
