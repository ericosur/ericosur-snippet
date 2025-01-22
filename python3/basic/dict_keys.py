#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
simple python dict usage
'''
try:
    from rich import print as pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = pprint if USE_RICH else print

def main():
    '''main function'''
    d = {'name':'bob', 'number':99, 'phone':'123456789'}
    for key, value in d.items():
        prt(f"{key} => {value}")

    # pylint not recommend:
    #for key in d.keys():
    #    print(key, '=>', d[key])

if __name__ == '__main__':
    main()
