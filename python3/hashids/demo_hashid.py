#!/usr/bin/env python3
# coding: utf-8

'''
trivia sample of hashids
refer to https://github.com/davidaurelio/hashids-python
'''

from random import randint
from hashids import Hashids


def main():
    ''' main '''

    def __r():
        ''' randint '''
        return randint(101, 999)

    hashids = Hashids()
    m = hashids.encode(__r(), __r(), __r())
    print('encoded:', m)
    n = hashids.decode(m)
    print('decoded:', n)


if __name__ == '__main__':
    main()
