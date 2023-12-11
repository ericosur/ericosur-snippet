#!/usr/bin/env python3
# coding: utf-8

''' read digits from big file '''

from goab import get_pipath


def get_pos(x):
    ''' because sequence start with "3." remove it '''
    start = 2
    if x >= 9:
        start = x - 10 + 2
    return start

def test():
    ''' test '''
    try:
        with open(get_pipath(), 'rt') as pi:
            for p in [10, 768, 1e6, 1e7, 1e8, 1e9]:
                _p = int(p)
                pi.seek(get_pos(_p), 0)
                buf = pi.read(10)
                print('{}: {}'.format(_p, buf))
    except FileNotFoundError as e:
        print('except:', e)

def main():
    ''' main '''
    test()

if __name__ == '__main__':
    main()
