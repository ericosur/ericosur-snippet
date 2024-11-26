#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

'''
use typer to handle CLI
'''

import sys
from typing import List, Optional
from typing_extensions import Annotated
try:
    import typer
except ImportError:
    print('[FAIL] you need module typer to run this')
    sys.exit(1)

from rich import print as rprint
from loguru import logger

def do_nothing(*args, **wargs) -> None:
    ''' do nothing '''
    return None

class Main():
    ''' main '''
    def __init__(self):
        self.logd = do_nothing
        self.logv = do_nothing

    def do_tests(self) -> None:
        ''' do tests '''
        logd = self.logd
        logv = self.logv
        assert 1+1==2
        logd('pass')
        logv("There will be more info...")

    def do_values(self, values, after=0, before=0, context=0) -> None:
        ''' do values '''
        logd = self.logd
        logv = self.logv
        logd(f'{values=}')
        logd(f'{after=}, {before=}, {context=}')

        if context != 0 :
            if after!=0 or before!=0:
                logv(f'context({context}) will override after({after}) and before({before})')
            after = context
            before = context

        for i in values:
            upper = i + after
            lower = i - before
            ll = [x for x in range(lower, upper+1)]
            self.show_list(ll, i)

    def show_list(self, the_list: List, v: int) -> None:
        ''' show the list '''
        print('[', end='')
        for i in the_list:
            if i==v:
                rprint(f'[yellow]{i}[/]', end='')
            else:
                rprint(f'{i}', end='')
            if i != the_list[-1]:
                rprint(', ', end='')
        print(']')

    def main(self, values: Annotated[Optional[List[int]],
                                     typer.Argument(help="specify values")] = None,
            after: Annotated[int,
                             typer.Option("--after", "-A", help="after nn year")] = 0,
            before: Annotated[int,
                              typer.Option("--before", "-B", help="before nn year")] = 0,
            context: Annotated[int, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = 0,
            test: Annotated[bool, typer.Option("--test", "-t",
                                        help="run tests")] = False,
            debug: Annotated[bool, typer.Option("--debug / --no-debug", "-d / -D",
                                        help="show dubug info")] = False,
            verbose: Annotated[bool, typer.Option("--verbose", "-v",
                                        help="verbose mode")] = False,
            ) -> None:
        '''
        if no option is specified, run the default test
        '''
        if debug:
            self.logd = logger.debug
        self.logd(f'{debug=}')
        if verbose:
            self.logv = logger.info
        self.logd(f'{verbose=}')
        self.logv('verbose mode is on...')
        if test:
            self.do_tests()
            return
        if values:
            self.do_values(values, after=after, before=before, context=context)
            return
        logger.info(f"use ```{sys.argv[0]} --help``` to see help")

if __name__ == '__main__':
    m = Main()
    # yeah I may use the member function of an class
    typer.run(m.main)
