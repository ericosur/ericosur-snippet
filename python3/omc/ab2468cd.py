#!/usr/bin/python3
# coding: utf-8

'''
from (1,40) pick a,b (a<b and a!=b)
sum of a and b is 4m
'''

import itertools as it

def get_productsum(a,b,c,d):
    ''' get ab + bc + db + ac '''
    return a*b + b*c + d*b + a*c

def main():
    ''' main '''
    symbols = [2, 4, 6, 8]
    for n in it.permutations(symbols, 4):
        (a, b, c, d) = n
        r = get_productsum(a,b,c,d)
        print(n, r)

if __name__ == '__main__':
    main()
