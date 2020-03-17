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

def get_cjkblocks(n):
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
                print('{:06x} ... {:06x}  {}'.format(start, end, name))
                break
        except ValueError:
            pass

    cnt = 0
    with open('ext-e.txt', 'wt') as f:
        for i in range(s, e + 1):
            cnt += 1
            l = '{:5x} {}\n'.format(i, chr(i))
            f.write(l)
    print('cnt:', cnt)

def main():
    ''' main '''
    t = 'CJK Unified Ideographs Extension E'
    get_cjkblocks(t)


if __name__ == '__main__':
    main()
