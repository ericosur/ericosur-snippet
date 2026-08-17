#!/usr/bin/env python3

'''
platform and its path
'''

import os
import re
import sys
from sysconfig import get_platform

from basic_common import setup_local_paths

try:
    setup_local_paths()
    from madlog import get_prt
except ModuleNotFoundError:
    print('[INFO] no basic_common or madlog, exit...')
    sys.exit(1)

USE_COLOR = True
prt = get_prt()
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

def yes_no(is_yes: bool, prefix=None, postfix='') -> None:
    ''' yea or no '''
    if USE_COLOR:
        yes_no_color(is_yes, prefix=prefix, postfix=postfix)
        return
    msg = ''
    if prefix:
        msg = prefix
    if is_yes:
        print(f'{msg} YES {postfix}')
    else:
        print(f'{msg} NO {postfix}')

def yes_no_color(is_yes: bool, prefix=None, postfix='') -> None:
    ''' color version '''
    if not USE_COLOR:
        return

    msg = prefix if prefix is not None else ''
    if is_yes:
        prt(f'{msg} [green]YES[/] {postfix}')
    else:
        prt(f'{msg} [red]NO[/] {postfix}')

def check_src(src: str) -> bool:
    ''' check if the src is ok '''
    return os.path.isdir(src)

def main():
    ''' main '''
    prt(f"platform: {PLAT}")
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
        if USE_COLOR:
            prefix=f'test #{i} check_src: [yellow]{d}[/]'
        else:
            prefix=f'test #{i} check_src: {d}'
        yes_no(check_src(d), prefix=prefix)

if __name__ == '__main__':
    main()
