#!/usr/bin/env python3
# coding: utf-8

'''
provide an interface/class for debug/verbose
'''

import sys

MODNAME = "DEBUG_VERBOSE"
__VERSION__ = "2024.03.12"

def die(*args, **kwargs):
    ''' similar to die in perl '''
    print(*args, file=sys.stderr, **kwargs)
    sys.exit()

class MyDebug():
    ''' my debug '''
    def __init__(self, debug, tag=None):
        self._debug = debug
        self._tag = tag

    @property
    def debug(self) -> bool:
        ''' title of notification '''
        return self._debug

    @debug.setter
    def debug(self, val: bool):
        ''' setter of title '''
        self._debug = val

    def logd(self, *args, **kwargs):
        '''
        from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
        1. if tag is set in the kwargs, use it
        2. if self._tag is set, use it
        3. keep it empty
        '''
        if not self._debug:
            return
        KEY = 'tag'
        v = None
        if KEY in kwargs:
            v = kwargs.pop(KEY)
        elif self._tag:
            v = self._tag
        if v:
            print(f"[DEBUG][{v}]", end=' ')
        else:
            print("[DEBUG]", end=' ')
        print(*args, **kwargs)


class MyVerbose():
    ''' my verbose '''
    def __init__(self, verbose, tag=None):
        self._verbose = verbose
        self._tag = tag

    @property
    def verbose(self) -> bool:
        ''' title of notification '''
        return self._verbose
    @verbose.setter
    def verbose(self, val: bool):
        ''' setter of title '''
        self._verbose = val

    def logv(self, *args, **kwargs):
        '''
        from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
        1. if tag is set in the kwargs, use it
        2. if self._tag is set, use it
        3. keep it empty
        '''
        if not self._verbose:
            return
        KEY = 'tag'
        v = None
        if KEY in kwargs:
            v = kwargs.pop(KEY)
        elif self._tag:
            v = self._tag
        if v:
            print(f"[VERBOSE][{v}]", end=' ')
        else:
            print("[VERBOSE]", end=' ')
        print(*args, **kwargs)
