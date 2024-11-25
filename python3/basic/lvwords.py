#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
levenshtein distance

'''
import Levenshtein as lt

def main():
    '''main function'''
    a = 'Chrysanthemum'
    b = 'Christopher'
    d = lt.distance(a, b)
    print(d)

if __name__ == '__main__':
    main()
