#!/usr/bin/python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html
'''

BUILTIN_LIB = False

import sys

class LoadToml():
    '''
    wrapper class to load toml, for builtin tomllib/toml
    '''
    is_builtin = None
    is_external = None
    toml_lib = None

    def __init__(self, fn):
        self.tomlfn = fn
        self.data = None
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
            #print("cannot import tomllib, try toml")
            try:
                # pip install toml
                import toml
                LoadToml.is_builtin = True
                LoadToml.is_external = False
                LoadToml.toml_lib = toml
                if not self.tomlfn is None:
                    with open(self.tomlfn, 'rt', encoding='UTF-8') as f:
                        self.data = toml.load(f)
            except ImportError:
                print("cannot import toml, exit...")
                sys.exit(1)
        #self.load()

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
    obj = LoadToml.get_class('config.toml')
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
