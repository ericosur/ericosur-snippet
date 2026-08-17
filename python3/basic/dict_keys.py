#!/usr/bin/env python3

'''
simple python dict usage
'''

import sys

from basic_common import setup_local_paths

try:
    setup_local_paths()
    from madlog import get_prt
except ModuleNotFoundError:
    print('[INFO] no basic_common or madlog, exit...')
    sys.exit(1)

prt = get_prt()

def main():
    '''main function'''
    d = {'name':'bob', 'number':99, 'phone':'123456789'}
    for key, value in d.items():
        prt(f"{key} => {value}")


if __name__ == '__main__':
    main()
