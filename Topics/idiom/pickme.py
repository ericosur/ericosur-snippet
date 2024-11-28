#!/usr/bin/env python3
#coding: utf-8

'''
grep 4-character idioms from IDIOM_BOPOMOFO
'''

from random import randint
from idiom_list import IDIOM_BOPOMOFO as idioms
from numer4_idioms import FourCharIdioms as id4iom
from rich.console import Console
console = Console()
logd = console.log

class ChoiceIdiom():
    ''' pick some idioms from list '''
    def __init__(self):
        self.text0 = [] # not-4-char idioms here
        self.text4 = [] # 4-character idioms here
        logd(f'total idioms: {len(idioms)=}')
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
        logd(f"4-character idioms: {len4}")
        logd(f"other idioms: {len0}")
        assert len(idioms)==len4+len0

    @staticmethod
    def get_some_items_from_list(the_list: list, repeat: int=10) -> list:
        ''' from the_list get some items '''
        ans = []
        tmp = the_list.copy()
        logd(f'will return {repeat} idioms...')
        while len(ans) < repeat and len(tmp) > 1:
            rint = randint(0, len(tmp)-1)
            i = tmp.pop(rint)
            # only pick 4-han-character idioms
            ans.append(i)
        ans.sort()
        return ans

    def get_some_idioms(self) -> None:
        ''' get some idioms '''
        def inner(msg:str, the_list:list, n:int) -> None:
            ''' inner '''
            logd(msg)
            r = self.get_some_items_from_list(the_list, n)
            logd(r)

        inner('get some item from self.text4...', self.text4, 4)
        inner('get some item from self.text0...', self.text0, 3)
        inner('get some item from id4iom...', id4iom, 5)

    def show0(self):
        ''' show text0 '''
        logd(self.text0)

    def action(self):
        ''' action '''
        #self.show0()
        self.get_some_idioms()

def main():
    ''' main '''
    ChoiceIdiom.run()

if __name__ == "__main__":
    main()
