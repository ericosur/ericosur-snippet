#!/usr/bin/env python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html
'''

from load_toml import LoadToml


# pylint: disable=import-outside-toplevel
def test_np():
    ''' numpy vs toml '''
    import numpy as np

    print('test_np')
    n = np.arange(0, 10, dtype=np.double)
    output = {'n': n}

    obj = LoadToml.get_class()
    toml = obj.toml_lib

    if LoadToml.is_builtin:
        print('[INFO] tomllib does not support dumps()')
        return

    print('toml.dump()...')
    t = toml.dumps(output)
    #n = [ "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0",]\n
    print(t)

    t = toml.dumps(output, encoder=toml.TomlNumpyEncoder())
    #n = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,]\n
    print(t)


def test0():
    ''' test0 '''
    print('test0')

    obj = LoadToml.get_class('config.toml')
    data = obj.get_data()

    if obj.is_builtin:
        print('[INFO] use builtin library')
    else:
        print('[INFO] use external library')

    if data is None:
        print('cannot load data')
        return

    # Access data from the loaded TOML file
    print(data['title'])

    o = data['owner']
    dob = o['dob']
    print(dob, type(dob))

    d = data['clients']['wtf']
    print(f"{d['odd']=}")
    print(f'{d["even"]=}')

def main():
    ''' main '''
    test0()
    test_np()

if __name__ == '__main__':
    main()
