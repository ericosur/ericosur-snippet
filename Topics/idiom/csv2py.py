#!/usr/bin/python
# coding:utf-8

'''
the script parse the csv file and output the python dict/list
'''

import sys
import os
import re
from rich.console import Console
console = Console()
logd = console.log

class Csv2py():
    ''' csv to py '''
    FN = "idiom_bopo2.csv"
    def __init__(self):
        self.idioms = []
        self.__readtxt()

    def __readtxt(self):
        ''' read txt
        '''
        logd("readtxt...")
        with open(self.FN, "rt", encoding='UTF-8') as fobj:
            cnt, cnt1, cnt2 = 0, 0, 0
            for ln in fobj.readlines():
                ln = ln.strip()
                #logd(ln)
                cnt += 1
                m = re.match(r'^([^,]+),(.+)([　 ]+\(變\).+)$', ln)
                if m:
                    cnt1 += 1
                    self.idioms.append((m[1], m[2]))
                    continue
                m = re.match(r'^([^,]+),([^變]+)$', ln)
                if m:
                    cnt2 += 1
                    self.idioms.append((m[1], m[2]))
                    continue
                logd(f'not match:{cnt} {ln}')
        logd(f'{cnt=}, {cnt1=}, {cnt2=}')
        assert cnt==cnt1+cnt2
        logd(self.idioms)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()


def main():
    ''' main '''
    Csv2py.run()

if __name__ == "__main__":
    main()
