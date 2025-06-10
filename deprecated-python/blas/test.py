#!/usr/bin/env python3
# coding: utf-8

''' test np.random '''

import numpy as np

def main():
    ''' main '''
    a1 = np.random.rand(10000, 10000)
    a2 = np.random.rand(10000, 10000)
    np.dot(a1, a2)

if __name__ == '__main__':
    main()
