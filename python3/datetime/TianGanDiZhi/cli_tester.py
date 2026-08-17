#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

'''
typer tests gngan_yaljux.py
'''

import sys
from random import randint
from typing import Annotated

try:
    import typer
except ImportError:
    print('[FAIL] you need module typer to run this')
    sys.exit(1)

try:
    from gngan_yaljux import GanChi, do_ab, do_tests, do_values, do_verbose, prt
    from tgdz_common import do_nothing, logd
except ImportError as e:
    print('[FAIL] fail to import module: ', e)
    sys.exit(1)


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
         apple: Annotated[int | None, typer.Option("--apple", "-a",
                                                    help="TianGan index (0-9)")] = None,
         ball: Annotated[int | None, typer.Option("--ball", "-b",
                                                   help="DiZhi index (0-11)")] = None,
        ) -> None:
    '''
    no required arguments, use options to toggle, only the first one will be taken
    '''
    _logd = logd if debug else do_nothing
    if verbose: # list all elements
        do_verbose(_logd=_logd)
        return
    if values:  # pick 3 values and show
        x = [randint(1900,2050) for _ in range(3)]
        x.sort()
        do_values(x, _logd=_logd)
        return
    if alltests:
        do_tests(_logd=_logd)
        return
    if testbasic:
        gc = GanChi(_logd=_logd)
        gc.test0()
        return
    if testab:
        if apple is None or ball is None:
            prt('[FAIL] --ab requires both --apple/-a and --ball/-b')
            return
        if not GanChi.check_ab(apple, ball):
            prt(f'[FAIL] invalid --ab values: {apple}, {ball}')
            return
        do_ab(apple, ball, _logd=_logd)
        return

    prt(f"[INFO] use [yellow]{sys.argv[0]} --help[/yellow] to see help messages")


app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
app.command()(main)

if __name__ == '__main__':
    app()
