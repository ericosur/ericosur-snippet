#!/usr/bin/env python
'''
using sympy.factorint to factorize integers

it takes a while to load sympy (it's huge!)
'''
def show(value):
    '''
    use sympy.factorint() and display in formatted form
    '''
    from sympy import factorint
    if (value <= 0):
        print("must >= 0")
        return
    myd = factorint(value)
    # output the result...
    print value,"=",
    x = list(myd.keys())
    x.sort()
    while (True):
        key = x.pop(0)
        print key, "^", myd[key],
        if len(x) == 0: # empty
            break
        else:
            print "*",

import sys

if len(sys.argv) == 1:
    print("usage: %s [arg1] [arg2]..." % sys.argv[0])
    quit()

#for x in xrange(1, len(sys.argv)):
for x in sys.argv[1:]:
    try:
        value = int(x)
        show(value)
        print
    except ValueError:
        print("not a numeric value")
        quit()
    except:
        print("unexpected error:", sys.exc_info()[0])
        raise
