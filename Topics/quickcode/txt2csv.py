#!/usr/bin/env python3
# coding: utf-8

'''
translate txt into csv with the format:
keys,character

YV,土
'''

import re
import glob

def parse_file(fn):
    ''' parse_file '''
    words = []
    ofn = fn.replace('.txt', '.csv')
    print('output to {}'.format(ofn))
    with open(fn, 'r') as f:
        for ln in f:
            m = re.findall(r'(\S+)\s+=\s+(\S+)', ln.strip())
            for item in m:
                (vv, kk) = item
                words.append((kk, vv))

    radical_dict = dict(words)
    radical_keys = list(radical_dict.keys())
    radical_keys.sort()
    with open(ofn, 'w') as csv:
        for ii in radical_keys:
            oline = '{},{}\n'.format(ii, radical_dict[ii])
            csv.write(oline)


def main():
    ''' main '''
    arr = glob.glob('t?.txt')
    arr.sort()
    for ff in arr:
        parse_file(ff)

if __name__ == '__main__':
    main()