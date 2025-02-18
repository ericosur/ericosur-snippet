#!/usr/bin/env python3
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

import argparse
import os
from sysconfig import get_platform
from typing import Any

# while import stage, do not use logd
DIAG_IMPORT = False
HAS_RICH = False
HAS_ANSICOLOR = False

try:
    import rich
    HAS_RICH = True
except ImportError:
    if DIAG_IMPORT:
        print("no rich, use __pip install rich__")

try:
    from colorama import Fore
    from colorama import init as color_init
    HAS_ANSICOLOR = True
except ImportError:
    if DIAG_IMPORT:
        print("no colorama, use __pip install colorama__")

try:
    from loguru import logger
    HAS_LOGGER = True
except ImportError:
    HAS_LOGGER = False

def colorlog(color, msg):
    ''' color log '''
    if HAS_ANSICOLOR:
        print(color+msg)
    else:
        print(msg)

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

class PathLister():
    ''' list path '''
    STR_DUP = '-'*20 + ' duplicated ' + '-'*20
    STR_NG = '-'*20 + ' not found ' + '-'*20

    def __init__(self, args: Any):
        self.args = args
        self.alldirs: dict[str, list[str]] = {'dirs': [], 'ngs': [], 'dups': []}
        if args.debug:
            self.logd = logger.debug if HAS_LOGGER else print
        else:
            self.logd = do_nothing
        self.__check_path__()
        self.is_windows = None
        self.is_rdp = None
        self.__check_platform__()
        self.use_rich = False
        self.use_ansi = False
        self.__determine_color__()
        if args.debug:
            self.dump_vars()

    def __determine_color__(self):
        ''' determine which color library to use
            use rich first, then colorama, then normal print
        '''
        logd = self.logd
        use_rich = self.args.rprint
        use_ansi = self.args.ansi
        if use_rich:
            if HAS_RICH:
                logd("has rich, and apply")
                self.use_rich = True
            else:
                logd("request rich, but no rich")
        if use_ansi:
            if HAS_ANSICOLOR:
                logd("has ansi, and apply")
                self.use_ansi = True
            else:
                logd("request ansi, but no ansi to use")

    def __check_platform__(self):
        ''' check platform '''
        logd = self.logd
        platform = get_platform()
        logd(f'platform: {platform}')
        self.is_windows = "win" in platform
        if self.is_windows:
            _s = os.getenv("SESSIONNAME")
            if _s:
                logd(f'session: {_s}')
                self.is_rdp = "RDP" in _s

    def dump_vars(self):
        ''' dump vars '''
        args = self.args
        logd = self.logd
        logd(f'args: {args}')

    @classmethod
    def run(cls):
        ''' run '''
        args = do_parser()
        obj = cls(args)
        obj.action()

    def action(self):
        ''' acton '''
        # use rich
        if self.use_rich:
            self.report_in_rich()
            return
        # use colorama
        if self.use_ansi:
            self.report_in_colorama()
            return
        self.report()

    def __check_path__(self):
        ''' check paths '''
        p = os.environ['PATH']
        for d in p.split(os.pathsep):
            if d == '':
                continue
            if os.path.isdir(d):
                if d in self.alldirs['dirs']: # duplicates
                    self.alldirs['dups'].append(d)
                else:
                    self.alldirs['dirs'].append(d)
            else:
                self.alldirs['ngs'].append(d)

    def report(self):
        ''' report '''
        for d in self.alldirs['dirs']:
            print(d)
        if self.alldirs['dups']:
            print(PathLister.STR_DUP)
            for d in self.alldirs['dups']:
                print(d)
        if self.alldirs['ngs']:
            print(PathLister.STR_NG)
            for d in self.alldirs['ngs']:
                print(d)

    def report_in_colorama(self):
        ''' use colorama '''
        #logd = self.logd
        color_init(autoreset=True)
        for d in self.alldirs['dirs']:
            colorlog(Fore.GREEN, d)
        # not found
        for d in self.alldirs['ngs']:
            colorlog(Fore.RED, f'[NOT FOUND] {d}')
        # warn: duplicated
        if self.alldirs['dups']:
            colorlog(Fore.YELLOW, PathLister.STR_DUP)
            for d in self.alldirs['dups']:
                colorlog(Fore.YELLOW, f'[DUPLICATED] {d}')

    def report_in_rich(self):
        ''' in rich '''
        logd = self.logd
        logd('will use rich')
        rp = rich.print
        for d in self.alldirs['dirs']:
            rp('[green]'+d)
        if self.alldirs['dups']:
            rp('[yellow]'+self.STR_DUP)
            for d in self.alldirs['dups']:
                rp(d)
        if self.alldirs['ngs'] and len(self.alldirs['ngs'])>0:
            rp('[bold red]'+self.STR_NG)
            for d in self.alldirs['ngs']:
                rp(d)

def do_parser() -> Any:
    ''' make parser '''
    parser = argparse.ArgumentParser(description='chataes demo encrypt/decrypt')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("-d", "--debug", dest='debug', action='store_true',
        default=False, help='debug mode')
    parser.add_argument("-r", "--rprint", dest='rprint', action='store_true',
        default=False, help='requst rich')
    parser.add_argument("-a", "--ansi", dest='ansi', action='store_true',
        default=False, help='request ansi')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    PathLister.run()
