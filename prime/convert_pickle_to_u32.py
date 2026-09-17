#!/usr/bin/env python3
'''Convert a pickle prime table to a little-endian uint32 binary file.'''

import argparse
import pickle
from pathlib import Path
from tempfile import NamedTemporaryFile
from time import perf_counter

import numpy as np  # type: ignore[import]

UINT32_MAX = np.iinfo(np.uint32).max


def convert(input_path: Path, output_path: Path) -> None:
    '''Convert a pickled integer sequence to a uint32 file.'''
    started = perf_counter()
    with input_path.open('rb') as input_file:
        primes: list[int] = pickle.load(input_file)

    if not primes:
        raise ValueError(f'input contains no values: {input_path}')
    minimum = min(primes)
    maximum = max(primes)
    if minimum < 0 or maximum > UINT32_MAX:
        raise ValueError(
            f'values must fit uint32; found range {minimum}..{maximum}'
        )

    values = np.asarray(primes, dtype='<u4')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        mode='wb', dir=output_path.parent, prefix=f'{output_path.name}.',
        delete=False,
    ) as temporary_file:
        temporary_path = Path(temporary_file.name)
        values.tofile(temporary_file)

    temporary_path.replace(output_path)
    elapsed = perf_counter() - started
    size_mib = output_path.stat().st_size / (1024 * 1024)
    print(
        f'converted {len(values):,} values to {output_path} '
        f'({size_mib:.1f} MiB) in {elapsed:.3f} sec'
    )


def main() -> None:
    '''Parse command-line arguments and convert the prime table.'''
    default_input = Path.home() / '.prime' / 'h422.p'
    default_output = default_input.with_suffix('.u32')
    parser = argparse.ArgumentParser(
        description='Convert a pickled prime table to little-endian uint32.'
    )
    parser.add_argument('input', nargs='?', type=Path, default=default_input)
    parser.add_argument('output', nargs='?', type=Path, default=default_output)
    args = parser.parse_args()
    convert(args.input, args.output)


if __name__ == '__main__':
    main()
