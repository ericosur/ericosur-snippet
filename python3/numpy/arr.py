#!/usr/bin/env python3
# coding: utf-8

'''
with asyncio to compare sum vs np.sum
'''

from timeit import default_timer
import asyncio
import concurrent
import numpy as np
from rich.console import Console

MAXCNT = 500_000_000
MAX_TIMEOUT = 20  # seconds

console = Console()
prt = console.print

def builtin_sum(arr) -> int:
    ''' builtin sum '''
    start = default_timer()
    r = sum(arr)
    during = default_timer() - start
    print_during(during, "builtin_sum")
    return r

def numpy_sum(arr) -> int:
    ''' numpy sum'''
    start = default_timer()
    r = np.sum(arr)
    during = default_timer() - start
    print_during(during, "numpy_sum")
    return r

async def do_builtin_job(loop, pool, arr) -> int:
    '''
    builtin sum
    '''
    return await loop.run_in_executor(pool, builtin_sum, arr)

async def do_numpy_job(loop, pool, arr) -> int:
    '''
    numpy sum
    '''
    return await loop.run_in_executor(pool, numpy_sum, arr)

def print_during(during: float, msg: str) -> None:
    ''' print during '''
    prt(f'{msg}: during: {during:.6f}')

async def main():
    '''
    async main
    '''
    np_arr = None
    int_arr = None
    outer_start = default_timer()
    with console.status("[bold green] running...", spinner="bouncingBar") as _status:
        start = default_timer()
        np_arr = np.random.randint(255, size=MAXCNT)
        int_arr = np_arr.tolist()
        during = default_timer() - start
        print_during(during, "time taken for array generation")

        loop = asyncio.get_event_loop()
        start = default_timer()
        try:
            async with asyncio.timeout(MAX_TIMEOUT):
                prt("start running tasks...")
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    task1 = asyncio.create_task(do_builtin_job(loop, pool, int_arr))
                    task2 = asyncio.create_task(do_numpy_job(loop, pool, np_arr))
                    prt('before calling gather...')
                    results = await asyncio.gather(task1, task2)
        except TimeoutError:
            prt("The long operation timed out, but we've handled it.")

    out_during = default_timer() - outer_start
    print_during(out_during, "main")
    prt('-' * 70)
    prt('gathered results:')
    for idx,r in enumerate(results):
        prt(f'{idx}: {r}')

if __name__ == "__main__":
    asyncio.run(main())
