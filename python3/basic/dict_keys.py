#!/usr/bin/env python3

'''
simple python dict usage
'''

from basic_common import setup_local_paths

setup_local_paths()
from madlog import get_prt

prt = get_prt()

def main():
    '''main function'''
    d = {'name':'bob', 'number':99, 'phone':'123456789'}
    for key, value in d.items():
        prt(f"{key} => {value}")


if __name__ == '__main__':
    main()
