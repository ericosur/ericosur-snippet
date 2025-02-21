#!/usr/bin/env python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html

some recommends tomlkit

'''

import sys
try:
    from rich import print as pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = pprint if USE_RICH else print

try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False
logd = logger.debug if USE_LOGURU else print

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
            if self.tomlfn is not None:
                with open(self.tomlfn, 'rt', encoding='UTF-8') as f:
                    self.data = toml.load(f)
        except ModuleNotFoundError:
            #prt("cannot import tomllib...")
            self._use_another_lib()

    def _use_another_lib(self):
        ''' load built-in library '''
        if self.debug:
            logd('use built-in library tomllib')
        try:
            # tomllib is standard library provided by python 3.11
            import tomllib  # type: ignore[import]
            LoadToml.is_builtin = True
            LoadToml.is_external = False
            LoadToml.toml_lib = tomllib
            if self.tomlfn is not None:
                with open(self.tomlfn, 'rb') as f:
                    self.data = tomllib.load(f)
        except ImportError:
            logd("cannot import toml nor tomllib, exit...")
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
    msg = "builtin library" if obj.is_builtin else "use external library"
    prt(msg)

    if data is None:
        logd('data is None')
    else:
        prt(data)
        #prt(f'owner: {data["owner"]}')

if __name__ == '__main__':
    test()
