#!/usr/bin/env python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html
'''

import numpy as np
from load_toml import LoadToml
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


def test_np():
    ''' numpy vs toml '''
    logd('test_np')
    n = np.arange(0, 10, dtype=np.double)
    output = {'n': n}

    obj = LoadToml('config.toml')
    toml = obj.toml_lib

    if obj.is_builtin:
        prt('[INFO] tomllib does not support dumps(), exit...')
        return

    prt('toml.dumps(output) =====>')
    t = toml.dumps(output)
    #n = [ "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0",]\n
    prt(t)

    prt("toml.dumps(... encoder...) =====>")
    t = toml.dumps(output, encoder=toml.TomlNumpyEncoder())
    #n = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,]\n
    prt(t)


def test0():
    ''' test0 '''
    logd('test0')

    obj = LoadToml('config.toml')
    data = obj.get_data()

    the_type = "builtin" if obj.is_builtin else "external"
    prt(f'obj uses {the_type} library')

    if data is None:
        logd('data is None')
        return

    # Access data from the loaded TOML file
    prt(f"date['title']: {data['title']}")

    o = data['owner']
    dob = o['dob']
    prt('date in the owner section...')
    prt(dob, type(dob))

    d = data['clients']['wtf']
    prt(f"{d['odd']=}")
    prt(f'{d["even"]=}')

def main():
    ''' main '''
    test0()
    prt('-' * 66)
    test_np()

if __name__ == '__main__':
    main()
