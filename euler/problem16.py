#!/usr/bin/env python3
# coding: utf-8

'''
http://projecteuler.net/problem=16
'''

def main():
    ''' main '''
    N = 2**1000
    chars = list(str(N))
    ints = list(map(int, chars[:]))
    print('len:', len(ints))
    s = sum(ints)
    print('sum:', s)

if __name__ == '__main__':
    main()
