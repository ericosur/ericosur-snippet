#!/usr/bin/env python3
# coding: utf-8

''' ordered dict '''

from collections import OrderedDict

def get_dict():
    ''' get_dict '''

    params = OrderedDict(
        [('bcid', 'ean13'), ('text', 'hello world'), ('scale', 3),
         ('rotate', 'N'), ('includetext', 'null')]
    )
    print(params)

def main():
    ''' main '''
    get_dict()

if __name__ == '__main__':
    main()
