#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

USE_ANSICOLOR = False
try:
    from colorama import Fore, init
    USE_ANSICOLOR = True
except ImportError:
    print('[info] suggest install colorama to enable ansi color')

def logd(*args, **wargs):
    ''' logd '''
    print(*args, **wargs, file=sys.stderr)

def colorlog(color, msg):
    ''' color log '''
    if USE_ANSICOLOR:
        print(color+msg)
    else:
        print(msg)

class PathLister():
    ''' list path '''
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
        if USE_ANSICOLOR:
            self.report_in_colorama()
        else:
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
        if self.dirs:
            for d in self.dirs:
                print(d)
        if self.dups:
            print('-'*20, "duplicated", '-'*20)
            for d in self.dups:
                print(d)
        if self.ngs:
            print('-'*20, "not found", '-'*20)
            for d in self.ngs:
                print(d)

    def report_in_colorama(self):
        ''' use colorama '''
        logd('report_in_colorama')
        init(autoreset=True)
        for d in self.dirs:
            print(d)
        # not found
        for d in self.ngs:
            colorlog(Fore.RED, f'[NOT FOUND] {d}')
        # warn: duplicated
        for d in self.dups:
            colorlog(Fore.YELLOW, f'[DUPLICATED] {d}')

def main():
    ''' main '''
    PathLister.run()

if __name__ == '__main__':
    main()
