#!/usr/bin/python3
# coding: utf-8

'''
from (1,40) pick a,b (a<b and a!=b)
sum of a and b is 4m
'''

import itertools as it


def get_one2n(n):
    ''' sum of 1 .. n '''
    t = (1+n)*n/2
    a = t / n
    return t, a

def main():
    ''' main '''
    vals = []
    limit = 2015
    for i in range(999999,1,-1):
        t, a = get_one2n(i)
        if a <= limit:
            print(t, a, i)
            break



if __name__ == '__main__':
    main()
