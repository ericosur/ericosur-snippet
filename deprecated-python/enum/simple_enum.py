#!/usr/bin/env python3
# coding: utf-8

''' simple enum '''

from __future__ import print_function
from enum import Enum

class Fruit(Enum):
    ''' enum '''
    apple = 11
    banana = 17
    orange = 19

def main():
    ''' main '''
    print('list all fruits:')
    for ff in Fruit:
        print(ff, '=', ff.value)

    try:
        print()
        print('Fruit.apple: {}'.format(Fruit.apple))
        print('Fruit.orange.value: {}'.format(Fruit.orange.value))
        print('Fruit(11): {}'.format(Fruit(11)))
        print('Fruit(2): {}'.format(Fruit(2)))
    except ValueError as e:
        print('ValueError:', e)

if __name__ == '__main__':
    main()
