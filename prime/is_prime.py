#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
#

'''
check if input number is prime or not with external module

module dependency:
- MUST
    - type_extensions
    - typer
    - pydantic
    - rich
- OPTIONAL from one of the following:
    - first: sympy.ntheory.primetest.isprime
    - 2nd: gmpy2.is_prime
    - if none, will report error and exit
'''

from random import randint
import sys
from typing_extensions import Annotated, List
from pydantic import BaseModel

LOCAL_DEBUG = False
from store import dbg, do_nothing
dbg = dbg if LOCAL_DEBUG else do_nothing

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print
dbg(f'{USE_RICH=}')

try:
    import typer
except ImportError:
    prt('typer is required...')
    sys.exit(1)

# try first: sympy.ntheory.primetest.isprime
try:
    from sympy.ntheory.primetest import isprime as sympy_isprime
    USE_SYMPY = True
except ImportError as err:
    prt('Import Error while:', err)
    USE_SYMPY = False
dbg('f{USE_SYMPY=}')

# try 2nd: gmpy2.is_prime
USE_GMPY2 = False
gmpy2_isprime = None
if not USE_SYMPY:
    try:
        from gmpy2 import is_prime as gmpy2_isprime
        USE_GMPY2 = True
    except ImportError as err:
        if not USE_SYMPY:
            prt('Import Error while:', err)
dbg(f'{USE_GMPY2}')

def is_prime(n: int) -> bool:
    ''' check if a prime with sympy '''
    DEBUG = False
    if USE_SYMPY:
        if DEBUG:
            prt('use sympy...')
        return sympy_isprime(n)
    if USE_GMPY2:
        if DEBUG:
            prt('use gmpy2...')
        return gmpy2_isprime(n)
    #prt(f"no module support for is_prime({n})")
    return None

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

def prt_in_color(v: int, yes_no: bool) -> None:
    ''' print a number in color '''
    if yes_no:
        rprint(f'[cyan]{v}[/] is a [green]PRIME[/]')
    else:
        rprint(f'[cyan]{v}[/] is [red]NOT a PRIME[/]')

def run_random(nn: int) -> None:
    ''' test nn random numbers '''
    cnt = 0
    while cnt < nn:
        v = randint(1, 1_000_000)
        if v % 2 == 0:
            v += 1
        prt_in_color(v, is_prime(v))
        cnt += 1

class GivenOptions(BaseModel):
    ''' options '''
    values: List[int] = []
    after: int = 0
    before: int = 0
    context: int = 0
    around: int = 0

class Solution():
    ''' solution '''
    SHOW_PING = False
    def __init__(self):
        self.opts = GivenOptions()
        self._ping()

    def _ping(self):
        ''' ping '''
        if Solution.SHOW_PING:
            prt("ping!")
        if is_prime(2) is None:
            prt('no module support for checking primality')
            sys.exit(2)

    def help_me_around(self) -> bool:
        ''' help me around '''
        if not self.opts.around:
            return False
        abc = self.opts.after or self.opts.before or self.opts.context
        if abc:
            prt('note: options abc will be ignored')
        if len(self.opts.values)>1:
            prt("note: only the first value is used")
        v = self.opts.values[0]
        search_around_primes(v, self.opts.around)
        return True

    def help_abc(self) -> bool:
        ''' help if abc'''
        abc = self.opts.after or self.opts.before or self.opts.context
        if not abc:
            return False
        if len(self.opts.values)>1:
            prt("note: only the first value is used")
        v = self.opts.values[0]
        vals = self.prepare_values(v)
        any_prime = False # if found any prime number
        for v in vals:
            if is_prime(v):
                rprint(f'[cyan]{v}[/] is a [green]PRIME[/]')
                any_prime = True
        if not any_prime:
            rprint("no prime number at all")
        return True

    def run_test(self):
        ''' test '''
        self.opts.context = 5
        v = 1_000_000
        vals = self.prepare_values(v)
        for v in vals:
            prt_in_color(v, is_prime(v))

    def prepare_values(self, v: int) -> List[int]:
        ''' prepare values '''
        after = 0 if self.opts.after is None else self.opts.after
        before = 0 if self.opts.before is None else self.opts.before
        radius = 0 if self.opts.context is None else self.opts.context
        if radius!=0:
            if after!=0 or before!=0:
                prt(f"CONFLICT: context({radius}) vs after({after})/before({before})")
                prt("The value of context will override after and/or before")
            after, before = radius, radius
        upper = v + after
        lower = v - before
        if lower > upper:
            lower,upper = upper,lower
        vals = []
        for y in range(lower, upper+1):
            vals.append(y)
        return vals

    def help_tdr(self, test: bool, demo: bool, random: bool) -> None:
        ''' handle test, demo, random'''
        if test:
            self.run_test()
            sys.exit(0)
        if demo:
            run_demo()
            sys.exit(0)
        if random:
            run_random(random)
            sys.exit(0)

    def main(self,
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
            random: Annotated[int, typer.Option("--random", help="test nn random odd numbers")] = 0,
        ):
        '''
        use -A, -B, -C to search a range of specified value, like

        python is_prime.py 50 -C 3

        will check 47 48 49 50 51 52 53, and only show the prime
        '''
        if test or demo or random:
            self.help_tdr(test, demo, random)
            sys.exit(0)

        if values is None:
            prt(f'get some help: {sys.argv[0]} --help')
            sys.exit(1)
        # values, abc, and around
        self.opts.values = values
        self.opts.around = around
        self.opts.after = after
        self.opts.before = before
        self.opts.context = context

        if self.help_me_around():
            sys.exit(0)

        if self.help_abc():
            sys.exit(0)

        # check values one by one
        check_values(values)

if __name__ == '__main__':
    obj = Solution()
    typer.run(obj.main)
