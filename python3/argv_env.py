#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
from random import choice

def main(argv):
    ''' main function '''
    if argv == []:
        print('random choose one env variable to show:')
        argv.append(choice(list(os.environ)))

    for x in argv:
        en = os.environ.get(x)
        print('{} = {}'.format(x, en))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("usage: argv_env.py [arg1] [arg2]...\n")
        main([])
