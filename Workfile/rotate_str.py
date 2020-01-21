#!/usr/bin/env python3
# coding: utf-8

''' rotate string '''

import itertools as it

def rotate_string(token):
    ''' rotate_string '''
    sss = [set(), set(), set()]
    for ii, cc in enumerate(list(token)):
        sss[ii].add(cc.upper())
        sss[ii].add(cc.lower())

    for x in it.product(sss[0], sss[1], sss[2]):
        print(''.join(x))


def main():
    ''' main '''
    tails = ['mp3', 'wav', 'aac', 'm4a', 'wma', 'mp4', 'wmv', 'png', 'jpg']
    for x in tails:
        rotate_string(x)
        print('-' * 20)


if __name__ == "__main__":
    main()
