#!/usr/bin/env python3
# coding: utf-8
#

'''
use linecache for one million lines of text file
'''

import random
from itertools import islice
from line_count import bufcount

# pylint: disable=global-statement

FILENAME = 'py1.txt'
TOTAL_CALLS = 0

def get_nth_line_from_file(fn, line_num):
    '''
    get nth line from file, start from 1, not 0
    https://www.rosettacode.org/wiki/Read_a_specific_line_from_a_file#Python
    '''
    if line_num == 0:
        return None
    line = None
    with open(fn) as f:
        try:
            line = next(islice(f, line_num - 1, line_num))
        except StopIteration as e:
            print(e)
    return line.strip()

def search_from_file(val, fn, total_lines=0):
    ''' search value at index or between '''
    import os
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
    import os
    file_size = os.stat(fn)[6]
    return file_size

def main(argv):
    ''' main '''
    fn = FILENAME
    sz = get_filesize(fn)
    lnc = bufcount(fn)
    print('text file: {}, size: {}, lines: {}'.format(fn, sz, lnc))
    print('first line: {}'.format(get_nth_line_from_file(fn, 1)))
    print('last line: {}'.format(get_nth_line_from_file(fn, lnc)))

    targets = [2, 15485863, 1, 16999777]
    if not argv:
        for _ in range(6):
            targets.append(random.randint(2, 15485863))
    else:
        targets = [int(x) for x in argv]


    for t in targets:
        print('search {} ... '.format(t), end='')
        (p, q) = search_from_file(t, fn, lnc)
        if p is not None:
            print('between ({}, {})'.format(p, q))
    print('total IO calls:', TOTAL_CALLS)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])