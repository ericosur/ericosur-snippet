#!/usr/bin/env python3
# coding: utf-8

'''
demo of module filetype
'''

import os
import sys
from myutil import read_from_stdin

try:
    import filetype
except ImportError as e:
    print(e)
    sys.exit(1)

def call_guess(f: str):
    ''' call filetype.guess '''
    if not os.path.exists(f):
        print('file not found:', f)
        return

    kind = filetype.guess(f)
    if kind:
        print('{}\t{}\t{}'.format(f, kind.extension, kind.mime))
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
        print('use "{} -" read input from STDIN'.format(sys.argv[0]))
        # demo mode
        print('demo mode...')
        main(['/home/rasmus/Pictures/data/lena.jpg'])
        sys.exit()

    if sys.argv[1] == '-':
        read_from_stdin(main)
    else:
        main(sys.argv[1:])
