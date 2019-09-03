#!/usr/bin/python
# -*- coding: utf-8 -*-
#

'''
    practice for getting environment variables

    The way to get env var:
        os.environ.get('PATH')
    OR
        os.getenv('PATH')

    may input argument from CLI, or nothing to see demo
'''

import sys
import os

def pick_one():
    ''' pick one element from os.environ '''
    from random import choice
    print('random choose one env variable to show:')
    arr = [x for x in os.environ]
    k = choice(arr)
    en = os.environ.get(k)
    print('{} = {}'.format(k, en))

def main(argv):
    ''' main function '''
    if argv == []:
        assert False    # should not happen

    for x in argv:
        en = os.environ.get(x)
        print('{} = {}'.format(x, en))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("usage: argv_env.py [arg1] [arg2]...\n")
        pick_one()
