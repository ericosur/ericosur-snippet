#!/usr/bin/env python3
# coding: utf-8

'''
demo of module filetype
'''

import sys
from myutil import read_from_stdin, isfile

try:
    import filetype  # type: ignore[import]
except ImportError as e:
    print('ImportError:', e)
    sys.exit(1)


def call_guess(f: str):
    ''' call filetype.guess '''
    if not isfile(f):
        print('file not found:', f)
        return

    kind = filetype.guess(f)
    if kind:
        print(f'{f}\t{kind.extension}\t{kind.mime}')
    else:
        print('cannot determine such file:', f)


def main(argv):
    ''' main '''
    if argv == []:
        print('need specify filenames...')
        sys.exit()

    for f in argv:
        try:
            call_guess(f)
        except ValueError:
            print('not a value:', f)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f'use "{sys.argv[0]} -" read input from STDIN')
        # demo mode
        print('demo mode...')
        main(['/home/rasmus/Pictures/data/lena.jpg'])
        sys.exit()

    if sys.argv[1] == '-':
        read_from_stdin(main)
    else:
        main(sys.argv[1:])
