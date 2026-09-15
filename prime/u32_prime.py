#!/usr/bin/env python3
'''Query the h422 prime table stored as a memory-mapped uint32 file.'''

import argparse
import random
from pathlib import Path

import numpy as np

DEFAULT_DATA_FILE = Path.home() / '.prime' / 'h422.u32'


class PrimeTableU32:
    '''Read a sorted little-endian uint32 prime table with NumPy.'''

    def __init__(self, filename: Path = DEFAULT_DATA_FILE) -> None:
        if not filename.is_file():
            raise FileNotFoundError(f'prime data file not found: {filename}')
        if filename.stat().st_size == 0 or filename.stat().st_size % 4:
            raise ValueError(f'invalid uint32 data file: {filename}')
        self.filename = filename
        self.primes = np.memmap(filename, dtype='<u4', mode='r')

    def __str__(self) -> str:
        return (
            f'min: {int(self.primes[0])}, '
            f'max: {int(self.primes[-1]):,}, '
            f'total primes: {len(self.primes):,}'
        )

    def at(self, index: int) -> int | None:
        '''Return the prime at index, or None when index is invalid.'''
        if index < 0 or index >= len(self.primes):
            return None
        return int(self.primes[index])

    def get_around(self, value: int) -> tuple[int | None, int | None]:
        '''Return lower and upper indexes around value.'''
        if value < int(self.primes[0]) or value > int(self.primes[-1]):
            return None, None
        index = int(np.searchsorted(self.primes, value, side='left'))
        if index < len(self.primes) and int(self.primes[index]) == value:
            return index, None
        return index - 1, index

    def list_nearby(self, value: int, count: int = 4) -> list[int] | None:
        '''Return up to count primes on each side of value.'''
        lower, _upper = self.get_around(value)
        if lower is None:
            return None
        start = max(0, lower - count)
        stop = min(len(self.primes), lower + count + 2)
        return [int(prime) for prime in self.primes[start:stop]]


def show_result(table: PrimeTableU32, value: int) -> None:
    '''Print the prime or the two surrounding primes for value.'''
    lower, upper = table.get_around(value)
    if lower is None:
        print(f'{value:,} is outside the prime table')
        return
    if upper is None:
        print(f'{value:,} is prime at index {lower:,}')
        return
    lower_value = table.at(lower)
    upper_value = table.at(upper)
    print(f'{value:,}: ({lower_value:,} <-----> {upper_value:,})')


def main() -> None:
    '''Parse values and query the h422 uint32 table.'''
    parser = argparse.ArgumentParser(
        description='Query primes from ~/.prime/h422.u32.'
    )
    parser.add_argument(
        'values', metavar='int', type=int, nargs='*',
        help='integers to test; random values are used when omitted',
    )
    parser.add_argument(
        '--file', type=Path, default=DEFAULT_DATA_FILE,
        help=f'uint32 data file (default: {DEFAULT_DATA_FILE})',
    )
    args = parser.parse_args()

    table = PrimeTableU32(args.file)
    print(table)
    values = args.values
    if not values:
        minimum = int(table.primes[0])
        maximum = int(table.primes[-1])
        values = [random.randint(minimum, maximum) for _ in range(10)]
    for value in values:
        show_result(table, value)


if __name__ == '__main__':
    main()
