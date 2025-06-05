#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
call ifconfig and parse the output
'''

import os
import re
import sys
try:
    from rich import print as pprint
    from rich.console import Console
    from rich.table import Table
    RICH_ENABLED = True
    prt = pprint
    console = Console()
    logd = console.log
except ImportError:
    prt = print
    logd = print
    RICH_ENABLED = False
try:
    sys.path.insert(0, '../../python3/')
    from myutil import run_command
except ImportError:
    print('Cannot import myutil, please check the module path.')
    sys.exit(1)

def test() -> None:
    ''' test '''
    outs = run_command("fc-list :lang=zh:family")
    fonts = set()
    for i in outs:
        m = re.match(r'^([^:]+):([^:]+):([^:]+)', i)
        if m:
            #font_file = m.group(1).strip()
            font_name = m.group(2).strip()
            #font_style = m.group(3).strip()
            fonts.add(font_name)
        else:
            logd('no match for', i)
    fonts = sorted(list(fonts))
    for i in fonts:
        prt(i)

def main():
    ''' main '''
    test()

if __name__ == "__main__":
    main()
