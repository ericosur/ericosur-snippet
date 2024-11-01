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

# if 57, one line 76 characters
# use 3n to avoid padding issues (4 char from 3 bytes)
CHUNK_SIZE = 57

# Function to encode a file to base64 in chunks
def encode_file_to_base64_chunked(file_path, chunk_size=CHUNK_SIZE):
    ''' read file into chunks, and base64 encoding chunk by chunk '''
    with open(file_path, "rb") as file:
        while chunk := file.read(chunk_size):
            # Encode the current chunk to Base64
            base64_chunk = base64.b64encode(chunk)
            # Convert bytes to string for each chunk (if needed)
            yield base64_chunk.decode('utf-8')

def main():
    ''' main '''
    # Usage example: print each chunk of Base64 encoded data
    fn = "r.bin"
    for base64_chunk in encode_file_to_base64_chunked(fn):
        print(base64_chunk)

if __name__ == "__main__":
    main()
