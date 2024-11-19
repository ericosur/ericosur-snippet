#!/usr/bin/python
#coding: utf-8

'''
choice
'''

from random import randint
from idiom_list import IDIOM_BOPOMOFO as idioms
from rich.console import Console
console = Console()
logd = console.log

class ChoiceIdiom():
    ''' pick some idioms from list '''
    def __init__(self):
        self.text0 = []
        self.text4 = []
        logd(f'{len(idioms)=}')
        self.__seperate4()

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

    def __seperate4(self):
        ''' not 4c idioms '''
        for v in idioms:
            if len(v[0])==4:
                self.text4.append(v)
            else:
                self.text0.append(v)
        self.text0.sort()
        self.text4.sort()
        len4 = len(self.text4)
        len0 = len(self.text0)
        logd(f"{len4=}")
        logd(f"{len0=}")
        assert len(idioms)==len4+len0

    def get_some_4c(self):
        ''' get some 4 character-idiom '''
        repeat = 10
        ans = []
        tmp = self.text4.copy()
        while len(ans) < repeat and len(tmp) > 1:
            rint = randint(0, len(tmp)-1)
            ret = tmp.pop(rint)
            # only pick 4-han-character idioms
            if len(ret[0]) == 4:
                ans.append(ret)
            else:
                logd(f'not match: {ret}')
        ans.sort()
        logd(ans)

    def show0(self):
        ''' show text0 '''
        logd(self.text0)

    def action(self):
        ''' action '''
        logd("action...")
        self.show0()
        self.get_some_4c()

def main():
    ''' main '''
    ChoiceIdiom.run()

if __name__ == "__main__":
    main()
