#!/usr/bin/env python3
# coding: utf-8

''' show input character in which unicode block '''

from unicode_blocks import UnicodeBlock

def get_cjkblocks():
    ''' main '''
    with UnicodeBlock() as s:
        blocks = s.get_blocks()
        cjk_blocks = list()
        for start, end, name in blocks:
            try:
                _ = name.index('CJK')
                print('{:06x} ... {:06x}  {}'.format(start, end, name))
                cjk_blocks.append([start, end, name])
            except ValueError:
                pass
    return cjk_blocks

def main():
    ''' main '''
    get_cjkblocks()


if __name__ == '__main__':
    main()
