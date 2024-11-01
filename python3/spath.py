#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

'''
get current path setting and split it
then list them

for ansi color (optional):
    - colorama
    - rich
'''

# single line alias version:
# alias path='echo $PATH | sed "s/:/\n/g"'

import os
import sys

DEBUG = False
USE_RICH = False
USE_ANSICOLOR = False

def logd(*args, **wargs):
    ''' logd '''
    if DEBUG:
        print(*args, **wargs, file=sys.stderr)

try:
    import rich
    USE_RICH = True
except ImportError:
    logd("no rich, use __pip install rich__")

if not USE_RICH:
    try:
        from colorama import Fore
        from colorama import init as color_init
        USE_ANSICOLOR = True
    except ImportError:
        logd("no colorama, use __pip install colorama__")
else:
    Fore = None
    color_init = None

logd(f'{USE_RICH=}')
logd(f'{USE_ANSICOLOR=}')

def colorlog(color, msg):
    ''' color log '''
    if USE_ANSICOLOR:
        print(color+msg)
    else:
        print(msg)

class PathLister():
    ''' list path '''
    STR_DUP = '-'*20 + ' duplicated ' + '-'*20
    STR_NG = '-'*20 + ' not found ' + '-'*20
    def __init__(self):
        self.dirs = []
        self.ngs = []
        self.dups = []
        self.__check_path__()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

    def action(self):
        ''' acton '''
        if USE_RICH:
            self.report_in_rich()
            return
        if USE_ANSICOLOR:
            self.report_in_colorama()
            return
        self.report()

    def __check_path__(self):
        ''' check paths '''
        p = os.environ['PATH']
        for d in p.split(os.pathsep):
            if os.path.isdir(d):
                if d in self.dirs: # duplicates
                    self.dups.append(d)
                else:
                    self.dirs.append(d)
            else:
                self.ngs.append(d)

    def report(self):
        ''' report '''
        for d in self.dirs:
            print(d)
        if self.dups:
            print(PathLister.STR_DUP)
            for d in self.dups:
                print(d)
        if self.ngs:
            print(PathLister.STR_NG)
            for d in self.ngs:
                print(d)

    def report_in_colorama(self):
        ''' use colorama '''
        logd('report_in_colorama')
        color_init(autoreset=True)
        for d in self.dirs:
            print(d)
        # not found
        for d in self.ngs:
            colorlog(Fore.RED, f'[NOT FOUND] {d}')
        # warn: duplicated
        for d in self.dups:
            colorlog(Fore.YELLOW, f'[DUPLICATED] {d}')

    def report_in_rich(self):
        ''' in rich '''
        logd('will use rich')
        rp = rich.print
        for d in self.dirs:
            rp(d)
        if self.dups:
            rp('[bold yellow]'+self.STR_DUP)
            for d in self.dups:
                rp(d)
        if self.ngs:
            rp('[bold red]'+self.STR_NG)
            for d in self.ngs:
                rp(d)

def main():
    ''' main '''
    PathLister.run()

if __name__ == '__main__':
    main()
