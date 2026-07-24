#!/usr/bin/env python3

'''
call ifconfig and parse the output
'''

import os
import re
import sys

try:
    #from rich import print as pprint
    from rich.console import Console
    from rich.pretty import pprint
    RICH_ENABLED = True
    prt = pprint
    console = Console()
    logd = console.log
except ImportError:
    RICH_ENABLED = False
    prt = print
    logd = print

try:
    sys.path.insert(0, './')
    sys.path.insert(0, '../')
    sys.path.insert(0, 'python3/')
    home = os.environ.get('HOME')
    abs_path = os.path.join(home, 'src/ericosur-snippet/python3')
    sys.path.insert(0, abs_path)
    from myutil import (  # type: ignore[import]
        is_linux,
        run_command,  # type: ignore[import]
        show_platform,
    )
except ImportError:
    print("cannot import local modules")

def run_in_termux() -> bool:
    ''' get prefix '''
    p = os.environ.get('PREFIX')
    if p is None:
        return False
    p = p.decode('utf-8')
    return "com.termux" in p

def get_macaddr():
    ''' get mac addr via ip '''
    cmd = "adb shell ip link show wlan0"
    outs = run_command(cmd)
    if outs is None:
        prt("No output from command: " + cmd)
        return ""
    ret = ""
    for ln in outs:
        reg = r'link/ether (\S+)'
        mac = re.search(reg, ln)
        if mac:
            ret = f'{mac.group(1)}'
            break
    return ret

def main():
    ''' main '''
    if not is_linux():
        prt('this script is for Linux only')
        show_platform()
        return

    # note: if returns has no inet, it will be removed
    ret = get_macaddr()
    print('wtf')
    print(type(ret))
    print(ret)

if __name__ == "__main__":
    main()
