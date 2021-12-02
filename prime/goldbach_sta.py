#!/usr/bin/python3
# coding: utf-8

'''
table: prime_100k.txt
will load/save it as pickle format

given cli argument to get lower/upper prime

'''

import bisect
import time

from store_prime import StorePrime

# pylint: disable=import-error
# pylint: disable=unused-import
PYTHONISTA=False
if PYTHONISTA:
    # pythonista
    import clipboard
    import console

# pylint: disable=invalid-name
# too-many-statements

version = '2021.11.25.18.01'

def get_bisect(a, x):
    ''' Locate the leftmost value exactly equal to value **x** from list **a** '''
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def impl1(val, ret):
    ''' impl1 '''
    ans = []
    cnt = 0
    start_time = time.time()
    for pp in ret:
        left = val - pp
        cnt += 1
        if pp > left:
            break
        if left in ret:
            ans.append((pp, left))
    return ans, cnt, time.time() - start_time

def impl2(val, ret):
    ''' impl2 '''
    ans = []
    cnt = 0
    start_time = time.time()
    for pp in ret:
        left = val - pp
        cnt += 1
        if pp > left:
            break
        try:
            ret.index(left)
        except ValueError:
            pass
        else:
            ans.append((pp, left))
    return ans, cnt, time.time() - start_time

def impl3(val, ret):
    ''' impl3 '''
    ans = []
    cnt = 0
    start_time = time.time()
    for pp in ret:
        left = val - pp
        cnt += 1
        if pp > left:
            break
        try:
            get_bisect(ret, left)
        except ValueError:
            pass
        else:
            ans.append((pp, left))
    return ans, cnt, time.time() - start_time


def gold_bach(val, debug=False):
    ''' it could be found if val < 4 * 10^17 '''
    if debug:
        print(f'test {val}...')
    with StorePrime() as sp:
        if val % 2 != 0:
            print('[ERROR] must be an even number')
            return None

        ret = sp.get_primes_less_than(val)
        if debug:
            print('len(ret):', len(ret))

        if debug:
            ans, cnt, duration = impl1(val, ret)
            print(f'len: {len(ans)}, cnt: {cnt}, time: {duration:.3f}')
            ans, cnt, duration = impl2(val, ret)
            print(f'len: {len(ans)}, cnt: {cnt}, time: {duration:.3f}')

        ans, cnt, duration = impl3(val, ret)
        if debug:
            print(f'len: {len(ans)}, cnt: {cnt}, time: {duration:.3f}')
        return ans

def profile():
    ''' basic test '''
    gold_bach(250000, debug=True)

def print_duration(start, end, msg=''):
    ''' print duration '''
    print(f'{msg} duration: {end-start:.3f} seconds (wall clock)')


def run_this():
    ''' run this for pythonista '''
    ret = console.input_alert('input a number')
    try:
        val = int(ret)
        if val <= 0 or val % 2 == 1:
            console.alert(f'invalid number: {val}, need an even number')
            return

        res = gold_bach(val)
        if res is None:
            console.alert('no valid answers')
            return

        msg = f'the first: {res[0]}, the last: {res[-1]}'
        console.alert(msg)
    except ValueError:
        print(f'{ret} is a ValueError')


if __name__ == '__main__':
    if PYTHONISTA:
        run_this()
    else:
        profile()
