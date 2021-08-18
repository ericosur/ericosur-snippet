#!/usr/bin/python3
# coding: utf-8

'''
simple script to get sphere volume and surface area
'''

import math
import sys

def main(argv):
    ''' The volume of a sphere is V = 4/3 πr³
        The surface area of a sphere of radius r is A = 4 πr*r
    '''
    for t in argv:
        try:
            r = float(t)
            r2 = r * r
            #c = math.pi * r2
            a = 4.0 * math.pi * r2
            v = 4.0 / 3.0 * math.pi * r2 * r
            print('r: {}, a: {:.3f}, v: {:.3f}'.format(r, a, v))
        except ValueError:
            print('value error')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main([10, 20, 30])
