#!/usr/bin/python3
# coding: utf-8

'''
simple gcd runner with argparse
'''

import argparse
from gcd import gcd

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
