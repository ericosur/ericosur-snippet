#!/usr/bin/python3
# coding: utf-8

'''
This script will generate a script which write embedded data into file.
'''

import argparse
import base64
import time

def gen_script(dfn: str, ofn: str) -> None:
    ''' main '''
    content = None
    start = time.time()
    with open(dfn, 'rb') as fin:
        content = fin.read()
        print(f'content len: {len(content)}')
    duration = time.time() - start
    print(f'duration: {duration}')

    b64str = base64.b64encode(content).decode('utf-8')
    del content
    print(f'base64 len: {len(b64str)}')
    #print("type:", type(b64str))

    with open(ofn, 'wt', encoding='utf8') as fobj:
        print('''
#!/usr/bin/python3
# coding: utf-8

""" This script is auto generated by mk-embed-script.py """

import base64
import os
import sys

''', file=fobj)
        print(f'ofn = "{dfn}"', file=fobj)
        print('''
if os.path.exists(ofn):
    print("WARN:", ofn, "exists, will skip...")
    sys.exit(1)
''', file=fobj)
        print('''b64str = """''', file=fobj)
        fobj.write(b64str)
        print('''"""
b64bytes = b64str.encode('utf-8')
u64b = base64.b64decode(b64bytes)
print(f'len: {len(u64b)}')
print("type:", type(u64b))
with open(ofn, 'wb') as fo:
    fo.write(u64b)
print('output to:', ofn)
''', file=fobj)

    print('output to:', ofn)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='script to generate data embedded script')
    parser.add_argument('-o', '--output', default='write_smt.py',
        help='The output script filename')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-d', '--data', required=True,
        help='The data file (compressed file recommended)')

    args = parser.parse_args()

    if args.output:
        print('output:', args.output)
    if args.data:
        print('data:', args.data)

    gen_script(args.data, args.output)

if __name__ == '__main__':
    main()