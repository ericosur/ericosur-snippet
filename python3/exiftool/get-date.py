#!/usr/bin/env python3

'''
get-date.py: to get the last modified date of files in current directory
'''

import os
from glob import glob


def main():
    ''' main '''
    MAX_FILES = 5
    files = glob('*.jpg')
    for cnt, f in enumerate(files, 1):
        d = os.path.getmtime(f)
        print(f'({cnt}) {f}: {d}')
        if cnt >= MAX_FILES:
            break

if __name__ == '__main__':
    main()
