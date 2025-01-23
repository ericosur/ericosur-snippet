#!/usr/bin/env python3
# coding: utf-8

'''
a demo of asyncio, threading id,
'''

import asyncio
import concurrent
import threading
from timeit import default_timer
from random import randint
import numpy as np

try:
    from rich import print as pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = pprint if USE_RICH else print

try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False
logd = logger.debug if USE_LOGURU else print

ARR_SIZE = 100_000

def hard_work() -> str:
    ''' hard work '''
    tid = threading.current_thread().ident
    logd(f'hard_work: thread id: {tid}')
    rep = randint(1, 4) * 1000
    arr = [randint(0, 255) for _ in range(ARR_SIZE)]
    total = 0
    start = default_timer()
    for _ in range(rep):
        total += sum(arr)
    during = default_timer() - start
    print_during(during, f'hard-{tid}')
    msg = f' hard_work: {tid}:\nelem {rep*ARR_SIZE:,}, during {during:.6f}, total: {total:,}'
    #logd(msg)
    return msg

def heavy_work() -> str:
    ''' heavy work '''
    rep = 100_000
    tid = threading.current_thread().ident
    logd(f'heavy_work: thread id: {tid}')
    total = 0
    start = default_timer()
    arr = np.random.randint(255, size=ARR_SIZE)
    for _ in range(rep):
        total += np.sum(arr)  # type: ignore[assignment]
    during = default_timer() - start
    print_during(during, f'heavy-{tid}')
    msg = f'heavy_work: {tid}:\nelem {rep*ARR_SIZE:,}, during: {during:.6f}, total: {total:,}'
    #logd(msg)
    return msg

async def do_hard_job(loop, pool, idx: int) -> str:
    '''
    put hard_work() into executor pool
    '''
    r = await loop.run_in_executor(pool, hard_work)
    #await asyncio.sleep(1)
    logd(f'task{idx}: hard_work done!')
    return r

async def do_heavy_job(loop, pool, idx: int) -> str:
    '''
    put heavy_job into executor pool
    '''
    r = await loop.run_in_executor(pool, heavy_work)
    #await asyncio.sleep(1)
    logd(f'task{idx}: heavy_work done!')
    return r

async def do_easy_job(_loop, _pool, idx: int) -> None:
    '''
    easy job just sleep a moment
    '''
    start = default_timer()
    await asyncio.sleep(1)
    during = default_timer() - start
    print_during(during, f'easy-{idx}')
    logd(f'task{idx}: do_easy_job done!')
    return None

def print_during(during: float, msg: str|None) -> None:
    ''' during '''
    prt(f'{msg}: during: {during:.5f}')

async def main():
    '''
    async main
    '''
    MAX_TIMEOUT = 20
    loop = asyncio.get_event_loop()
    start = default_timer()
    try:
        async with asyncio.timeout(MAX_TIMEOUT):
            print("This statement will run regardless.")
            with concurrent.futures.ThreadPoolExecutor() as pool:
                task1 = asyncio.create_task(do_easy_job(loop, pool, 1))
                task2 = asyncio.create_task(do_hard_job(loop, pool, 2))
                task3 = asyncio.create_task(do_heavy_job(loop, pool, 3))
                task4 = asyncio.create_task(do_easy_job(loop, pool, 4))
                task5 = asyncio.create_task(do_hard_job(loop, pool, 5))
                print('before calling gather...')
                results = await asyncio.gather(task1, task2, task3, task4, task5)
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    during = default_timer() - start
    print_during(during, "main")
    print('-' * 70)
    print('show gathered results:')
    for idx,r in enumerate(results):
        print(f'{idx}: {r}')

if __name__ == "__main__":
    asyncio.run(main())
