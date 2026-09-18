#!/usr/bin/env python3
'''Inspect a prime data file, choosing a handler based on file extension.'''

import argparse
import json
import pickle
import sys
from array import array
from pathlib import Path
from time import perf_counter

try:
    import numpy as np  # type: ignore[reportMissingTypeStubs]
except ImportError:
    print('[info] numpy not available, falling back to array module')
    np = None

_ARRAY_TYPECODES = {'.u32': 'I', '.u64': 'Q'}
_ARRAY_DTYPES = {'.u32': '<u4', '.u64': '<u8'}


def _load_text(path: Path) -> list[int]:
    ''' load a plain-text prime list, one value per line '''
    with path.open('r') as f:
        return [int(line) for line in f]


def _load_pickle(path: Path) -> list[int]:
    ''' load a pickled prime list '''
    with path.open('rb') as f:
        return pickle.load(f)


def _load_array(path: Path, ext: str) -> list[int]:
    ''' load a little-endian uint32/uint64 binary prime list '''
    if np is not None:
        return np.fromfile(path, dtype=_ARRAY_DTYPES[ext]).tolist()
    values = array(_ARRAY_TYPECODES[ext])
    with path.open('rb') as f:
        values.frombytes(f.read())
    if sys.byteorder != 'little':
        values.byteswap()
    return values.tolist()


def inspect(path: Path, as_json: bool = False) -> None:
    ''' inspect a prime data file and print basic stats '''
    ext = path.suffix.lower()
    started = perf_counter()
    if ext == '.txt':
        values = _load_text(path)
    elif ext == '.p':
        values = _load_pickle(path)
    elif ext in ('.u32', '.u64'):
        values = _load_array(path, ext)
    else:
        print(f'[FAIL] unsupported file extension: {ext}')
        sys.exit(1)
    elapsed = perf_counter() - started

    if not values:
        if as_json:
            print(json.dumps({'file': str(path), 'format': ext, 'count': 0}))
        else:
            print(f'{path}: empty')
        return

    if as_json:
        result = {
            'file': str(path),
            'format': ext,
            'count': len(values),
            'min': min(values),
            'max': max(values),
            'first': values[0],
            'last': values[-1],
            'elapsed_sec': elapsed,
        }
        print(json.dumps(result))
        return

    print(f'file: {path}')
    print(f'format: {ext}')
    print(f'count: {len(values):,}')
    print(f'min: {min(values):,}')
    print(f'max: {max(values):,}')
    print(f'first: {values[0]:,}')
    print(f'last: {values[-1]:,}')
    print(f'loaded in {elapsed:.3f} sec')


def main() -> None:
    ''' parse command-line arguments and inspect the file '''
    parser = argparse.ArgumentParser(
        description='Inspect a prime data file (.txt, .p, .u32, .u64).'
    )
    parser.add_argument('input', type=Path)
    parser.add_argument('-j', '--json', action='store_true', help='output a JSON object')
    args = parser.parse_args()
    inspect(args.input, as_json=args.json)


if __name__ == '__main__':
    main()
