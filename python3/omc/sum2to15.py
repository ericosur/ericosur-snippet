#!/bin/usr/env python3
# coding:utf-8


def term(n):
    ''' given n '''
    if n < 1:
        raise ValueError
    return (n-1, n, n+1)

def mul(p):
    if p is None or len(p)!=3:
        raise ValueError
    return p[0]*p[1]*p[2]

def main():
    ''' main '''
    s=-
    for i in range(1,16):
        p = term(i)
        r = mul(p)
        print(p, r)

if __name__ == '__main__':
    main()
