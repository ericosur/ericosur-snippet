#!/usr/bin/env python3
'''Query a prime table split across two files: a uint32 low range and a uint64
high range. The two files must be contiguous (the high file's first value is the
prime immediately after the low file's last value), so together they behave as
one sorted sequence. Lookups use seek()+read() binary search rather than mmap:
in this environment mmap+np.searchsorted was observed to pull the entire file(s)
into RSS on first touch, while seek()+read() stays at a few probes worth of I/O.
'''

import argparse
import random
import struct
from pathlib import Path

DEFAULT_LOW_FILE = Path.home() / '.prime' / 'h422.u32'
DEFAULT_HIGH_FILE = Path.home() / '.prime' / 'part2.u64'

LOW_FMT, LOW_SIZE = '<I', 4
HIGH_FMT, HIGH_SIZE = '<Q', 8


class _FileArray:
    '''A sorted fixed-width binary file, read via seek()+read() binary search.'''

    def __init__(self, path: Path, fmt: str, size: int) -> None:
        if not path.is_file():
            raise FileNotFoundError(f'prime data file not found: {path}')
        file_size = path.stat().st_size
        if file_size == 0 or file_size % size:
            raise ValueError(f'invalid binary data file: {path}')
        self.count = file_size // size
        self.fmt = fmt
        self.size = size
        self.file = path.open('rb')

    def __len__(self) -> int:
        return self.count

    def at(self, index: int) -> int:
        self.file.seek(index * self.size)
        return struct.unpack(self.fmt, self.file.read(self.size))[0]

    def search(self, value: int) -> tuple[int, bool]:
        '''Return (index, exact); index is the leftmost position with a value >= value.'''
        lo, hi = 0, self.count
        while lo < hi:
            mid = (lo + hi) // 2
            if self.at(mid) < value:
                lo = mid + 1
            else:
                hi = mid
        exact = lo < self.count and self.at(lo) == value
        return lo, exact


class CombinedPrimeTable:
    '''Read a sorted, contiguous low(uint32) + high(uint64) prime table pair.'''

    def __init__(
        self,
        low_file: Path = DEFAULT_LOW_FILE,
        high_file: Path = DEFAULT_HIGH_FILE,
    ) -> None:
        self.low = _FileArray(low_file, LOW_FMT, LOW_SIZE)
        self.high = _FileArray(high_file, HIGH_FMT, HIGH_SIZE)
        self.low_min = self.low.at(0)
        self.low_max = self.low.at(len(self.low) - 1)
        self.high_min = self.high.at(0)
        self.high_max = self.high.at(len(self.high) - 1)

    def __str__(self) -> str:
        return (
            f'min: {self.low_min}, max: {self.high_max:,}, '
            f'total primes: {len(self.low) + len(self.high):,}'
        )

    def get_around(self, value: int) -> tuple[int | None, int | None]:
        '''Return (lower, upper) primes around value, or (prime, None) on an exact hit.'''
        if value < self.low_min or value > self.high_max:
            return None, None
        if self.low_max < value < self.high_min:
            return self.low_max, self.high_min  # falls in the gap between the two files

        if value <= self.low_max:
            index, exact = self.low.search(value)
            if exact:
                return value, None
            lower = self.low.at(index - 1) if index > 0 else None
            upper = self.low.at(index) if index < len(self.low) else self.high_min
            return lower, upper

        index, exact = self.high.search(value)
        if exact:
            return value, None
        lower = self.high.at(index - 1) if index > 0 else self.low_max
        upper = self.high.at(index) if index < len(self.high) else None
        return lower, upper


def show_result(table: CombinedPrimeTable, value: int) -> None:
    '''Print the prime or the two surrounding primes for value.'''
    lower, upper = table.get_around(value)
    if lower is None:
        print(f'{value:,} is outside the prime table')
        return
    if upper is None:
        print(f'{value:,} is prime' if lower == value else f'{lower:,} is prime')
        return
    print(f'{value:,}: ({lower:,} <-----> {upper:,})')


def main() -> None:
    '''Parse values and query the combined low/high prime table.'''
    parser = argparse.ArgumentParser(
        description='Query primes from a combined uint32 + uint64 table.'
    )
    parser.add_argument(
        'values', metavar='int', type=int, nargs='*',
        help='integers to test; random values are used when omitted',
    )
    parser.add_argument('--low-file', type=Path, default=DEFAULT_LOW_FILE)
    parser.add_argument('--high-file', type=Path, default=DEFAULT_HIGH_FILE)
    args = parser.parse_args()

    table = CombinedPrimeTable(args.low_file, args.high_file)
    print(table)
    values = args.values
    if not values:
        values = [random.randint(table.low_min, table.high_max) for _ in range(10)]
    for value in values:
        show_result(table, value)


if __name__ == '__main__':
    main()
