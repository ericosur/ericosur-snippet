#!/usr/bin/python3
# coding: utf-8

'''
read from wordlist.txt
'''

import os
import re
import sys
from rich.console import Console
from morses import MORSES

console = Console()
logd = console.log

class Words():
    ''' words '''
    FN = "wordlist.txt"
    MFN = "morse.txt"

    def __init__(self):
        self.words = []
        self.chars = {}
        #self.morse = {}
        self.__readtxt()
        self.__initchars()
        #self.__readmorse()

    def __initchars(self):
        ''' init self.chars '''
        seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        assert len(seq) == 26
        logd("__initchars")
        for c in list(seq):
            self.chars[c] = 0

    def __readtxt(self):
        ''' read txt '''
        with open(self.FN, "rt", encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                ln = ln.strip().upper()
                if len(ln) < 1:
                    continue
                self.words.append(ln)
        # sort
        self.words.sort()

    # def __readmorse(self):
    #     ''' load morse '''
    #     with open(self.MFN, "rt", encoding="utf-8") as fobj:
    #         for ln in fobj.readlines():
    #             ln = ln.strip()
    #             if ln == "":
    #                 continue
    #             m = re.match(r'^([A-Z]) ([\.-]+)$', ln)
    #             if m:
    #                 #logd(f'{ln}\n{m[1]}:  {m[2]}')
    #                 self.morse[m[1]] = m[2]
    #             else:
    #                 logd(f'not match: {ln}')

    def dump(self) -> None:
        ''' dump '''
        #logd("dump...")
        # 2,3,5,7,11
        V = 307
        if V % 2 == 0:
            logd("the self.words =====>")
            for i in self.words:
                logd(i)
        if V % 3 == 0:
            logd("the self.chars =====>")
            for k,v in self.chars.items():
                if v:
                    logd(k,v)
        if V % 5 == 0:
            #logd("the morse list...")
            logd(MORSES)

    def count_words(self):
        ''' count words'''
        for w in self.words:
            for c in list(w):
                self.chars[c] += 1

    def word_to_morse(self, w: str) -> str:
        ''' SMS: .../--/... '''
        ms = []
        for c in list(w):
            ms.append(MORSES[c])
        msg = "/".join(ms)
        # https://rich.readthedocs.io/en/stable/appendix/colors.html
        logd(f'{w:6s}: [chartreuse4]{msg}')
        return msg

    def traverse_words(self):
        ''' traverse all words '''
        for w in self.words:
            self.word_to_morse(w)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.count_words()
        obj.dump()
        obj.traverse_words()

def main():
    ''' main '''
    Words.run()

if __name__ == "__main__":
    main()
