#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
get current path setting and split it
then list them
'''

# single line alias version:
# alias path='echo $PATH | sed "s/:/\n/g"'

import os


USE_ANSICOLOR = False
try:
    from colorama import Fore, init
    USE_ANSICOLOR = True
except ImportError:
    print('[info] suggest install colorama to enable ansi color')


def colorlog(color, msg):
    ''' color log '''
    if USE_ANSICOLOR:
        print(color+msg)
    else:
        print(msg)

def main():
    ''' main '''

    PATH = os.environ['PATH']
    dirs = []

    if USE_ANSICOLOR:
        init(autoreset=True)

    for d in PATH.split(os.pathsep):
        if not os.path.isdir(d):
            # warn: not found
            colorlog(Fore.RED, f'[NOT FOUND] {d}')
        else:
            if d in dirs:
                # warn: duplicated
                colorlog(Fore.YELLOW, f'[DUPLICATED] {d}')
            else:
                dirs.append(d)
                print(d)

if __name__ == '__main__':
    main()
