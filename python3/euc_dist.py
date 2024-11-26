#!/usr/bin/python3
# coding: utf-8

''' euclidean distance '''

import numpy as np
USE_RICH = False
try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    pass

def show(m, d):
    ''' show '''
    if USE_RICH:
        console = Console()
        console.log(f'[red]{m}[/]: {d}')
    else:
        print(f'{m}: {d}')

def main():
    ''' main '''
    m = np.array([3, 4])
    d = np.linalg.norm(m)
    show(m, d)

if __name__ == '__main__':
    main()
