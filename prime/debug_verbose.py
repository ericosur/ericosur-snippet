#!/usr/bin/python3
# coding: utf-8

'''
provide an interface/class for debug/verbose
'''

MODNAME = "DEBUG_VERBOSE"
VERSION = "2024.03.12"

class MyDebug():
    ''' my debug '''
    def __init__(self, debug):
        self._debug = debug

    @property
    def debug(self) -> bool:
        ''' title of notification '''
        return self._debug

    @debug.setter
    def debug(self, val: bool):
        ''' setter of title '''
        self._debug = val

class MyVerbose():
    ''' my verbose '''
    def __init__(self, verbose):
        self._verbose = verbose

    @property
    def verbose(self) -> bool:
        ''' title of notification '''
        return self._verbose
    @verbose.setter
    def verbose(self, val: bool):
        ''' setter of title '''
        self._verbose = val
