#!/usr/bin/python3.6
# coding: utf-8

'''
read en.xml and output to csv
'''

import csv
from datetime import date
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

# XLSWRITER_OK = False
# try:
#     import xlsxwriter
#     XLSWRITER_OK = True
# except ImportError:
#     print('cannot import module xlsxwriter')
#     sys.exit(1)


class Solution():
    ''' solution to read en.xml and output as csv-like data '''
    def __init__(self):
        self.content = None
        self.emoji = dict()

    @staticmethod
    def to_codepoint(cc: str):
        '''
        cc [in] unicode char
        calling: to_from_u16(chr(0x0001f3c8))
        '''
        ue = cc.encode('unicode-escape').decode('utf-8')
        return ue

    @staticmethod
    def read_file(fn):
        ''' read specified file and return file content '''
        content = None
        with open(fn, 'rt') as fh:
            content = fh.read()
        return content

    def make_soup(self):
        ''' make soup from content '''
        soup = BeautifulSoup(self.content, 'lxml')
        t = soup.find('annotations')
        anns = t.find_all('annotation')
        for i in anns:
            key = i['cp']
            if key in self.emoji:
                if len(i.text) < len(self.emoji[key][1]):
                    self.emoji[key].insert(1, i.text)
                else:
                    self.emoji[key].append(i.text)
            else:
                self.emoji[key] = list()
                self.emoji[key].append(Solution.to_codepoint(key))
                self.emoji[key].append(i.text)

    @staticmethod
    def value_to_string(v: list):
        ''' value to string '''
        s = str()
        for i in v:
            s += '"' + i + '"' + ','
        # remove the extra ,
        return s[:-1]


    def output_data(self):
        ''' output data '''
        print('len: {}'.format(len(self.emoji)))
        outfn = 'output.csv'
        with open(outfn, 'wt') as f:
            for _, (k, v) in enumerate(self.emoji.items()):
                vals = Solution.value_to_string(v)
                print(f'\"{k}\",{vals}', file=f)
        print('output to {}'.format(outfn))


    def action(self):
        ''' action '''
        for fn in ['en-basic.xml', 'en-derived.xml']:
            print('fn: {}'.format(fn))
            self.content = self.read_file(fn)
            # parsing xml and store into list()
            self.make_soup()
            self.output_data()


def get_datetag():
    ''' string in UMMDD '''
    today = date.today()
    s = 'U{:02d}{:02d}'.format(today.month, today.day)
    return s

def output_csv(data):
    ''' output data as csv format in UMMDD.csv '''
    fn = get_datetag() + '.csv'
    print('[INFO] output to:', fn)
    with open(fn, 'wt') as csvfile:
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
