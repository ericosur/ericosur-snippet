#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
levenshtein distance
'''
import sys
try:
    import Levenshtein as lt  # type: ignore[import]
except ImportError:
    print('module Levenshtein is required...')
    sys.exit(1)

def main():
    '''main function'''
    a = 'Chrysanthemum'
    b = 'Christopher'
    d = lt.distance(a, b)
    print(d)

if __name__ == '__main__':
    main()
