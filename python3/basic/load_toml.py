#!/usr/bin/python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html

some recommends tomlkit

'''

import sys

# pylint: disable=import-outside-toplevel
class LoadToml():
    '''
    wrapper class to load toml, for builtin tomllib/toml
    '''
    debug = False
    is_builtin = None
    is_external = None
    toml_lib = None

    def __init__(self, fn):
        self.tomlfn = fn
        self.data = None

        # load external toml first, then built-in tomllib
        try:
            # pip install toml
            import toml
            LoadToml.is_builtin = False
            LoadToml.is_external = True
            LoadToml.toml_lib = toml
            if not self.tomlfn is None:
                with open(self.tomlfn, 'rt', encoding='UTF-8') as f:
                    self.data = toml.load(f)
        except ModuleNotFoundError:
            #print("cannot import tomllib...")
            self._use_another_lib()

    def _use_another_lib(self):
        ''' load built-in library '''
        if self.debug:
            print('use built-in library tomllib')
        try:
            # tomllib is standard library provided by python 3.11
            import tomllib
            LoadToml.is_builtin = True
            LoadToml.is_external = False
            LoadToml.toml_lib = tomllib
            if not self.tomlfn is None:
                with open(self.tomlfn, 'rb') as f:
                    self.data = tomllib.load(f)
        except ImportError:
            print("cannot import toml nor tomllib, exit...")
            sys.exit(1)

    @classmethod
    def get_class(cls, fn=None):
        ''' get class '''
        #print(cls.__name__)
        return cls(fn)

    def get_data(self):
        ''' get data '''
        return self.data


def test():
    ''' test '''
    print('test()')
    obj = LoadToml.get_class('config.toml')
    obj.debug = True
    data = obj.get_data()
    if obj.is_builtin:
        print('[INFO] use builtin library')
    else:
        print('[INFO] use external library')

    if data is None:
        print('cannot load data')
    else:
        print(data)
        #print(f'owner: {data["owner"]}')

if __name__ == '__main__':
    test()
