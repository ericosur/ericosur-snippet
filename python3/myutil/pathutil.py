#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' some useful tool functions for
    get default config by this order

'''

import os

__MODULE__ = "DefaultConfig"
__VERSION__ = "2024.03.29"


def _isdir(d):
    ''' true if a dir '''
    return os.path.isdir(d)

def _isfile(f):
    ''' true if a file '''
    return os.path.isfile(f)


class DefaultConfig():
    ''' a class helps to look up in default order '''

    def __init__(self, filename, debug=False):
        self.debug = debug
        self.fn = filename
        self.paths = []
        self.__prepare_paths()

    def __append_if_isfile(self, f):
        ''' append to the list if d exists '''
        if _isfile(f):
            self.paths.append(f)
        else:
            self.logd(f'[warn] not found: {f}')

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

        msg = f'__prepare_paths: {self.paths}'
        self.logd(msg)

    def logd(self, msg):
        ''' print log '''
        if self.debug:
            print(f'{__MODULE__}: {msg}')

    def get_default_config(self):
        ''' search config file in default paths '''
        self.logd(self.paths)
        for p in self.paths:
            if os.path.exists(p):
                self.logd(p)
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
