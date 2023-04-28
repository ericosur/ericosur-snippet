#!/usr/bin/python3
# coding: utf-8

'''
patern match (need python >= 3.10)
'''

import sys
from myutil import require_python_version


def buy(thing):
    ''' buy something '''
    match thing:
        case 'apple':
            print('It is red.')
        case 'banana':
            print('It is yellow.')
        case 'grape':
            print('It is purple.')
        case _:
            print('You cannot buy it.')

def main():
    ''' main '''
    if require_python_version(3, 10):
        print('you need python >= 3.10')
        sys.exit(1)

    buy('grape')  # It is purple.
    buy('egg')    # You cannot buy it.

if __name__ == '__main__':
    main()
