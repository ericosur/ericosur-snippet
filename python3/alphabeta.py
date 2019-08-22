#!/usr/bin/env python3
# coding: utf-8

''' alpha beta charlie '''

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


def test():
    ''' test '''
    from random import choice
    arr = get_arr()
    for _ in range(3):
        print(choice(arr))


def main(argv):
    ''' main '''
    if argv == []:
        print('alphabeta.py [arg1] [arg2] ...')
        print('\nbasic choice:')
        test()
        print()
        argv.append('hello')
        argv.append('world')

    for e in argv:
        translate(e)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
