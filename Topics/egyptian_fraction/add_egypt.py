#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
use sympy to calculate egygtian style of fraction
'''

import sys
from sympy import Rational


def sum_fraction(values):
    ''' sum of egytian fraction '''
    fracts = [Rational(1, x) for x in values]
    print('sum of {}'.format(fracts))
    r = sum(fracts)
    print(r)


def read_from_stdin():
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        l = line.strip()
        vs = l.split(' ')
        args.extend(vs)
        #args.append(line.strip())
    main(args)

def main(argv):
    ''' main function '''
    vals = []
    if argv == []:  # no arguments
        print('demo values ====>')
        vals = [3, 9, 27]
    else:
        try:
            for a in argv:
                vals.append(int(a))
        except ValueError:
            print("not a numeric value")
            sys.exit()
        except:
            print("unexpected error:", sys.exc_info()[0])
            raise

    sum_fraction(vals)


if __name__ == '__main__':
    if len(sys.argv) == 1:  # no arguments
        print("Please input multiple non-zero integers")
        main([])
        sys.exit(0)

    if len(sys.argv) == 2:  # not enough arguments?
        if sys.argv[1] == '-' or sys.argv[1] == '--':
            read_from_stdin()
    else:
        main(sys.argv[1:])
