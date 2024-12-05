#!/usr/bin/env python3
# coding: utf-8

'''
platform and its path
'''

import os
import re
from sysconfig import get_platform
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

prt = rprint if USE_RICH else print
PLAT = get_platform()

def is_win() -> bool:
    ''' if platform name starts with "win" '''
    m = re.match(r'^win.+$', PLAT)
    return m is not None

def is_cygwin() -> bool:
    ''' if platform name starts with "cygwin" '''
    m = re.match(r'^cygwin.+$', PLAT)
    return m is not None

def is_linux() -> bool:
    ''' if "linux" appears in any position '''
    return 'linux' in PLAT

def yes_no(is_yes: bool, prefix=None, postfix=''):
    ''' yea or no '''
    if USE_RICH:
        yes_no_color(is_yes, prefix=prefix, postfix=postfix)
        return
    msg = ''
    if prefix:
        msg = prefix
    if is_yes:
        print(f'{msg} YES {postfix}')
    else:
        print(f'{msg} NO {postfix}')

def yes_no_color(is_yes: bool, prefix=None, postfix=''):
    ''' color version '''
    msg = prefix if prefix is not None else ''
    if is_yes:
        rprint(f'{msg} [green]YES[/] {postfix}')
    else:
        rprint(f'{msg} [red]NO[/] {postfix}')

def check_src(src: str) -> bool:
    ''' check if the src is ok '''
    #rprint(f'check_src: [yellow]{src}')
    return os.path.isdir(src)

def main():
    ''' main '''
    rprint(f"platform: {PLAT}")
    yes_no(is_win(), prefix="is_win:")
    yes_no(is_cygwin(), prefix="is_cygwin:")
    yes_no(is_linux(), prefix="is_linux:")

    # only for cygwin python, bash
    srcs = [
        '/cygdrive/c/Users/rasmus_lai/AppData/Local/Programs/Microsoft VS Code/',
        'c:/Users/rasmus_lai/AppData/Local/Programs/Microsoft VS Code/',
        r'c:\\Users\\USER\AppData\\Local\\Programs\\Python\\Launcher',
        '/ssd/node-v22.11.0-linux-x64/lib/node_modules/corepack/dist/lib',
        '/data/data/com.termux/files/home/src/ericosur-snippet/python3/basic',
    ]
    for i,d in enumerate(srcs):
        if USE_RICH:
            prefix=f'test #{i} check_src: [yellow]{d}[/]'
        else:
            prefix=f'test #{i} check_src: {d}'
        yes_no(check_src(d), prefix=prefix)

if __name__ == '__main__':
    main()
