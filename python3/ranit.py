#!/usr/bin/env python3
# coding: utf-8

'''
get some random 4 digit numbers
'''

import random

def main():
    ''' main '''
    for _ in range(10):
        r = random.randint(1000, 9999)
        print(r, divmod(r, 7))
        if r % 7 == 0:
            print('{} is seven multiple...'.format(r))


if __name__ == '__main__':
    main()
