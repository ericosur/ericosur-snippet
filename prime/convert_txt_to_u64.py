#!/usr/bin/env python3
'''Convert a plain-text prime list (one value per line) to a little-endian uint64 binary file.'''

import argparse
from pathlib import Path
from tempfile import NamedTemporaryFile
from time import perf_counter

import numpy as np

CHUNK_LINES = 1_000_000


def convert(input_path: Path, output_path: Path) -> None:
    '''Stream-convert a text prime list to a uint64 file, bounding memory to one chunk at a time.'''
    started = perf_counter()
    total = 0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with input_path.open('r') as text_file, NamedTemporaryFile(
        mode='wb', dir=output_path.parent, prefix=f'{output_path.name}.',
        delete=False,
    ) as out_file:
        temporary_path = Path(out_file.name)
        chunk: list[int] = []
        for line in text_file:
            chunk.append(int(line))
            if len(chunk) == CHUNK_LINES:
                np.array(chunk, dtype='<u8').tofile(out_file)
                total += len(chunk)
                chunk.clear()
        if chunk:
            np.array(chunk, dtype='<u8').tofile(out_file)
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
    default_output = Path.home() / '.prime' / 'part2.u64'
    parser = argparse.ArgumentParser(
        description='Convert a plain-text prime list to little-endian uint64.'
    )
    parser.add_argument('input', type=Path)
    parser.add_argument('output', nargs='?', type=Path, default=default_output)
    args = parser.parse_args()
    convert(args.input, args.output)


if __name__ == '__main__':
    main()
