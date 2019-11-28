#!/usr/bin/env python3
# coding: utf-8

''' alpha beta charlie '''

import sys
from random import choice

def get_arr():
    ''' get_arr '''
    arr = '''
        Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India
        Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo
        Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu
    '''.strip().split()
    return arr

def translate(s):
    ''' translate '''
    # init
    arr = get_arr()
    d = {}
    for e in arr:
        d[e[0]] = e

    # start list
    print('input:', s)
    for c in list(s.upper()):
        if c in d:
            print(d[c], end=' ')
    print()


def random_pick(n: int = 3):
    ''' random_pick '''
    arr = get_arr()
    for _ in range(n):
        print(choice(arr))

def read_from_stdin():
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        args.append(line.strip())
    main(args)


def main(args: list):
    ''' main '''
    if args == []:
        print('alphabeta.py [arg1] [arg2] ...')
        print('\nrandom choice:')
        random_pick(3)
        print()
        args.append('hello')
        args.append('world')
    for e in args:
        translate(e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            read_from_stdin()
        else:
            main(sys.argv[1:])
    else:
        print('use "{} -"'.format(sys.argv[0]))
