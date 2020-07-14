#!/usr/bin/python3
# coding: utf-8

'''
table: prime_100k.txt
will load/save it as pickle format

given cli argument to get lower/upper prime

'''

import bisect
import random
import time

# pylint: disable=import-error
# pylint: disable=unused-import
# pythonista
import clipboard
import console

import search_in_primes

# pylint: disable=invalid-name
# too-many-statements

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
        print('test {}...'.format(val))
    with search_in_primes.LoadPrimeFromText() as sp:
        if val % 2 != 0:
            print('[ERROR] must be an even number')
            return None

        ret = sp.get_primes_less_than(val)
        if debug:
            print('len(ret):', len(ret))

        if debug:
            ans, cnt, duration = impl1(val, ret)
            print('len: {}, cnt: {}, time: {}'.format(len(ans), cnt, duration))
            ans, cnt, duration = impl2(val, ret)
            print('len: {}, cnt: {}, time: {}'.format(len(ans), cnt, duration))

        ans, cnt, duration = impl3(val, ret)
        if debug:
            print('len: {}, cnt: {}, time: {}'.format(len(ans), cnt, duration))
        return ans

def profile():
    ''' basic test '''
    gold_bach(250000, debug=True)

def print_duration(start, end, msg=''):
    ''' print duration '''
    print('{} duration: {:.3f} seconds (wall clock)'.format(msg, end - start))


def run_this():
    ''' run this for pythonista '''
    ret = console.input_alert('input a number')
    try:
        val = int(ret)
        if val <= 0 or val % 2 == 1:
            print('invalid number, use auto demo')
            val = random.randint(5000, 15000) * 2

        res = gold_bach(val)
        if res is not None:
            print('test {} goldbach ====>'.format(val), end='')
            print('  total combination: {}'.format(len(res)))
            print('  pick random one: {}'.format(res[random.randint(0, len(res)-1)]))
            print('  pick last one: {}'.format(res[-1]))
    except ValueError:
        print('{} is a ValueError'.format(ret))


if __name__ == '__main__':
    run_this()
