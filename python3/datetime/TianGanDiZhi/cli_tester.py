#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

'''
typer tests gngan_yaljux.py
'''

import sys
from random import randint
from typing_extensions import Annotated
try:
    import typer
except ImportError:
    print('[FAIL] you need module typer to run this')
    sys.exit(1)

console = None
try:
    from rich.console import Console
    console = Console()
except ImportError:
    print("[WARN] no rich.console to use")

from gngan_yaljux import do_tests, do_values, do_verbose, GanChi

def do_nothing(*args, **wargs) -> None:
    ''' do nothing '''
    return None

def main(verbose: Annotated[bool, typer.Option("--list", "-l",
                                               help="list all 天干/地支/生肖")] = False,
         debug: Annotated[bool, typer.Option("--debug", "-d",
                                               help="debug info")] = False,
         values: Annotated[bool, typer.Option("--value",
                                               help="test some values")] = False,
         alltests: Annotated[bool, typer.Option("--alltests","--all",
                                               help="run all tests")] = False,
         testbasic: Annotated[bool, typer.Option("--basictest","--basic",
                                               help="run basic tests")] = False,
         testab: Annotated[bool, typer.Option("--abtest","--ab",
                                               help="run AB tests")] = False,
        ) -> None:
    '''
    no required arguments, use options to toggle, only the first one will be taken
    '''
    log = do_nothing
    if debug:
        log = console.log
    if verbose: # list all elements
        do_verbose(log=log)
        return
    if values:  # pick 3 values and show
        x = [randint(1900,2050) for _ in range(3)]
        x.sort()
        do_values(x, log=log)
        return
    if alltests:
        do_tests(log=log)
        return
    if testbasic:
        gc = GanChi(log)
        gc.test0()
        return
    if testab:
        gc = GanChi(log)
        gc.test1()
        return

    console.print(f"[INFO] use [yellow]{sys.argv[0]} --help[/yellow] to see help messages")

if __name__ == '__main__':
    typer.run(main)
