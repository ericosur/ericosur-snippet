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
from loguru import logger
logd = logger.debug

ARR_SIZE = 100_000

def hard_work() -> str:
    ''' hard work '''
    tid = threading.current_thread().ident
    logd(f'hard_work: thread id: {tid}')
    rep = randint(6, 12) * 100
    arr = np.random.randint(255, size=ARR_SIZE)
    total = 0
    start = default_timer()
    for _ in range(rep):
        total += sum(arr)
    end = default_timer()
    during = end - start
    print_during(start, end, f'hard-{tid}')
    msg = f'hard_work: {tid}: elem {rep*ARR_SIZE:,}, during {during}, total: {total}'
    logd(msg)
    return msg

def heavy_work() -> str:
    ''' heavy work '''
    rep = 6_000
    tid = threading.current_thread().ident
    logd(f'heavy_work: thread id: {tid}')
    total = 0
    start = default_timer()
    arr = np.random.randint(255, size=ARR_SIZE)
    for _ in range(rep):
        total += np.sum(arr)  # type: ignore[assignment]
    end = default_timer()
    during = end - start
    print_during(start, end, f'heavy-{tid}')
    msg = f'heavy_work: {tid}: elem {rep*ARR_SIZE:,}, during: {during}, total: {total}'
    logd(msg)
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
    await asyncio.sleep(1)
    logd(f'task{idx}: do_easy_job done!')
    return None

def print_during(start: float, end: float, msg: str|None) -> None:
    ''' during '''
    during = end - start
    print(f'{msg}: during: {during:.5f}')

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

    end = default_timer()
    print_during(start, end, "main")
    print('-' * 70)
    print('show gathered results:')
    for idx,r in enumerate(results):
        print(f'{idx}: {r}')

if __name__ == "__main__":
    asyncio.run(main())
