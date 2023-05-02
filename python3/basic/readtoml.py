#!/usr/bin/python3
# coding: utf-8

'''
example to read config.toml
https://docs.python.org/zh-tw/dev/library/tomllib.html
'''

import sys
try:
    # tomllib is standard library provided by python 3.11
    import tomllib as tml
except ImportError:
    print("cannot import tomllib, try toml")
    try:
        # pip install toml
        import toml as tml
    except ImportError:
        print("cannot import toml")
        sys.exit(1)

import numpy as np

def test_np():
    ''' numpy vs toml '''
    n = np.arange(0, 10, dtype=np.double)
    output = {'n': n}

    t = tml.dumps(output)
    #n = [ "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0",]\n
    print(t)

    t = tml.dumps(output, encoder=toml.TomlNumpyEncoder())
    #n = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,]\n
    print(t)


def test0():
    ''' test0 '''
    # Load data from a TOML file
    with open('config.toml', 'r', encoding='utf-8') as f:
        data = tml.load(f)

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

if __name__ == '__main__':
    main()
