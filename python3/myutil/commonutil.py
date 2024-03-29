#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions '''

import os
import sys


def get_home():
    ''' return $HOME '''
    return os.getenv('HOME')

def is_path_exist(p):
    ''' true if specified path exists '''
    if not p:
        raise ValueError("input is None")
    return os.path.exists(p)

def isfile(url):
    '''test file exists'''
    if not url:
        raise ValueError("input is None")
    return os.path.isfile(url)

def isdir(url):
    '''test dir exists'''
    if not url:
        raise ValueError("input is None")
    return os.path.isdir(url)

def read_from_stdin(func):
    ''' read from stdin '''
    if not func:
        raise ValueError("input is None")
    args = []
    for line in sys.stdin:
        args.append(line.strip())
    func(args)

def print_stderr(*args, **kwargs):
    '''
    from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
    '''
    print(*args, file=sys.stderr, **kwargs)
