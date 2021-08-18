#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
using sympy.factorint to factorize integers

it takes a while to load sympy (it's huge!)
'''

import sys
from random import randint
from sympy import factorint

# pylint: disable=import-error
# pylint: disable=unused-import
# for pythonista
#import clipboard
HAS_CONSOLE_MODULE = False
try:
    import console
    HAS_CONSOLE_MODULE = True
except ImportError:
    print('No console module of pythonista')

def show(value):
    '''
    use sympy.factorint() and display in formatted form
    '''
    assert value >= 0

    # factorint() will return dict with factor and its
    myd = factorint(value)
    # output the result...
    msg = ''
    msg = '{} = '.format(value)
    #print(value, "= ", end='')
    arr = list(myd.keys())
    arr.sort()
    isFirst = True
    for key in arr:
        if not isFirst:
            #print(" * ", end='')
            msg = msg + ' * '
        else:
            isFirst = False
        val = myd[key]
        if val == 1:
            msg = msg + '{}'.format(key)
            #print(key, end='')
        else:
            #print("{}**{}".format(key, myd[key]), end='')
            msg = msg + "{}**{}".format(key, myd[key])
    if HAS_CONSOLE_MODULE:
        console.alert(msg)
    else:
        print(msg)

def main(argv: list):
    '''main function'''
    if argv == []:
        print("usage: factoring.py [arg1] [arg2]...")
        print()

        for _ in range(3):
            argv.append(randint(1001, 9999))

    for x in argv:
        try:
            value = int(x)
            show(value)
            print()
        except ValueError:
            print("not a numeric value:", x)
            continue
        # except:
        #     print("unexpected error:", sys.exc_info()[0])
        #     continue

def run_this():
    ''' run this at pythonista '''
    ret = console.input_alert('input a number')
    argv = []
    try:
        val = int(ret)
        if val <= 0:
            raise ValueError
    except ValueError:
        print('{} not a number'.format(ret))
        val = randint(1001, 99999)
        print('invalid number, use random number:', val)
    argv.append(val)
    main(argv)


if __name__ == '__main__':
    if HAS_CONSOLE_MODULE:
        run_this()
    else:
        main(sys.argv[1:])
