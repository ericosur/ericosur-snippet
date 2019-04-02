#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
using sympy.factorint to factorize integers

it takes a while to load sympy (it's huge!)
'''

from __future__ import print_function
import sys

def show(value):
    '''
    use sympy.factorint() and display in formatted form
    '''
    from sympy import factorint
    if value <= 0:
        print("must > 0")
        return
    # factorint() will return dict with factor and its
    myd = factorint(value)
    # output the result...
    print(value, "= ", end='')
    x = list(myd.keys())
    x.sort()
    isFirst = True;
    for key in x:
        if not isFirst:
            print(" * ", end='')
        else:
            isFirst = False
        val = myd[key]
        if val == 1:
            print(key, end='')
        else:
            print("{}**{}".format(key, myd[key]), end='')



def main():
    '''main function'''
    if len(sys.argv) == 1:
        print("usage: %s [arg1] [arg2]..." % sys.argv[0])
        quit()

    #for x in xrange(1, len(sys.argv)):
    for x in sys.argv[1:]:
        try:
            value = int(x)
            show(value)
            print()
        except ValueError:
            print("not a numeric value")
            quit()
        except:
            print("unexpected error:", sys.exc_info()[0])
            raise

if __name__ == '__main__':
    main()
