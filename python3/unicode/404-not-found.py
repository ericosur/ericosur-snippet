# coding: utf-8

''' show emoji string '''

import sys

def dump(s: str):
    ''' dump '''
    for c in list(s):
        print(hex(ord(c)))

def help():
    ''' help '''
    print('parameters: show or dump(default if not provided)')
    print()

if __name__ == '__main__':
    shrug = '¯\\_(ツ)_/¯'
    if len(sys.argv) == 1:
        help()
        dump(shrug)
    else:
        if sys.argv[1] == 'show':
            print(shrug)
        elif sys.argv[1] == 'dump':
            dump(shrug)
        else:
            help()
