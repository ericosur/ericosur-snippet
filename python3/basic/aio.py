#!/usr/bin/env python3
# coding: utf-8

import asyncio
import concurrent
import threading
from time import sleep
from timeit import default_timer
from random import randint
import numpy as np
from loguru import logger
logd = logger.debug

def hard_work() -> int:
    ''' hard work '''
    tid = threading.current_thread().ident
    logd(f'hard_work: thread id: {tid}')
    rep = randint(1, 6) * 1_000_000
    total = 0
    start = default_timer()
    for _ in range(rep):
        total += randint(1, 9999)
    end = default_timer()
    during = end - start
    print_during(start, end, f'hard-{tid}')
    logd(f'{tid}: repeat {rep} times during {during}')
    return total

def heavy_work() -> int:
    ''' heavy work '''
    pass

# async def do_async_job():
#     await asyncio.sleep(2)
#     print(datetime.now().isoformat(), 'thread id', threading.current_thread().ident)

async def do_async_job(loop, pool, idx: int) -> int:
    r = await loop.run_in_executor(pool, hard_work)
    await asyncio.sleep(1)
    logd(f'task{idx}: hard job done!')
    return r

async def do_easy_job(loop, pool, idx: int) -> None:
    await asyncio.sleep(1)
    logd(f'task{idx}: do_easy_job done!')
    return None

def print_during(start: float, end: float, msg: str|None) -> None:
    ''' during '''
    during = end - start
    print(f'{msg}: during: {during:.5f}')

async def main():
    loop = asyncio.get_event_loop()
    start = default_timer()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        task1 = asyncio.create_task(do_async_job(loop, pool, 1))
        task2 = asyncio.create_task(do_easy_job(loop, pool, 2))
        task3 = asyncio.create_task(do_async_job(loop, pool, 3))
        task4 = asyncio.create_task(do_easy_job(loop, pool, 4))
        task5 = asyncio.create_task(do_async_job(loop, pool, 5))
        print('before calling gather...')
        results = await asyncio.gather(task1, task2, task3, task4, task5)
    end = default_timer()
    print_during(start, end, "main")
    print('-' * 70)
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
