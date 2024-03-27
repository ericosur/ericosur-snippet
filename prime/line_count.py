#!/usr/bin/env python
# coding: utf-8

'''
A benchmark for various function to count lines in a text file. It is not
always the same between different python version.

line_count.py --clear-cache

https://gist.github.com/zed/0ac760859e614cd03652
https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
'''

import mmap
import os
import subprocess
import sys

from collections import defaultdict
from timeit import default_timer as timer

from store import GetConfig

def wrap_config():
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey("large")    # change this to use larger table
    txtfn = obj.get_full_path("txt")
    return txtfn


# pylint: disable=consider-using-f-string
# pylint: disable=consider-using-with

def mapcount(filename):
    ''' memory map '''
    with open(filename, "r+t", encoding='utf8') as f:
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
    return lines

def simplecount(filename):
    ''' simple count '''
    lines = 0

    with open(filename, 'rt', encoding='utf8') as fobj:
        for _ in fobj:
            lines += 1
    return lines

def bufcount(filename):
    ''' buf count '''
    lines = 0
    buf_size = 1024 * 1024
    with open(filename, encoding='utf8') as f:
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
    #return sum(1 for _ in open(filename, 'rbU'))
    return sum(1 for _ in open(filename, 'rb'))

def opcount(fname):
    ''' use enumerate '''
    line_number = 0
    with open(fname, encoding='utf8') as f:
        for line_number, _ in enumerate(f, 1):
            pass
    return line_number

def kylecount(fname):
    ''' kyle count '''
    with open(fname, encoding='utf8') as fobj:
        res = sum(1 for line in fobj)
    return res
    #return sum(1 for line in open(fname))

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
    default_fn = wrap_config()

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
        print(f'{name.ljust(width)} {av:11.2g} {min_:7.2g} {min_/absmin_:6.2f}')

if __name__ == '__main__':
    main()
