#!/usr/bin/env python3
# coding: utf-8

'''
read parts.txt and save it to csv
'''

#import os
import re
#import sys
from time import time

MODNAME = "parts2csv.py"
VERSION = "2023.10.30"

def show_duration(duration):
    ''' show duration '''
    print(f'{MODNAME}: duration: {duration:.3e} sec')

class Solution():
    ''' test date is a prime '''

    IFN = "parts.txt"
    OFN = "parts-output.csv"

    def __init__(self):
        self.p = []

    def read_txt_out_csv(self, itxtfn, ocsvfn):
        ''' process file '''
        cnt = 0
        print(f'read from {itxtfn}...')
        with open(itxtfn, "rt", encoding='UTF-8') as fin, open(ocsvfn,
            'wt', encoding='UTF-8') as fout:
            for ln in fin.readlines():
                ln = ln.strip()
                if len(ln) == 0:
                    continue
                if ln.find("#") >= 0:
                    continue
                ln = ln.replace(' ', '')
                cnt += 1
                print(f'{cnt},{ln}', file=fout)

    def input_txtfile_re(self, itxtfn):
        ''' process file '''
        cnt = 0
        r = re.compile(r'\b\d+\b')
        print(f'read from {itxtfn}...')
        with open(itxtfn, "rt", encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                ln.strip()
                cnt += 1
                m = r.findall(ln)
                if m:
                    if cnt < 3:
                        print(m)
                    else:
                        print(f'{cnt}\r', end='')

                    t = [ int(x) for x in m ]
                    self.p.extend(t)

                    # dry run
                    print('[INFO] Dry run...')
                    if cnt > 10:
                        break


    def action(self):
        ''' action '''
        start = time()
        self.read_txt_out_csv(self.IFN, self.OFN)
        duration = time() - start
        show_duration(duration)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
