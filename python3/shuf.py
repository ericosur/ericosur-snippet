#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
a simple demo to ultilize function in the other script
'''


import random
import numpy as np


def shuffle_array(arr):
    ''' shuffle array using fisher
        will change arr
    '''
    n = len(arr)
    while n > 1:
        k = random.randint(0, n-1)
        n = n - 1
        arr[n], arr[k] = arr[k], arr[n]
        '''
        if SHOW_STEP:
            print('k:{} exchange:{} and {}'.format(k, arr[n], arr[k]))
            show_array(arr)
        '''


def main():
    ''' demo multiple way to shuffle a numeric list '''
    SIZE = 40
    vals = [i for i in range(SIZE)]
    shuffle_array(vals)
    print(vals)

    vals = [i for i in range(SIZE)]
    random.shuffle(vals)
    print(vals)

    vals = [i for i in range(SIZE)]
    np.random.shuffle(vals)
    print(vals)


if __name__ == '__main__':
    main()
