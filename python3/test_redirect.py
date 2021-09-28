#!/usr/bin/env python3
# coding: utf-8

'''
test script for redirect stderr, stdout

use 2>&1 to combine stdout and stderr into one
it is buffered

python3 test_redirect.py > out.txt 2>&1
python3 test_redirect.py 2>&1 | tee out.txt

'''

import sys
from myutil import print_stderr

def main():
    ''' main '''
    rep = 1000000
    try:
        for i in range(rep):
            print(f'stdout: {i}')
            print_stderr(f'stderr: {i}')
    except KeyboardInterrupt:
        print(f'KeyboardInterrupt at: {i}')
        sys.exit(1)

if __name__ == '__main__':
    main()
