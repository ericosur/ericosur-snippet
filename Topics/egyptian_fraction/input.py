#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
provide a recursive version of gcd and lcm
TODO: apply argparse
'''

import sys
from typing import List
from gcd_lcm import gcd_lcm

def read_from_stdin():
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        l = line.strip()
        vs = l.split(' ')
        args.extend(vs)
        #args.append(line.strip())
    main(args)

def main(argv: List):
    ''' main function '''
    vals = []
    if argv == []:  # no arguments
        print('demo values ====>')
        vals = [1280, 1024]
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

    # pylint: disable=unbalanced-tuple-unpacking
    [a, b] = vals
    if a == 0 or b == 0:
        print("cannot be zero")
        sys.exit(-1)

    (g, l) = gcd_lcm(a, b)
    print(f"gcd({a}, {b}) = {g}")
    print(f"({a} : {b}) = ({a/g} : {b/g})")
    print(f"lcm({a}, {b}) = {l}")


if __name__ == '__main__':
    if len(sys.argv) == 1:  # no arguments
        print("MUST input two number by argument")
        main([])
    if len(sys.argv) == 2:  # not enough arguments?
        if sys.argv[1] == '-' or sys.argv[1] == '--':
            read_from_stdin()
            sys.exit(0)
        else:
            print("NOT enough arguments, need 2, given 1")
            sys.exit(-2)
    if len(sys.argv) == 3:
        main(sys.argv[1:])
