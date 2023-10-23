#!/usr/bin/env python3
# coding: UTF-8

'''
module that helps to load functions in myutil
'''

__VERSION__ = "2023.10.23"
SETTING_FILE = "setting.json"

# pylint: disable=import-error
# pylint: disable=wrong-import-position

import os
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

import myutil

def get_home():
    ''' get home dir '''
    return HOME

def gethome():
    ''' get home dir '''
    return HOME

def read_jsonfile(fn):
    ''' read json file '''
    return myutil.read_jsonfile(fn)

def read_setting(fn):
    ''' read settings '''
    return myutil.read_setting(fn)

def read_from_stdin(fn):
    ''' read from stdin '''
    return myutil.read_from_stdin(fn)

def get_smalltxt_path():
    ''' get prime data file path '''
    d = read_setting(SETTING_FILE)
    if d is None:
        print(f'[FAIL] {__file__}: fail to read settings')
        sys.exit(1)
    txtfn = os.path.join(gethome(), d['prime_path'], d['prime_small'])
    return txtfn

def get_largedata_path():
    ''' get large prime data file path '''
    d = read_setting(SETTING_FILE)
    if d is None:
        print(f'[FAIL] {__file__}: fail to read settings')
        sys.exit(1)
    txtfn = os.path.join(gethome(), d['prime_path'], d['prime_large'])
    pfn = os.path.join(gethome(), d['prime_path'], d['pickle_large'])
    pzfn = os.path.join(gethome(), d['prime_path'], d['pickle_large_compress'])
    return txtfn, pfn, pzfn

def get_bigdata_path():
    ''' get large prime data file path '''
    d = read_setting(SETTING_FILE)
    if d is None:
        print(f'[FAIL] {__file__}: fail to read settings')
        sys.exit(1)
    txtfn = os.path.join(gethome(), d['prime_path'], d['prime_big'])
    pfn = os.path.join(gethome(), d['prime_path'], d['pickle_big'])
    pzfn = os.path.join(gethome(), d['prime_path'], d['pickle_big_compress'])
    return txtfn, pfn, pzfn
