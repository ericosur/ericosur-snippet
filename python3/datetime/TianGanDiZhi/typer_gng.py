#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

'''
天干地支

use typer to handle CLI
'''

from typing import List, Optional
from typing_extensions import Annotated
import typer

from rich.console import Console
console = Console()

from gngan_yaljux import do_ab, do_tests, do_values, do_verbose, get_thisyear

class Main():
    ''' main '''
    def __init__(self):
        self.logd = console.log

    def prepare_values(self, year: int, after: int=0, before: int=0, radius: int=0) -> List:
        ''' prepare values '''
        if after<0 or before<0 or radius<0:
            raise ValueError("value MUST be greater than 0")
        if radius!=0:
            if after!=0 or before!=0:
                self.logd(f"CONFLICT: context({radius}) vs after({after})/before({before})")
                return [year]
            after, before = radius, radius

        logd = self.logd
        logd(f"prepare_values... {after=}, {before=}")
        upper = year + after
        lower = year - before
        if lower>upper:
            lower,upper = upper,lower
        logd(f"{upper=}")
        logd(f"{lower=}")
        vals = []
        for y in range(lower,upper+1):
            vals.append(y)
        logd(f'return: {vals}')
        return vals

    def main(self, values: Annotated[Optional[List[int]],
                                     typer.Argument(help="specify year")] = None,
            after: Annotated[int,
                             typer.Option("--after", "-A", help="after nn year")] = 0,
            before: Annotated[int,
                              typer.Option("--before", "-B", help="before nn year")] = 0,
            context: Annotated[int, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = 0,
            debug: Annotated[bool, typer.Option("--debug / --no-debug", "-d / -D",
                                        help="show dubug info")] = False,
            show: Annotated[bool, typer.Option("--show", "-s",
                                        help="list GnnGj and YalJux")] = False,
            test: Annotated[bool, typer.Option("--test", "-t",
                                        help="run test on GnnGj and YalJux")] = False,
            gnn: Annotated[bool, typer.Option("--gnn",
                                        help="do ab test")] = False,
            ) -> None:
        '''
        if no option is specified, run the default test
        '''

        def do_nothing(*args, **wargs) -> None:
            ''' do nothing '''
            return None

        if not debug:
            self.logd = do_nothing

        if gnn:
            if len(values)==2:
                do_ab(values[0], values[1], log=self.logd)
                return
            print('[FAIL] must specify two arguments')
            return
        if test:
            do_tests()
            return
        if show:
            do_verbose()
            return

        # if no values, append this year
        this_year = get_thisyear()
        if not values:
            values = [this_year]
        self.logd(f'{after=}')
        self.logd(f'{before=}')
        for v in values:
            self.logd(f'{v=}')
            if v==this_year:
                self.logd(f"this_year: {v}")
            the_vals = self.prepare_values(v, after=after, before=before, radius=context)
            do_values(the_vals, log=self.logd)

if __name__ == '__main__':
    m = Main()
    typer.run(m.main)
