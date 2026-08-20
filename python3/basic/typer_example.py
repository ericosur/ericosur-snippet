#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

'''
use typer to handle CLI
'''

import sys
from typing import Annotated

try:
    import typer
    print("version of typer:", typer.__version__)
    from basic_common import do_nothing, get_logd, prt
except ImportError as e:
    print('[FAIL] failed to load module:', e)
    sys.exit(1)


class Main:
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

    def do_values(self, values: list[int], after: int=0, before: int=0, context:int=0) -> None:
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
            #ll = [x for x in range(lower, upper+1)]
            ll = list(range(lower, upper+1))
            self.show_list(ll, i)

    def show_list(self, the_list: list, v: int) -> None:
        ''' show the list '''
        print('[', end='')
        for i in the_list:
            if i==v:
                prt(f'[yellow]{i}[/]', end='')
            else:
                prt(f'{i}', end='')
            if i != the_list[-1]:
                prt(', ', end='')
        print(']')

    #
    # OLD typer, it will complain no such positional arg
    # ```default```` for typer.Argument():
    #
    # typer.Argument(default=None)]
    #
    # NEWER typer, use this way to set the default:
    # typer.Argument()] = None,
    #
    def main(self, values: Annotated[list[int] | None,
                                     typer.Argument(help="specify values")] = None,
            after: Annotated[int | None,
                             typer.Option("--after", "-A", help="after nn year")] = None,
            before: Annotated[int | None,
                              typer.Option("--before", "-B", help="before nn year")] = None,
            context: Annotated[int | None, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = None,
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
            self.logd = get_logd()
        self.logd(f'{debug=}')
        if verbose:
            self.logv = prt
        self.logd(f'{verbose=}')
        self.logv('verbose mode is on...')
        if test:
            self.do_tests()
            return

        has_range_option = any(v is not None for v in (after, before, context))
        after_value = after if after is not None else 0
        before_value = before if before is not None else 0
        context_value = context if context is not None else 0

        if values:
            self.do_values(values, after=after_value, before=before_value, context=context_value)
            return
        if has_range_option:
            self.do_values([17], after=after_value, before=before_value, context=context_value)
            return
        prt(f"use ```{sys.argv[0]} --help``` to see help")

if __name__ == '__main__':
    m = Main()
    # Keep Typer behavior but expose both -h and --help.
    app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
    app.command()(m.main)
    app()
