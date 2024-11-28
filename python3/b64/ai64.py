#!/usr/bin/env python3
#coding:UTF-8

'''
the ouput will be same as /usr/bin/base64

test:
dd if=/dev/urandom of=r.bin bs=307 count=101
base64 r.bin > b.txt
py ai64.py > a.txt
md5sum ?.txt
'''

import base64
import os
import stat
import sys

sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from myutil import is_linux

from typing_extensions import Annotated
import typer
# if 57, one line 76 characters
# use 3n to avoid padding issues (4 char from 3 bytes)
CHUNK_SIZE = 57
USE_LOGGER = False
try:
    from loguru import logger
    USE_LOGGER = True
except ImportError:
    print("cannot import module: loguru")

def do_nothing(*args):
    ''' do nothing '''
    return args

def is_chardev(filepath, log=do_nothing) -> bool:
    ''' return if a char dev '''
    logd = log
    mode = os.stat(filepath).st_mode  # Get the file's mode
    logd(f'{mode=}')
    if stat.S_ISCHR(mode):
        return True
    # if stat.S_ISREG(mode): return "Regular file"
    # elif stat.S_ISDIR(mode): return "Directory"
    # elif stat.S_ISBLK(mode): return "Block device"
    # elif stat.S_ISFIFO(mode): return "FIFO (named pipe)"
    # elif stat.S_ISSOCK(mode): return "Socket"
    # elif stat.S_ISLNK(mode): return "Symbolic link"
    # else: return "Unknown type"
    # except FileNotFoundError: return "File not found"
    # except PermissionError: return "Permission denied"
    return False

def encode_file_to_base64_chunked(file_path, chunk_size=CHUNK_SIZE, log=do_nothing):
    ''' read file into chunks, and base64 encoding chunk by chunk
        it is iterable
    '''
    logd = log
    max_repeat, cnt = -1, 0
    logd(f'{file_path=}')
    logd(f'{chunk_size=}')
    # if char dev, repeat in limited count
    if is_chardev(file_path):
        max_repeat = 2

    with open(file_path, "rb") as file:
        while chunk := file.read(chunk_size):
            if 0 < max_repeat < cnt:
                logd("reach the max repeat, break...")
                break
            # Encode the current chunk to Base64
            base64_chunk = base64.b64encode(chunk)
            # Convert bytes to string for each chunk (if needed)
            yield base64_chunk.decode('utf-8')
            cnt += 1

def main(
        input_fn: Annotated[str, typer.Option("--input", "-i", help="specify input file")]=None,
        debug: Annotated[bool, typer.Option("--debug", "-d", help="show debug info")]=False,
        chunk: Annotated[int, typer.Option("--chunk", "-c",
                                    help="specify the size of chunk")] = 57,
):
    '''
    print each chunk of Base64 encoded data
    Usage example:

    dd if=/dev/urandom of=abc.bin count=57 bs=1

    ai64.py --input abc.bin

    RZv+frUlOjplVto6Bwdjn2ZXr/2ARvV9ZX+LaFgkgLfDDtyplU+IogelNQXu77dsC5Z61pXFLWy5
    '''

    logd = do_nothing
    if debug:
        if USE_LOGGER:
            logd = logger.debug
        else:
            logd = print

    fn = None
    if is_linux():
        fn = "/dev/urandom"
    logd(f'{fn=}')

    if input_fn and os.path.isfile(input_fn):
        fn = input_fn
        logd(fn)
    if fn is None:
        print('You MUST specify a file or file not found?')
        sys.exit(1)
    for base64_chunk in encode_file_to_base64_chunked(fn, chunk_size=chunk, log=logd):
        print(base64_chunk)

if __name__ == "__main__":
    typer.run(main)
