#!/usr/bin/env python
# coding: utf-8

'''
https://gist.github.com/zed/0ac760859e614cd03652
https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
'''

#from __future__ import with_statement
#import time
#import random
import mmap
import os
import subprocess
import sys

from collections import defaultdict
from timeit import default_timer as timer

def mapcount(filename):
    ''' memory map '''
    with open(filename, "r+") as f:
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
    return lines

def simplecount(filename):
    ''' simple count '''
    lines = 0
    for _ in open(filename):
        lines += 1
    return lines

def bufcount(filename):
    ''' buf count '''
    lines = 0
    buf_size = 1024 * 1024
    with open(filename) as f:
        read_f = f.read # loop optimization
        buf = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            buf = read_f(buf_size)
    return lines

def wccount(filename):
    ''' external __wc -l__ '''
    out = subprocess.Popen(['/usr/bin/wc', '-l', filename],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT
                           ).communicate()[0]
    return int(out.partition(b' ')[0])

def itercount(filename):
    ''' itercount, what is U in open ???'''
    return sum(1 for _ in open(filename, 'rbU'))

def opcount(fname):
    ''' use enumerate '''
    line_number = 0
    with open(fname) as f:
        for line_number, _ in enumerate(f, 1):
            pass
    return line_number

def kylecount(fname):
    ''' kyle count '''
    return sum(1 for line in open(fname))

try:
    from fadvise import sequential, normal # http://chris-lamb.co.uk/projects/python-fadvise/
    def fadvcount(fname):
        ''' fadv count '''
        sequential(fname)
        c = bufcount(fname)
        normal(fname)
        return c
except ImportError:
    import warnings
    warnings.warn("can't import fadvise: fadvcount() will be unavailable", UserWarning)

def clear_cache():
    """Clear disk cache on Linux."""
    os.system("/bin/sync ; /usr/bin/sudo /bin/sh -c '/bin/echo 3 > /proc/sys/vm/drop_caches'")

def main():
    ''' main '''
    counts = defaultdict(list)
    default_fn = 'big.txt'

    if '--clear-cache' in sys.argv:
        sys.argv.remove('--clear-cache')
        do_clear_cache = True
    else:
        do_clear_cache = False

    filename = sys.argv[1] if len(sys.argv) > 1 else default_fn
    for _ in range(3):
        for func in (f
                     for n, f in globals().items()
                     if n.endswith('count') and hasattr(f, '__call__')):
            if do_clear_cache:
                clear_cache()
            start_time = timer()
            # http://norvig.com/big.txt
            if filename == 'big.txt':
                assert func(filename) == 1000000 # 1000000 1000000 8245905 big.txt
            else:
                func(filename)
            counts[func].append(timer() - start_time)

    timings = {}
    for key, vals in counts.items():
        timings[key.__name__] = sum(vals) / float(len(vals)), min(vals)
    width = max(len(n) for n in timings) + 1
    print("%s %s %s %s" % (
        "function".ljust(width),
        "average, s".rjust(11),
        "min, s".rjust(7),
        "ratio".rjust(6)))
    absmin_ = min(x[1] for x in timings.values())
    for name, (av, min_) in sorted(timings.items(), key=lambda x: x[1][1]):
        print("%s %11.2g %7.2g %6.2f" % (
            name.ljust(width), av, min_, min_/absmin_))

if __name__ == '__main__':
    main()

# function      average, s  min, s  ratio
# wccount            0.005  0.0042   1.00
# bufcount          0.0081  0.0081   1.91
# fadvcount         0.0094  0.0091   2.13
# opcount            0.018   0.015   3.42
# simplecount        0.019   0.016   3.66
# kylecount          0.019   0.017   4.03
# mapcount           0.027   0.021   4.97
# itercount          0.044   0.031   7.21

## python3.1 ginstrom.py
# function      average, s  min, s  ratio
# wccount           0.0049  0.0046   1.00
# itercount          0.021    0.02   4.47
# mapcount           0.023   0.023   5.09
# bufcount           0.034   0.032   7.02
# opcount            0.043   0.043   9.46
# simplecount         0.05   0.046  10.20
# kylecount           0.05    0.05  10.95

## python ginstrom.py /big/mkv/file
# function      average, s  min, s  ratio
# wccount             0.51    0.49   1.00
# opcount              1.8     1.8   3.58
# simplecount          1.8     1.8   3.66
# kylecount            1.9     1.9   3.75
# mapcount              19       2   4.01
# fadvcount            2.3     2.2   4.52
# bufcount             2.3     2.2   4.52
## wc /big/mkv/file
## 7137518   40523351 1836139137 /big/mkv/file

## with --clear-cache
# function      average, s  min, s  ratio
# simplecount         0.06   0.057   1.00
# opcount            0.067   0.057   1.00
# kylecount          0.057   0.057   1.00
# itercount           0.06   0.058   1.02
# mapcount           0.059   0.058   1.02
# fadvcount          0.064   0.058   1.02
# bufcount            0.07   0.062   1.09
# wccount            0.072   0.065   1.15

## python3.1 with --clear-cache
# function      average, s  min, s  ratio
# itercount          0.061   0.057   1.00
# simplecount        0.069   0.061   1.06
# mapcount           0.062   0.061   1.07
# wccount            0.067   0.064   1.11
# kylecount          0.067   0.065   1.12
# opcount            0.072   0.067   1.17
# bufcount           0.083   0.073   1.27
