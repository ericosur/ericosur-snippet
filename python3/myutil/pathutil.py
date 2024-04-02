#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions for
    get default config by this order

'''

import os
from .debug_verbose import MyDebug

__MODULE__ = "DefaultConfig"
__VERSION__ = "2024.04.02"


def _isdir(d):
    ''' true if a dir '''
    return os.path.isdir(d)

def _isfile(f):
    ''' true if a file '''
    return os.path.isfile(f)


class DefaultConfig(MyDebug):
    ''' a class helps to look up in default order '''

    def __init__(self, filename, debug=False):
        super().__init__(debug) # MyDebug
        self.fn = filename
        self.paths = []
        self.__prepare_paths()

    def __append_if_isfile(self, f):
        ''' append to the list if d exists '''
        if _isfile(f):
            self.paths.append(f)
        else:
            self._log(f'[warn] not found: {f}')

    def __prepare_paths(self):
        ''' prepare paths '''
        home = os.getenv('HOME')

        # 1. $HOME/Private/
        tmp = os.path.join(home, 'Private', self.fn)
        self.__append_if_isfile(tmp)
        # 2. $HOME
        tmp = os.path.join(home,  self.fn)
        self.__append_if_isfile(tmp)
        # 3. the current folder
        tmp = os.path.join('./',  self.fn)
        self.__append_if_isfile(tmp)

        # msg = f'__prepare_paths: {self.paths}'
        # self._log(msg)

    def _log(self, *args, **wargs):
        ''' my own log '''
        if 'tag' not in wargs:
            wargs['tag'] = __MODULE__
        self.logd(*args, **wargs)

    def get_default_config(self):
        ''' search config file in default paths '''
        self._log(f'get_default_config: paths: {self.paths}')
        for p in self.paths:
            if _isfile(p):
                self._log('got:', p)
                return p
        return None

    def search_in_path(self):
        ''' search file in $PATH
            return immediately if found
        '''
        the_path = os.getenv('PATH')
        for d in the_path.split(os.pathsep):
            if os.path.isdir(d):
                p = os.path.join(d, self.fn)
                if os.path.exists(p):
                    return p
        return None
