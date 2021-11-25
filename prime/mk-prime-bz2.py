#!/usr/bin/python3
# coding: utf-8

'''
read prime_100k.txt
'''

import bz2
import base64
import time
import os

def get_home():
    ''' return $HOME '''
    return os.getenv('HOME')

def get_datapath():
    ''' get the full path of data file '''
    fn = get_home() + '/.prime/small.txt'
    return fn

def main():
    ''' main '''
    fn = get_datapath()
    print('fn:', fn)

    start = time.time()
    compressed = None
    content = None
    with open(fn, 'rb') as fin:
        content = fin.read()
        print(f'len: {len(content)}')
        compressed = bz2.compress(content)
        print(f'len: {len(compressed)}')
        print("type:", type(compressed))
    del content
    duration = time.time() - start
    print(f'duration: {duration}')

    b64str = base64.b64encode(compressed).decode('utf-8')
    print(f'len: {len(b64str)}')
    print("type:", type(b64str))

    ofn = 'write-small.py'
    with open(ofn, 'wt', encoding='utf8') as fobj:
        print('''
#!/usr/bin/python3
# coding: utf-8

import base64
import bz2

b64str = """''', file=fobj)
        fobj.write(b64str)
        print('''"""
ofn = 'small.txt'
b64bytes = b64str.encode('utf-8')
u64b = base64.b64decode(b64bytes)
uncompress = bz2.decompress(u64b).decode('utf-8')
print(f'len: {len(uncompress)}')
print("type:", type(uncompress))
with open(ofn, 'wt', encoding='utf-8') as fo:
    fo.write(uncompress)
print('output to:', ofn)
''', file=fobj)

    print('output to:', ofn)

if __name__ == '__main__':
    main()
