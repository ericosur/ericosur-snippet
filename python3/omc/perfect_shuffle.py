#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
https://en.wikipedia.org/wiki/Faro_shuffle
'''

# implement fisher-yates shuffle in python

def shuffle_array(arr):
    '''shuffle array using fisher'''
    half = len(arr) // 2
    p = arr[:half]
    q = arr[half:]
    res = []
    for i in range(half):
        res.append(p[i])
        res.append(q[i])
    return res

def show_array(arr):
    '''dump array'''
    print(arr)

def main():
    '''main function'''
    ARRAY_SIZE = 10
    REPEAT = 10

    arr = list(range(1,ARRAY_SIZE+1))
    show_array(arr)
    for i in range(1,REPEAT+1):
        print(i, "==>")
        new_arr = shuffle_array(arr)
        show_array(new_arr)
        arr = new_arr

if __name__ == '__main__':
    main()
