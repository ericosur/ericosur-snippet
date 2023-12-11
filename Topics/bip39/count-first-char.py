#!/usr/bin/env python3
#coding: utf-8

'''
template script
'''

import array_util


class Solution():
    ''' class solution '''

    wordlist = 'bip-39-english.txt'
    arraydat = 'pickle.dat'

    def __init__(self):
        self.dwords = {}
        self.isloaded = False
        self.diskarray = None
        self._make_a2z()
        self._load()

    def _make_a2z(self):
        ''' make a list with a to z '''
        CNT = 26
        for i in range(CNT):
            c = ord('a') + i
            self.dwords[chr(c)] = 0

    def _load(self):
        ''' load if exist '''
        self.diskarray = array_util.loadarray(self.arraydat)
        if self.diskarray is None:
            self.diskarray = []
        else:
            self.isloaded = True
            print(len(self.diskarray))

    def _save(self):
        ''' save if not exist '''
        if not self.isloaded:
            array_util.savearray(self.arraydat, self.diskarray)

    def categrorize_words(self, wd):
        ''' count wd into self.dwords '''
        self.dwords[wd[0]] += 1

    def show(self):
        ''' show '''
        tmp = 0
        for k, v in self.dwords.items():
            tmp += v
            print(f'{k}: {v}')
        print(f'{tmp=}')

    def process_words(self):
        ''' process words '''
        with open(self.wordlist, 'rt', encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                if not self.isloaded:
                    self.diskarray.append(ln)
                self.categrorize_words(ln)

    def action(self):
        ''' action '''
        self.process_words()
        self.show()
        self._save()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
