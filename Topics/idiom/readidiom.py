#!/usr/bin/env python3
# coding: utf-8

'''
read from datasheet.txt
'''

import re
from rich.console import Console
console = Console()
logd = console.log

class Idiom():
    ''' idiom '''
    #DATA = "data-utf16le.txt"
    DATA = "data-u8.txt"
    #ENCODING = "UTF-16LE"
    ENCODING = "UTF-8"
    def __init__(self):
        self.idioms = []
        self.__readidiom()

    def __readidiom(self):
        ''' read idioms '''
        cnt = 0
        logd(f'open: {self.DATA}')
        with open(self.DATA, "rt", encoding=self.ENCODING) as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                if len(ln) < 1:
                    logd(f"wtf: {ln}")
                m = re.match(r'^(\xef\xbb\xbf)?\d+\s(.+)$', ln)
                if m:
                    self.idioms.append(m[2])
                else:
                    logd(f'not match: {ln}')
                cnt += 1
        logd(cnt)

    def dump(self):
        ''' dump '''
        #logd(self.idioms)
        logd(f'size:{len(self.idioms)}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.dump()

def main():
    ''' main '''
    Idiom.run()

if __name__ == "__main__":
    main()
