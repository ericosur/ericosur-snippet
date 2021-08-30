#!/usr/bin/python3
# coding: utf-8

'''
simple script to get sphere volume and surface area
'''

import argparse
import math
import sys

def calc_sphere(t):
    '''
    The volume of a sphere is V = 4/3 πr³
    The surface area of a sphere of radius r is A = 4 πr*r
    '''
    try:
        r = float(t)
        r2 = r * r
        #c = math.pi * r2
        a = 4.0 * math.pi * r2
        v = 4.0 / 3.0 * math.pi * r2 * r
        print('r: {}, a: {:.3f}, v: {:.3f}'.format(r, a, v))
    except ValueError:
        print('value error:', t)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("values", metavar='value', type=str, nargs='*',
        help="show these strings")
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='show information about sphere')

    args = parser.parse_args()

    if args.verbose:
        print(__doc__)
        print(calc_sphere.__doc__)
        sys.exit(1)

    if not args.values:
        print(__doc__)
        print("demo mode...")
        args.values.extend([10, 20, 30])

    #print('input:', args.values)
    for t in args.values:
        calc_sphere(t)

if __name__ == '__main__':
    main()
