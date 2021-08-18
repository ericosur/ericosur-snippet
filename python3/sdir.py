#!/usr/bin/env python3
# coding: utf-8

"""
try to locate specified name in PATH
"""

import os
import sys


def main(args: list):
    ''' input list of items to search '''
    if args == []:
        d = 'git'
        print('demo: use "{}"'.format(d))
        args.append(d)

    res = os.environ['PATH']

    for a in args:
        found = False
        for p in res.split(os.pathsep):
            fp = p + '/' + a
            if os.path.isfile(fp):
                print('found: {}'.format(fp))
                found = True
        if not found:
            print('not found: {}'.format(a))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print('specify arg to search in PATH')
        main([])
