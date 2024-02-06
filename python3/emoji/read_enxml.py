#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
read en.xml and output to csv
'''

import csv
import os
import sys
from datetime import date

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_textfile


class Solution():
    ''' solution to read en.xml and output as csv-like data '''

    FILES = ['en-basic.xml', 'en-derived.xml',
            'zh-basic.xml', 'zh-derived.xml']

    def __init__(self):
        self.content = None
        self.emoji = {}

    @staticmethod
    def to_codepoint(cc: str):
        '''
        cc [in] unicode char
        calling: to_from_u16(chr(0x0001f3c8))
        '''
        ue = cc.encode('unicode-escape').decode('utf-8')
        return ue

    def make_soup(self) -> None:
        ''' parse xml from content, store into self.emoji '''
        soup = BeautifulSoup(self.content, features='xml')
        t = soup.find('annotations')
        anns = t.find_all('annotation')
        for i in anns:
            key = i['cp']
            if key in self.emoji:
                if "type" in i.attrs:
                    self.emoji[key].insert(1, i.text)
                else:
                    self.emoji[key].append(i.text)
            else:
                self.emoji[key] = []
                self.emoji[key].append(Solution.to_codepoint(key))
                self.emoji[key].append(i.text)

    @staticmethod
    def value_to_string(v: list) -> list:
        ''' value to string '''
        s = str()
        for i in v:
            s += '"' + i + '"' + ','
        # remove the extra ,
        return s[:-1]


    def output_data(self, outfn) -> None:
        ''' output data '''
        #print(f'len: {len(self.emoji)}')
        with open(outfn, 'wt', encoding='utf8') as f:
            for _, (k, v) in enumerate(self.emoji.items()):
                vals = Solution.value_to_string(v)
                print(f'\"{k}\",{vals}', file=f)
        print(f'output to {outfn}')


    def action(self) -> None:
        ''' action '''
        for fn in Solution.FILES:
            print(f'read from: {fn}')
            self.content = read_textfile(fn)
            # parsing xml and store into list()
            self.make_soup()
            #print(f'curr len: {len(self.emoji)}')
        self.output_data('wtf.csv')


def get_datetag() -> str:
    ''' string in UMMDD '''
    today = date.today()
    s = f'U{today.month:02d}{today.day:02d}'
    return s

def output_csv(data) -> None:
    ''' output data as csv format in UMMDD.csv '''
    fn = get_datetag() + '.csv'
    print('[INFO] output to:', fn)
    with open(fn, 'wt', encoding='utf8') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        for dd in data:
            sw.writerow(dd)


def main():
    ''' main '''
    s = Solution()
    s.action()

if __name__ == '__main__':
    main()
