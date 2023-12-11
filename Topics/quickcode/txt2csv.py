#!/usr/bin/env python3
# coding: utf-8

'''
translate txt into csv with the format:
keys,character

YV,土
'''

import glob
import re


def parse_file(fn):
    ''' parse_file '''
    words = []
    ofn = fn.replace('.txt', '.csv')
    print(f'output to {ofn}')
    with open(fn, 'rt', encoding='utf8') as f:
        for ln in f:
            m = re.findall(r'(\S+)\s+=\s+(\S+)', ln.strip())
            for item in m:
                (vv, kk) = item
                words.append((kk, vv))

    radical_dict = dict(words)
    radical_keys = list(radical_dict.keys())
    radical_keys.sort()
    with open(ofn, 'wt', encoding='utf8') as csv:
        for ii in radical_keys:
            vv = radical_dict[ii]
            oline = f'{ii},{vv}\n'.format(ii, )
            csv.write(oline)


def main():
    ''' main '''
    arr = glob.glob('t?.txt')
    arr.sort()
    for ff in arr:
        parse_file(ff)

if __name__ == '__main__':
    main()
