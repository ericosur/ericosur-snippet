#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
try to call my own functions
'''

from __future__ import print_function
from gcd import gcd
from whokme import who_kick_me

def show_result(mm, nn):
    ''' show gcd result '''
    print("gcd({}, {}) = {}".format(mm, nn, gcd(mm, nn)))

def show_kick_me_result():
    ''' demo who_kick_me() '''
    ##a = (1, 2, 3, 4)
    ##b = [1, 2, 3, 4]
    who_kick_me()

def main():
    ''' main function '''
    show_result(128, 160)

if __name__ == '__main__':
    main()
