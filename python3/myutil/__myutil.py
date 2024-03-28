#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions '''

from __future__ import print_function


import os
import platform
import sys

# pylint: disable=no-member
# pylint: disable=import-outside-toplevel

__version__ = '0.0.4'

DEBUG = False



def insert_syspath(p):
    ''' help to insert path into module search path '''
    if os.path.isdir(p):
        print(f'insert {p} into sys path')
        sys.path.insert(0, p)


def mkdir(url) -> bool:
    ''' simulate mkdir -p '''
    try:
        if not os.path.exists(url):
            os.makedirs(url)
            if DEBUG:
                print(f'mkdir: {url}')
            return True
    except FileExistsError as e:
        if DEBUG:
            print(e)
    return False


def get_hostname():
    ''' get hostname '''
    return platform.node()

def is_cygwin():
    ''' check if cygwin '''
    system_name = platform.system().lower()
    return "cygwin" in system_name

def is_linux():
    ''' check if linux '''
    system_name = platform.system().lower()
    return "linux" in system_name

def is_windows():
    ''' check if windows '''
    system_name = platform.system().lower()
    return "windows" in system_name


def get_random_str(lens=15):
    ''' get secret '''
    import re
    import secrets

    #r = secrets.token_hex(LENS)
    r = ''
    while len(r) < lens:
        r = secrets.token_urlsafe(lens*2)   # may contains _ or -
        r = re.sub(r'[-_]+', '', r)     # remove [-_]
        r = re.sub(r'^[0-9]+', '', r)   # remove leading digits 0-9
    return r[:lens]
