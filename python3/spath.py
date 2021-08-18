#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
get current path setting and split it
then list them
'''

# single line alias version:
# alias path='echo $PATH | sed "s/:/\n/g"'

import os

USE_COLOR = False
try:
    from colorama import Fore, Style
    USE_COLOR = True
except ImportError:
    pass


def main():
    ''' main '''

    PATH = os.environ['PATH']
    # or this way:
    #    str = os.getenv('path')

    warnlist = []
    for i in PATH.split(os.pathsep):
        if os.path.isdir(i):
            print(i)
        else:
            if not i in warnlist:
                warnlist.append(i)
    if USE_COLOR:
        print(Fore.YELLOW)
    for w in warnlist:
        print('[WARN] path not exists:', w)
    if USE_COLOR:
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    main()
