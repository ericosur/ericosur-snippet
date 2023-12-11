#!/usr/bin/python3
# coding: utf-8

'''
read liu.json
3400..4DBF; CJK Unified Ideographs Extension A

'''

import json
from typing import Dict, List

from unicode_blocks import UnicodeBlock


def check_cjk_b(items: list):
    ''' check '''
    cnt = 0
    c = 0
    for i in range(0x20000, 0x2a6df + 1):
        cnt += 1
        s = str(i)
        if s in items:
            c += 1
        else:
            print(f'missing: {i:06x}')
    print('cnt:', cnt)
    print('c:', c)

def get_available_codepoint_in_block(cjk_blocks: List) -> Dict:
    ''' return a dict of {block name: number of codepoints} '''
    cjk = {}
    for start, end, name in cjk_blocks:
        cjk[name] = end - start + 1
    return cjk

def main():
    ''' main '''
    fn = 'liu.json'
    data = None
    with open(fn, 'rt', encoding='utf8') as fobj:
        data = json.load(fobj)
    ub = UnicodeBlock()
    cjk_blocks = ub.get_cjkblocks()
    # store how many codepoint available in this block
    cjk = get_available_codepoint_in_block(cjk_blocks)
    # if char in this block, store here
    subset = {}
    cnt = 0
    for k in data.keys():
        try:
            cp = int(k)
            cnt += 1
            for start, end, name in cjk_blocks:
                if not name in subset:
                    subset[name] = []
                if start <= cp <= end:
                    subset[name].append(k)
        except TypeError as e:
            print(f"err: {e} at {k}")
        except ValueError as e:
            print(f"err: {e} at {k}")

    print(f'[INFO] From {fn} it could output {cnt} han characters/symbols')
    print(f'[INFO] There are {len(subset)} blocks name with CJK')
    for category in sorted(subset.keys()):
        print(f'Block [{category:40s}]: {len(subset[category]):6d} / {cjk[category]}')
    # ofn = 'cjks.json'
    # with open(ofn, 'wt') as of:
    #     of.write(json.dumps(subset, indent=2, sort_keys=True))

    # print('len of cjk_b:', len(subset['CJK Unified Ideographs Extension B']))
    # check_cjk_b(subset['CJK Unified Ideographs Extension B'])

if __name__ == '__main__':
    main()
