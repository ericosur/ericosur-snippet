#!/usr/bin/env python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html

some recommends tomlkit

'''

import sys
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

prt = rprint if USE_RICH else print

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
            import toml  # type: ignore[import]
            LoadToml.is_builtin = False
            LoadToml.is_external = True
            LoadToml.toml_lib = toml
            if not self.tomlfn is None:
                with open(self.tomlfn, 'rt', encoding='UTF-8') as f:
                    self.data = toml.load(f)
        except ModuleNotFoundError:
            #prt("cannot import tomllib...")
            self._use_another_lib()

    def _use_another_lib(self):
        ''' load built-in library '''
        if self.debug:
            prt('use built-in library tomllib')
        try:
            # tomllib is standard library provided by python 3.11
            import tomllib  # type: ignore[import]
            LoadToml.is_builtin = True
            LoadToml.is_external = False
            LoadToml.toml_lib = tomllib
            if not self.tomlfn is None:
                with open(self.tomlfn, 'rb') as f:
                    self.data = tomllib.load(f)
        except ImportError:
            prt("cannot import toml nor tomllib, exit...")
            sys.exit(1)

    def get_data(self):
        ''' get data '''
        return self.data


def test() -> None:
    ''' test '''
    prt('test()')
    obj = LoadToml('config.toml')
    obj.debug = False
    data = obj.get_data()
    # if obj.is_builtin:
    #     prt('[INFO] use builtin library')
    # else:
    #     prt('[INFO] use external library')

    if data is None:
        prt('cannot load data')
    else:
        prt(data)
        #prt(f'owner: {data["owner"]}')

if __name__ == '__main__':
    test()
