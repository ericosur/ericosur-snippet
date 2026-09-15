'''
Run benchmark for config h422
to compare:
  - text
  - pickle
  - lzma
'''

import pickle
import sys
from pathlib import Path
from time import perf_counter

import compress_pickle
import numpy as np
from bench_common import setup_local_paths

try:
    setup_local_paths()
except ImportError as e:
    print(f"failed to setup local paths: {e}")
    sys.exit(1)

from madlog import get_console  # type: ignore[reportMissingImports]

from store import GetConfig, prt  # type: ignore[reportAttributeAccessIssue]
from store.textutil import read_textfile


def _report_load(name: str, filename: str, started: float,
                 primes: list[int]) -> list[int]:
    duration = perf_counter() - started
    prt(f'{name}: {filename}: {len(primes):,} values in {duration:.3f} sec')
    return primes


def load_from_text(filename: str) -> list[int]:
    '''Load primes from a newline-delimited text file.'''
    started = perf_counter()
    primes = read_textfile(filename)
    return _report_load('text', filename, started, primes)


def load_from_pickle(filename: str) -> list[int]:
    '''Load primes from an uncompressed pickle file.'''
    started = perf_counter()
    with open(filename, 'rb') as input_file:
        primes: list[int] = pickle.load(input_file)
    return _report_load('pickle', filename, started, primes)


def load_from_lzma(filename: str) -> list[int]:
    '''Load primes from a compressed pickle file.'''
    started = perf_counter()
    primes: list[int] = compress_pickle.load(filename)
    return _report_load('lzma', filename, started, primes)


def load_from_u32(filename: str) -> np.memmap:
    '''Memory-map a little-endian uint32 prime table.'''
    started = perf_counter()
    path = Path(filename)
    if path.stat().st_size == 0 or path.stat().st_size % 4:
        raise ValueError(f'invalid uint32 data file: {filename}')
    primes = np.memmap(path, dtype='<u4', mode='r')
    duration = perf_counter() - started
    prt(f'u32: {filename}: {len(primes):,} values mapped in {duration:.3f} sec')
    return primes


class Solution:
    def __init__(self) -> None:
        self.config = GetConfig()
        self.config.set_configkey('h422')
        self.sett = self.config.get_config()

    def run(self) -> None:
        ''' run test on text, pickle, and lzma '''
        d = self.sett
        if d is None:
            raise RuntimeError('Configuration is not available')
        with get_console().status("[bold green]Loading primes..."):
            load_from_u32(self.config.get_full_path('u32'))
            load_from_pickle(self.config.get_full_path('pickle'))
            load_from_lzma(self.config.get_full_path('compress_pickle'))
            load_from_text(self.config.get_full_path('txt'))

def main():
    ''' main '''
    obj = Solution()
    obj.run()

if __name__ == '__main__':
    main()
