#!/usr/bin/env python3
# coding: utf-8

'''
from 1 to 48, gcd == 1
'''

from math import gcd

def main():
    ''' main '''
    UPPER = 48
    m = []
    for v in range(1, UPPER+1):
        if gcd(v, UPPER) == 1:
            print(v)
            m.append(v)
    print('sum(m) is', sum(m))
    print('len(m) is', len(m))

if __name__ == '__main__':
    main()
