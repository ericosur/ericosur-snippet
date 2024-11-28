#!/usr/bin/env python3
# coding: utf-8

'''
This scripts tries to sort a list of 3-element tuples.
Sort by the first value, then the 2nd value, ...
'''


def test():
    ''' test '''
    values = [
        (5,23,99), (3,5,71), (3,5,9), (5,11,107),
        (9,13,47), (2,4,6), (1,3,19), (2,8,18)]

    print(values)
    new_vals = sorted(values, key=lambda x: (x[0], x[1], x[2]))
    print(new_vals)

if __name__ == '__main__':
    test()
