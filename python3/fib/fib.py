#!/usr/bin/env python3
# coding: utf-8

'''
a simple and stupid fib function test

It is time/memory consuming while n is large.
It took 23.81 sec to calculate fib(40)

2023-05-24 Host(zen33) takes 15.14 seconds to get fib(40)
2023-05-24 Host(jeff) takes 8.91 seconds to get fib(40)

'''

from timeit import default_timer
from datetime import datetime
from socket import gethostname
try:
    from rich.console import Console
    #from rich.markdown import Markdown
    USE_RICH = True
except ImportError:
    USE_RICH = False


def fib(n: int) -> int:
    ''' simple recursive version to get fib '''
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def prepare_msg(duration: float, ulimit: int) -> None:
    ''' prepare message '''
    dt = datetime.today().strftime('%Y-%m-%d')
    hostname = gethostname()
    msg = f'{dt} Host({hostname}) takes {duration:.3f} seconds to get fib({ulimit})'
    print(msg)

def test() -> None:
    ''' test '''
    m = 40
    print(f'Calculate fib({m}) from scratch, for cached fib(), use')
    print('fib_store.py')

    time_start = default_timer()
    if USE_RICH:
        console = Console()
        with console.status("[bold green]running...[/]", spinner="dots") as status:
            r = fib(m)
    else:
        r = fib(m)
    d = default_timer() - time_start

    print(f'fib({m}) = {r}')
    prepare_msg(d, m)

if __name__ == '__main__':
    test()
