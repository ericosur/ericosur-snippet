# coding: utf-8

''' show emoji string '''

import sys

SHRUG = '¯\\_(ツ)_/¯'

def dump(s: str):
    ''' dump '''
    for c in list(s):
        print(hex(ord(c)))

def help_message():
    ''' help '''
    print('parameters: show or dump(default if not provided)')
    print()

if __name__ == '__main__':

    if len(sys.argv) == 1:
        help()
        dump(SHRUG)
    else:
        if sys.argv[1] == 'show':
            print(SHRUG)
        elif sys.argv[1] == 'dump':
            dump(SHRUG)
        else:
            help_message()
