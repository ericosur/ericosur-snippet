#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
#

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

def is_simple_composite(v: int) -> bool:
    ''' if multiple of 2,3,5,7, return true '''
    return v%2==0 or v%3==0 or v%5==0 or v%7==0

def look_toward(v: int, around: int, is_increase: bool) -> List[int]:
    ''' look toward, is_increate true/false '''
    found = []
    if v % 2 == 0: # even number
        i = v - 1
    else:
        i = v
    step = 2 if is_increase else -2
    while len(found) < around:
        if i < 1:
            break
        if is_prime(i):
            found.append(i)
        i += step  # will skip even numbers at the first
    #prt(f'backward len: {len(backward)}, last i={i}')
    #prt(backward)
    return found

def search_around_primes(v: int, around: int) -> None:
    ''' search primes around, till the length is met
        for example, given v=101 (prime), and around=5
        will get 5 prime numbers less than 101 and
        5 prime number geater then 101
    '''
    # look backward
    ans = []
    i, j = v, v
    if is_prime(v):
        ans.append(v)
        i = v - 2
        j = v + 2
    backward = look_toward(i, around, is_increase=False)
    ans.extend(backward)
    forward = look_toward(j, around, is_increase=True)
    ans.extend(forward)
    ans.sort()
    prt(ans)

def main(
        values: Annotated[List[int], typer.Argument(help="given numbers")] = None,
        demo: Annotated[bool, typer.Option('--demo', '-D', help="give me a demo")] = False,
        test: Annotated[bool, typer.Option('--test', '-t', help="give me a test")] = False,
        after: Annotated[int,
                            typer.Option("--after", "-A", help="after nn")] = 0,
        before: Annotated[int,
                            typer.Option("--before", "-B", help="before nn")] = 0,
        context: Annotated[int, typer.Option("--context", "-C",
                                    help="radius nn, conflicts: after/before")] = 0,
        around: Annotated[int, typer.Option("--around", "-R", help="find nn prime numbers "
                                            "around given number, it overrides abc")] = 0,
    ):
    '''
    use -A, -B, -C to search a range of specified value, like

    python is_prime.py 50 -C 3

    will check 47 48 49 50 51 52 53, and only show the prime
    '''
    if test:
        run_test()
        sys.exit(0)
    if demo:
        run_demo()
        sys.exit(0)
    if values is None:
        prt(f'get some help: {sys.argv[0]} --help')
        sys.exit(1)
    if around:
        if after or before or context:
            prt('note: options abc will be ignored')
        if len(values)>1:
            prt("note: only the first value is used")
        v = values[0]
        search_around_primes(v, around)
        sys.exit(0)
    if after or before or context:
        v = values[0]
        prt(f'info: only take the first one: {v}')
        vals = prepare_values(v, after=after, before=before, radius=context)
        any_prime = False
        for v in vals:
            if is_prime(v):
                rprint(f'[cyan]{v}[/] is a [green]PRIME[/]')
                any_prime = True
        if not any_prime:
            rprint("no prime number at all")
        sys.exit(0)

    check_values(values)

if __name__ == '__main__':
    typer.run(main)
