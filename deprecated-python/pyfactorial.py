#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
a very trival script to show how to use sympy.factorint()
to factorize an integer (or determine a prime?)

needed module: sympy
'''
from __future__ import print_function
from sympy import factorint

def main():
    ''' main function '''
    while True:    # input value <= zero to exit
        val = input("input an postive integer (0 to quit): ")
        val = int(val)
        if val <= 0:
            break
        fdict = factorint(val)
        print(fdict)

if __name__ == '__main__':
    main()
