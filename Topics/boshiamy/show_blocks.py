#!/usr/bin/env python3
# coding: utf-8

'''
output specified section into
codepoint char
format

eg:
1234  我
'''

from unicode_blocks import UnicodeBlock

def get_cjkblocks(n: str):
    ''' main '''
    s = 0
    e = 0
    u = UnicodeBlock()
    bs = u.get_blocks()

    for start, end, name in bs:
        try:
            if name == n:
                s = start
                e = end
                print(f'{start:06x} ... {end:06x}  {name}')
                break
        except ValueError:
            pass

    cnt = 0
    fn = 'ext-e.txt'
    print(f'output to {fn}')
    with open(fn, 'wt', encoding='utf8') as f:
        for i in range(s, e + 1):
            cnt += 1
            l = f'{i:5x} {chr(i)}\n'
            f.write(l)
    print('cnt:', cnt)

def main():
    ''' main '''
    toks = ['CJK Unified Ideographs Extension A', 'CJK Unified Ideographs Extension B',
        'CJK Unified Ideographs Extension C', 'CJK Unified Ideographs Extension D',
        'CJK Unified Ideographs Extension E']
    get_cjkblocks(toks[-1])


if __name__ == '__main__':
    main()
