#!/usr/bin/python
#coding: utf-8

'''
from idiom list, and 4 character idioms,
pick idioms which has
零○一二三四五六七八九十拾百佰千仟萬億兆京垓
'''

#from random import randint
import re
from loguru import logger
logd = logger.debug
logi = logger.info
from idiom_list import IDIOM_BOPOMOFO as idioms

class GrepNumberInIdioms():
    ''' pick some idioms from list '''
    def __init__(self):
        self.numers = []
        self.ans = []

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

    def do_grep(self):
        ''' do grep '''
        pattern = r'.*[零○一二三四五六七八九十拾百佰千仟萬億兆京垓]+.*'
        for i in idioms:
            ph = i[0]
            m = re.match(pattern, ph)
            if m:
                self.numers.append(ph)
                if len(ph)==4:
                    self.ans.append(ph)
        self.ans.sort()

    def action(self):
        ''' action '''
        logd("action...")
        self.do_grep()
        #print(self.ans)
        print(f'{len(idioms)=}')
        print(f'{len(self.numers)=}')
        print(f'{len(self.ans)=}')

def main():
    ''' main '''
    GrepNumberInIdioms.run()

if __name__ == "__main__":
    main()
