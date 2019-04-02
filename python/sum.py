#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' just a trivia script to use foo-loop and print '''

from __future__ import print_function

def main():
    '''main function'''
    t = 0
    max_size = 100

    # sum from 0 to 100
    for i in range(max_size + 1):
        t += i

    print("sum from 1 to %d: %d" % (max_size, t))

if __name__ == '__main__':
    main()
