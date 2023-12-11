#!/usr/bin/env python3
#coding: utf-8

'''
provide functions only, do not run this directly
'''

import os
import pickle


def loadarray(fn):
    ''' load if exist '''
    if not os.path.exists(fn):
        print(f'[info] no such file {fn}')
        return None
    arr = None
    with open(fn, "rb") as fobj:
        arr = pickle.load(fobj)

    print(f'read {len(arr)} from disk')
    return arr


def savearray(fn, arr):
    ''' save if not exist '''
    if os.path.exists(fn):
        print(f'[info] will not overwrite {fn}')
        return

    with open(fn, "wb") as fobj:
        pickle.dump(arr, fobj)
    print(f'[info] save array to {fn}')
