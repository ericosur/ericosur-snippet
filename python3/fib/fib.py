#!/usr/bin/env python3

'''
a simple and stupid fib function test

It is time/memory consuming while n is large.
It took 23.81 sec to calculate fib(40)

2023-05-24 Host(zen33) takes 15.14 seconds to get fib(40)
2023-05-24 Host(jeff) takes 8.91 seconds to get fib(40)

'''

import sys
from datetime import datetime
from pathlib import Path
from socket import gethostname
from timeit import default_timer

# Add paths based on this file location (not current working directory)
THIS_DIR = Path(__file__).resolve().parent
PY3_DIR = THIS_DIR.parent
MYUTIL_DIR = PY3_DIR.joinpath('myutil')
sys.path.insert(0, str(PY3_DIR))
sys.path.insert(0, str(MYUTIL_DIR))
USE_RICH = True


def fib(n: int) -> int:
    ''' simple recursive version to get fib '''
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def prepare_msg(duration: float, ulimit: int) -> None:
    ''' prepare message '''
    dt = datetime.now().astimezone().strftime('%Y-%m-%d')
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
        from madlog import get_console
        console = get_console()
        with console.status("[bold green]running...[/]", spinner="dots") as _status:
            r = fib(m)
    else:
        r = fib(m)
    d = default_timer() - time_start

    print(f'fib({m}) = {r}')
    prepare_msg(d, m)

if __name__ == '__main__':
    test()
