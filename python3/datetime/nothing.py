#!/usr/bin/env python3
# coding: utf-8

'''
provide a basic function that does nothing
'''

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing'''
    return None

if __name__ == '__main__':
    print('Do not run this module directly! ' \
        'This is a module that provides function.')
