#!/usr/bin/python
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

# if 57, one line 76 characters
# use 3n to avoid padding issues (4 char from 3 bytes)
CHUNK_SIZE = 57

import os
import stat
from loguru import logger

logd = logger.debug
logi = logger.info

def is_chardev(filepath) -> bool:
    ''' return if a char dev '''
    mode = os.stat(filepath).st_mode  # Get the file's mode
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

def encode_file_to_base64_chunked(file_path, chunk_size=CHUNK_SIZE):
    ''' read file into chunks, and base64 encoding chunk by chunk
        it is iterable
    '''
    max_repeat, cnt = -1, 0
    # if char dev, repeat in limited count
    if is_chardev(file_path):
        max_repeat = 2

    with open(file_path, "rb") as file:
        while chunk := file.read(chunk_size):
            if max_repeat>0 and cnt > max_repeat:
                break
            # Encode the current chunk to Base64
            base64_chunk = base64.b64encode(chunk)
            # Convert bytes to string for each chunk (if needed)
            yield base64_chunk.decode('utf-8')
            cnt += 1

def main():
    ''' main '''
    # Usage example: print each chunk of Base64 encoded data
    fn = "/dev/urandom"
    for base64_chunk in encode_file_to_base64_chunked(fn):
        print(base64_chunk)

if __name__ == "__main__":
    main()
