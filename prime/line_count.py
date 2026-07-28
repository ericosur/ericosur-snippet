#!/usr/bin/env python

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


def wrap_config() -> str:
    ''' wrap config and retrieve settings '''
    obj = GetConfig()
    obj.set_configkey("large")    # change this to use larger table
    txtfn: str = obj.get_full_path("txt")
    return txtfn


def mapcount(filename: str) -> int:
    ''' memory map '''
    file_size: int = os.path.getsize(filename)
    if file_size == 0:
        return 0
    
    with open(filename, "rb") as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as buf:
        lines: int = 0
        readline = buf.readline
        while readline():
            lines += 1
    return lines

def simplecount(filename: str) -> int:
    ''' simple count '''
    lines: int = 0

    with open(filename, 'rt', encoding='utf8') as fobj:
        for _ in fobj:
            lines += 1
    return lines

def bufcount(filename: str) -> int:
    ''' buf count '''
    lines: int = 0
    buf_size: int = 1024 * 1024
    with open(filename, encoding='utf8') as f:
        read_f = f.read # loop optimization
        buf: str = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            buf = read_f(buf_size)
    return lines

def wccount(filename: str) -> int:
    ''' external __wc -l__ '''
    out: bytes = subprocess.Popen(['/usr/bin/wc', '-l', filename],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT
                           ).communicate()[0]
    return int(out.partition(b' ')[0])

def itercount(filename: str) -> int:
    ''' itercount, what is U in open ???'''
    #return sum(1 for _ in open(filename, 'rbU'))
    return sum(1 for _ in open(filename, 'rb'))

def opcount(fname: str) -> int:
    ''' use enumerate '''
    line_number: int = 0
    with open(fname, encoding='utf8') as f:
        for line_number, _ in enumerate(f, 1):
            pass
    return line_number

def kylecount(fname: str) -> int:
    ''' kyle count '''
    with open(fname, encoding='utf8') as fobj:
        res: int = sum(1 for line in fobj)
    return res
    #return sum(1 for line in open(fname))

try:
    # http://chris-lamb.co.uk/projects/python-fadvise/
    from fadvise import normal, sequential  # type: ignore[import]
    def fadvcount(fname: str) -> int:
        ''' fadv count '''
        sequential(fname)
        c: int = bufcount(fname)
        normal(fname)
        return c
except ImportError:
    import warnings
    warnings.warn("can't import fadvise: fadvcount() will be unavailable", UserWarning)

def clear_cache() -> None:
    """Clear disk cache on Linux."""
    try:
        subprocess.run(["sync"], check=True, capture_output=True)
        subprocess.run(
            ["sudo", "sh", "-c", "echo 3 > /proc/sys/vm/drop_caches"],
            check=True,
            capture_output=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        import warnings
        warnings.warn(f"Failed to clear cache: {e}", UserWarning)

def main() -> None:
    ''' main '''
    counts: dict = defaultdict(list)
    default_fn: str = wrap_config()

    if '--clear-cache' in sys.argv:
        sys.argv.remove('--clear-cache')
        do_clear_cache: bool = True
    else:
        do_clear_cache: bool = False

    filename: str = sys.argv[1] if len(sys.argv) > 1 else default_fn
    for _ in range(3):
        for func in (f
                     for n, f in globals().items()
                     if n.endswith('count') and callable(f)):
            if do_clear_cache:
                clear_cache()
            start_time: float = timer()
            # http://norvig.com/big.txt
            if filename == 'big.txt':
                assert func(filename) == 1000000 # 1000000 1000000 8245905 big.txt
            else:
                func(filename)
            counts[func].append(timer() - start_time)

    timings = {}
    for key, vals in counts.items():
        timings[key.__name__] = sum(vals) / float(len(vals)), min(vals)
    width: int = max(len(n) for n in timings) + 1
    print(f"{('function').ljust(width)} {'average, s'.rjust(11)} {'min, s'.rjust(7)} {'ratio'.rjust(6)}")
    absmin_ = min(x[1] for x in timings.values())
    for name, (av, min_) in sorted(timings.items(), key=lambda x: x[1][1]):
        print(f'{name.ljust(width)} {av:11.2g} {min_:7.2g} {min_/absmin_:6.2f}')

if __name__ == '__main__':
    main()
