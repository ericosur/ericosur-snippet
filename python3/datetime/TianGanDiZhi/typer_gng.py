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

import sys
from typing import Optional
from typing_extensions import Annotated
try:
    import typer
except ImportError:
    print('[FAIL] you need module typer to run this')
    sys.exit(1)

from rich.console import Console
console = Console()

from gngan_yaljux import do_ab, do_tests, do_values, do_verbose
sys.path.insert(0, "..")
from be_prepared import get_thisyear, prepare_values

class Main():
    ''' main '''
    def __init__(self):
        self.logd = console.log

    def main(self, values: Annotated[Optional[list[int]],
                                     typer.Argument(help="specify year")] = None,
            after: Annotated[int,
                             typer.Option("--after", "-A", help="after nn year")] = 0,
            before: Annotated[int,
                              typer.Option("--before", "-B", help="before nn year")] = 0,
            context: Annotated[int, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = 0,
            debug: Annotated[bool, typer.Option("--debug / --no-debug", "-d / -D",
                                        help="show dubug info")] = False,
            show: Annotated[bool, typer.Option("--show", "--list", "-s",
                                        help="list GnnGj and YalJux")] = False,
            test: Annotated[bool, typer.Option("--test", "-t",
                                        help="run test on GnnGj and YalJux")] = False,
            gnn: Annotated[bool, typer.Option("--gnn",
                                        help="apply two numbers for TianGan and DiZhi")] = False,
            ) -> None:
        '''
        If no option is specified, run the default test. If available, color will
        refelct: red for specified year, green is the current year, yellow is both
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
            print('[FAIL] NEED exactly two arguments')
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
            the_vals = prepare_values(v, after=after, before=before, radius=context)
            do_values(the_vals, target=v, log=self.logd)

if __name__ == '__main__':
    m = Main()
    typer.run(m.main)
