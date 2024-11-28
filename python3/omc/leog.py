#!/usr/bin/env python3
# coding: utf-8

'''
find one square
'''

def one_square(n):
    ''' square '''
    t = 2 * n
    for _ in range(n-2):
        t += 2
    return t

def main():
    ''' main '''
    for x in range(9, 9+5):
        r = one_square(x)
        print(x, r)

if __name__ == '__main__':
    main()
