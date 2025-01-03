#!/usr/bin/env python3
# coding: utf-8

'''
simple gcd runner with argparse

NOTE: use math.gcd() or local gcd
'''

import argparse

# local implementation of gcd
from the_gcd import gcd
# official math.gcd
#from math import gcd as math_gcd

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='calculate Greatest Common Divisor')
    parser.add_argument("n1", type=int, nargs='?', default=1024)
    parser.add_argument("n2", type=int, nargs='?', default=768)
    args = parser.parse_args()

    r = gcd(args.n1, args.n2)
    print(f'gcd({args.n1}, {args.n2}) = {r}')

if __name__ == '__main__':
    main()
