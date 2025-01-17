#!/usr/bin/env python3
# coding: utf-8

'''
filter list.txt and output to csv
'''

import re
import operator
import os
import sys
from rich import print as rprint
from loguru import logger

DEBUG = True

sys.path.insert(0, "./")
sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from myutil import do_nothing  # type: ignore[import]

prt = rprint
logd = logger.debug if DEBUG else do_nothing

class Solution():
    ''' solution '''
    def __init__(self, fn):
        self.ret = {}
        if os.path.isfile(fn):
            self.fn = fn
            logd(f'{self.fn=}')
        else:
            prt(f'file not found: {fn}')
            logd('exit...')
            sys.exit(1)

    def process(self):
        ''' process '''
        ret = {}
        with open(self.fn, "rt", encoding='utf-8') as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                exp_re = r'(pycache|\.vscode|\.mypy_cache)'
                exp_m = re.search(exp_re, ln)
                if exp_m:
                    #logd('found excluded string in ln...')
                    #logd(exp_m.group(1))
                    continue
                qq = r'(\S+)\s+(\d+)$'
                m = re.match(qq, ln)
                try:
                    if m:
                        #logger.debug(m)
                        k = m.group(1)
                        v = int(m.group(2))
                        ret[k] = v
                except ValueError:
                    pass
        self.ret = ret

    def output(self):
        ''' output '''
        # sed is list[tuple[str, int]]
        sed = sorted(self.ret.items(), key=operator.itemgetter(1), reverse=True)
        csv = "output.csv"
        with open(csv, "wt", encoding="utf-8") as fcsv:
            for i in sed:  # i: tuple(str, int)
                (p, v) = i
                if v > 0:
                    print(f'"{p}","{v}"', file=fcsv)
        logd(f"output to {csv}")

    @classmethod
    def run(cls, fn='out.txt'):
        ''' run '''
        logd("start...")
        obj = cls(fn)
        obj.process()
        obj.output()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Solution.run(fn=sys.argv[1])
    else:
        Solution.run()
