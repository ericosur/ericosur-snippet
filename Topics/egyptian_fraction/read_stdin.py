#!/usr/bin/env python3
# coding: utf-8

'''
common function to read from stdin and type casting to int,
then calling specified func
'''

import sys

__version__ = '0.0.1'

def read_from_stdin(func):
    ''' read from stdin and call process with List[int]'''
    args = []
    try:
        for ln in sys.stdin:
            ln = ln.strip()
            if len(ln):
                vs = ln.split(' ')
            else:   # skip if blank/empty
                continue
            if len(vs): # type cast to List[int]
                ws = [int(x) for x in vs]
            if len(ws):
                args.extend(ws)
        if len(args) == 0:
            print('nothing from STDIN')
            sys.exit(2)
        func(args)

    except ValueError:
        print('read_stdin.py: ValueError:', sys.exc_info()[0])
        sys.exit(1)

if __name__ == '__main__':
    print('This is a module, cannot run standalone')
