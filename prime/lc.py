#!/usr/bin/env python3
# coding: utf-8
#

'''
handle one million lines of text file with reading all lines into memory
'''

import errno
import os
import random
from itertools import islice
from line_count import bufcount
from load_myutil import read_setting, get_home

# pylint: disable=global-statement

TOTAL_CALLS = 0

def get_nth_line_from_file(fn, line_num):
    '''
    get nth line from file, start from 1, not 0
    https://www.rosettacode.org/wiki/Read_a_specific_line_from_a_file#Python
    '''
    if line_num == 0:
        return None
    line = None
    with open(fn, encoding='utf8') as f:
        try:
            line = next(islice(f, line_num - 1, line_num))
        except StopIteration as e:
            print(e)
    return line.strip()

def search_from_file(val, fn, total_lines=0):
    ''' search value at index or between '''
    if not os.path.exists(fn):
        print('[ERROR] file not found', fn)
        return (None, None)

    min_line = 1
    if total_lines == 0:
        max_line = bufcount(fn)
    else:
        max_line = total_lines

    def get_val(ln):
        global TOTAL_CALLS

        TOTAL_CALLS += 1
        s = get_nth_line_from_file(fn, ln)
        v = None
        try:
            v = int(s)
        except ValueError as e:
            print(e)
        return v

    # start to binary search
    max_idx = max_line
    min_idx = min_line
    max_v = get_val(max_idx)
    min_v = get_val(min_idx)
    if val > max_v or val < min_v:
        print('[ERROR] out of bound for', val)
        return (None, None)
    if val in (max_v, min_v):
        return (val, None)
    mid_idx = min_idx
    mid_v = min_v
    _cnt = 0
    while True:
        _cnt += 1
        mid_idx = (max_idx + min_idx) // 2
        mid_v = get_val(mid_idx)
        if mid_v > val:
            max_idx = mid_idx
        else:
            min_idx = mid_idx
        if min_idx > max_idx or min_idx == max_idx - 1:
            #print('    {} <====> {}'.format(min_idx, max_idx))
            break
        if _cnt > 20:
            print('[ERROR] exceed count:', _cnt)
            break
    min_v = get_val(min_idx)
    max_v = get_val(max_idx)
    return (min_v, max_v)


def get_filesize(fn):
    ''' get size of file '''
    file_size = os.stat(fn)[6]
    return file_size

def _try_fn(fn, paths):
    ''' try if file exists '''
    for p in paths:
        ff = p + '/' + fn
        if os.path.exists(ff):
            return ff
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), fn)

def main(argv):
    ''' main '''
    data = read_setting('setting.json')
    prime_big = data['prime_big']
    prime_path = data['prime_path']
    paths = []
    paths.append(get_home())
    paths.append(get_home() + '/' + prime_path)
    fn = _try_fn(prime_big, paths)
    sz = get_filesize(fn)
    lnc = bufcount(fn)
    print(f'text file: {fn}, size: {sz}, lines: {lnc}')
    res = get_nth_line_from_file(fn, 1)
    print(f'first line: {res}')
    res = get_nth_line_from_file(fn, lnc)
    print(f'last line: {res}')

    targets = [2, 15485863, 1, 16999777]
    if not argv:
        for _ in range(6):
            targets.append(random.randint(2, 15485863))
    else:
        targets = [int(x) for x in argv]


    for t in targets:
        print(f'search {t} ... ', end='')
        (p, q) = search_from_file(t, fn, lnc)
        if p is not None:
            print(f'between ({p}, {q})')
    print('total IO calls:', TOTAL_CALLS)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
