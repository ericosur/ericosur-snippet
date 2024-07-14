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
    from colorama import Fore, Style
    USE_ANSICOLOR = True
except ImportError:
    print('[info] suggest install colorama to enable ansi color')


def logd(self, *args, **wargs):
    ''' logd, output to file if available, else to stdout '''
    useColor = False
    if 'useColor' in wargs:
        useColor = wargs.pop('useColor')
    if USE_ANSICOLOR and useColor:
        print(Fore.YELLOW, end='')
    print(*args, **wargs)
    if USE_ANSICOLOR and useColor:
        print(Style.RESET_ALL, end='')

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
    for w in warnlist:
        logd('[WARN] path not exists:', w)

if __name__ == '__main__':
    main()
