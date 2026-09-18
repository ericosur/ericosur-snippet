#!/usr/bin/env python3
'''Convert a plain-text prime list (one value per line) to pickle, uint32, or uint64 binary.'''

import argparse
import pickle
import sys
from array import array
from pathlib import Path
from tempfile import NamedTemporaryFile
from time import perf_counter

try:
    import numpy as np  # type: ignore[reportMissingTypeStubs]
except ImportError:
    np = None

CHUNK_LINES = 1_000_000
UINT32_MAX = 0xFFFFFFFF

FMT_PICKLE = 'pickle'
FMT_U32 = 'u32'
FMT_U64 = 'u64'

_TYPECODES = {FMT_U32: 'I', FMT_U64: 'Q'}
_DTYPES = {FMT_U32: '<u4', FMT_U64: '<u8'}


def _write_chunk(chunk: list[int], out_file, typecode: str, dtype: str) -> None:
    '''Write a chunk of values as little-endian binary, using numpy if available.'''
    if np is not None:
        np.array(chunk, dtype=dtype).tofile(out_file)
        return
    values = array(typecode, chunk)
    if sys.byteorder != 'little':
        values.byteswap()
    values.tofile(out_file)


def convert(input_path: Path, output_path: Path, fmt: str) -> None:
    '''Stream-convert a text prime list to a pickle, uint32, or uint64 file.'''
    started = perf_counter()
    total = 0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    typecode = _TYPECODES.get(fmt)
    dtype = _DTYPES.get(fmt)
    with input_path.open('r') as text_file, NamedTemporaryFile(
        mode='wb', dir=output_path.parent, prefix=f'{output_path.name}.',
        delete=False,
    ) as out_file:
        temporary_path = Path(out_file.name)
        if fmt == FMT_PICKLE:
            values = [int(line) for line in text_file]
            pickle.dump(values, out_file)
            total = len(values)
        else:
            assert typecode is not None and dtype is not None
            chunk: list[int] = []
            for line in text_file:
                value = int(line)
                if fmt == FMT_U32 and not 0 <= value <= UINT32_MAX:
                    print(f'[WARN] value out of uint32 range: {value}, stopping early, keeping partial output')
                    break
                chunk.append(value)
                if len(chunk) == CHUNK_LINES:
                    _write_chunk(chunk, out_file, typecode, dtype)
                    total += len(chunk)
                    chunk.clear()
            if chunk:
                _write_chunk(chunk, out_file, typecode, dtype)
                total += len(chunk)

    temporary_path.replace(output_path)
    elapsed = perf_counter() - started
    size_mib = output_path.stat().st_size / (1024 * 1024)
    print(
        f'converted {total:,} values to {output_path} '
        f'({size_mib:.1f} MiB) in {elapsed:.3f} sec'
    )


def main() -> None:
    '''Parse command-line arguments and convert the prime list.'''
    parser = argparse.ArgumentParser(
        description='Convert a plain-text prime list to pickle, uint32, or uint64.'
    )
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-p', '--pickle', action='store_true',
        help='convert to a python pickle (stdlib only)',
    )
    group.add_argument(
        '--u32', action='store_true',
        help='convert to a little-endian uint32 binary file',
    )
    group.add_argument(
        '--u64', action='store_true',
        help='convert to a little-endian uint64 binary file',
    )
    args = parser.parse_args()
    if args.pickle:
        fmt = FMT_PICKLE
    elif args.u32:
        fmt = FMT_U32
    else:
        fmt = FMT_U64
    convert(args.input, args.output, fmt)


if __name__ == '__main__':
    main()
