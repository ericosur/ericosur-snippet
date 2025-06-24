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

class Solution():
    ''' Solution class to query font names '''
    fn_magic = "magick-fonts.txt"
    fn_fclist = "fclist-fonts.txt"

    def __init__(self):
        self.fonts = []

    @classmethod
    def run(cls) -> None:
        ''' run the solution '''
        sol = cls()
        sol.run_fclist()
        sol.run_magick()

    def output_to_file(self, fn: str) -> None:
        ''' output the fonts to a file '''
        if not self.fonts:
            logd('no fonts found')
            return
        with open(fn, 'wt', encoding='utf-8') as f:
            for font in self.fonts:
                f.write(font + '\n')
        logd(f'output fonts to: {fn}')

    def run_fclist(self) -> None:
        ''' run_fclist and show the reulst '''
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
        self.fonts = sorted(list(fonts))
        self.output_to_file(self.fn_fclist)

    def run_magick(self) -> None:
        ''' run magick and show the reulst '''
        outs = run_command("magick -list font")
        fonts = set()
        for i in outs:
            m = re.match(r'^\s*Font: (.+)', i)
            if m:
                font_name = m.group(1).strip()
                fonts.add(font_name)
        self.fonts = sorted(list(fonts))
        self.output_to_file(self.fn_magic)

def main():
    ''' main '''
    Solution.run()

if __name__ == "__main__":
    main()
