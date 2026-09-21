#!/usr/bin/env python3
# coding: UTF-8

'''
load some functions from __store__
'''

import sys
from pathlib import Path

try:
    this_dir = Path(__file__).resolve().parent  # top
    print(f'{this_dir=}')
    # prime_dir = this_dir.parent  # top/../
    # sys.path.insert(0, str(prime_dir))
    from store import GetConfig
except ImportError as e:
    print(f'failed to import: {e}')
    sys.exit(1)


def run_test():
    ''' try different loads '''
    conf = GetConfig()
    conf.do_tests()

def main():
    ''' main '''
    run_test()

if __name__ == '__main__':
    main()
