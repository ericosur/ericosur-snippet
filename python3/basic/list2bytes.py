#!/usr/bin/env python3
# coding: utf-8

'''
demo: convert a list of integers into numpy array and make slice

require hexdump and numpy
'''

from hexdump import hexdump # type: ignore[import]
import numpy as np


def main():
    ''' main '''
    slice_size = 7
    slice_num = 4

    # python method:
    # vals = [ x for x in range(slice_size*slice_num) ]
    # numpy method:
    vals = np.arange(slice_size * slice_num)
    a = np.array(vals, dtype=np.uint8)
    print(a)

    #print(len(a))
    hexdump(a)
    print('-' * 60)
    for i in range(len(a)//slice_size):
        pivot = i * slice_size
        s = a[pivot : pivot+slice_size]
        hexdump(s)
        print('-' * 60)

if __name__ == '__main__':
    main()
