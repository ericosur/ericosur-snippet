#!/usr/bin/env python3
# coding: utf-8

'''
check if input number is prime or not
may input numbers from CLI and stdin
use 'sympy.ntheory.primetest.isprime()'

use be_prepared and typer
'''

import sys
from typing_extensions import Annotated, List

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

prt = rprint if USE_RICH else print

try:
    from sympy import ntheory
    import typer
except ImportError as err:
    prt('Import Error while:', err)
    sys.exit(1)

def is_prime(n: int):
    ''' check if a prime with sympy '''
    return ntheory.primetest.isprime(n)

def prepare_values(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
    ''' prepare values '''
    after = 0 if after is None else after
    before = 0 if before is None else before
    radius = 0 if radius is None else radius
    if radius!=0:
        if after!=0 or before!=0:
            prt(f"CONFLICT: context({radius}) vs after({after})/before({before})")
            prt("The value of context will override after and/or before")
        after, before = radius, radius
    upper = v + after
    lower = v - before
    if lower>upper:
        lower,upper = upper,lower
    vals = []
    for y in range(lower,upper+1):
        vals.append(y)
    return vals

def check_values(vals: list[int]) -> None:
    ''' check values '''
    for v in vals:
        b = is_prime(v)
        if USE_RICH:
            if b:
                rprint(f'[cyan]{v}[/] is a [green]PRIME[/]')
            else:
                rprint(f'[cyan]{v}[/] is [red]NOT a PRIME[/]')
        else:
            yesno = " " if b else " not "
            print(f"{v} is{yesno}a PRIME")

def run_test():
    ''' test '''
    vals = prepare_values(1000, radius=10)
    for v in vals:
        if is_prime(v):
            rprint(f'[cyan]{v}[/] is a [green]PRIME[/]')

def run_demo():
    ''' demo '''
    vals = [7427466391, 27285757, 1190494759, 22216911, 4222234741]
    check_values(vals)

def main(
        values: Annotated[List[int], typer.Argument(help="given numbers")] = None,
        demo: Annotated[bool, typer.Option('--demo', '-D', help="give me a demo")] = False,
        debug: Annotated[bool, typer.Option('--debug', help='toggle debug')] = False,
        test: Annotated[bool, typer.Option('--test', '-t', help="give me a test")] = False,
        after: Annotated[int,
                            typer.Option("--after", "-A", help="after nn year")] = 0,
        before: Annotated[int,
                            typer.Option("--before", "-B", help="before nn year")] = 0,
        context: Annotated[int, typer.Option("--context", "-C",
                                    help="radius nn year, conflicts: after/before")] = 0,
    ):
    '''
    use -A, -B, -C to search a range of specified value, like

    python is_prime.py 50 -C 3

    will check 47 48 49 50 51 52 53, and only show the prime
    '''
    if test:
        run_test()
        exit(0)
    if demo:
        run_demo()
        exit(0)
    if values is None:
        prt(f'use: {sys.argv[0]} --help')
        exit(0)
    if after or before or context:
        v = values[0]
        prt(f'info: only take the first one: {v}')
        if debug:
            prt(f'debug: {v=}')
            if after:
                prt(f'{after=}')
            if before:
                prt(f'{before=}')
            if context:
                prt(f'{context=}')
        vals = prepare_values(v, after=after, before=before, radius=context)
        if debug:
            prt(f'check {vals[0]} to {vals[-1]}')
        any_prime = False
        for v in vals:
            if is_prime(v):
                rprint(f'[cyan]{v}[/] is a [green]PRIME[/]')
                any_prime = True
        if not any_prime:
            rprint("no prime number at all")
        exit(0)

    vals = values
    check_values(vals)

if __name__ == '__main__':
    typer.run(main)
