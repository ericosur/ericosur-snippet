#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
read en.xml and output to csv
'''

import re
import sys
from datetime import datetime
try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

sys.path.insert(0, "..")
from myutil import read_textfile

# header for generated python file
timestamp = datetime.today()
HEADER='''
# coding: utf-8

"""
emoji table in python dict, generated by parse_enxml.py
"""

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
'''

START='''
EMOJI = {'''

TAIL='''
}

if __name__ == "__main__":
    print("Only provides a dict: EMOJI")
    print("DO NOT run this script...")'''

class Solution():
    ''' solution to read en.xml and output as csv-like data '''
    def __init__(self):
        self.content = None

    @staticmethod
    def to_codepoint(cc: str):
        '''
        cc [in] unicode char
        calling: to_from_u16(chr(0x0001f3c8))
        '''
        ue = cc.encode('unicode-escape').decode('utf-8')
        return ue

    def need_filter(self, k):
        ''' check if this key could be filtered out '''
        black_set = {"backslash", "反斜線", "\\"}
        if k in black_set:
            return True
        if "skin_tone" in k:
            return True
        return False

    def make_soup(self, the_dict: dict) -> None:
        ''' parse xml from content, store into a dict '''
        soup = BeautifulSoup(self.content, features='xml')
        t = soup.find('annotations')
        anns = t.find_all('annotation')
        for i in anns:
            if 'type' in i.attrs:
                value = i['cp']
                key = self.normalize(i.text)
                if self.need_filter(key):
                    #print(f'filtered: {key}')
                    continue
                if key in the_dict:
                    #print(f"Warn: duplicated key: {key}")
                    continue
                the_dict[key] = value


    def make_sweetsoup(self, the_dict: dict) -> None:
        ''' parse xml from content, store into self.cp '''
        soup = BeautifulSoup(self.content, features='xml')
        t = soup.find('annotations')
        anns = t.find_all('annotation')
        for i in anns:
            if 'type' in i.attrs:
                key = i['cp']
                if self.need_filter(key):
                    continue
                v = self.normalize(i.text)
                #print(v)
                if key in the_dict:
                    value = f'{the_dict[key]},{v}'
                    #print(f'{value=}')
                    the_dict[key] = value
                else:
                    the_dict[key] = v

        #print(the_dict)

    @staticmethod
    def normalize(s: str) -> str:
        ''' substitue space to underscore, and lower case '''
        tmp = s.lower()
        tmp = re.sub(r'[:!+\']', '', tmp)
        tmp = re.sub(' ', '_', tmp)
        return tmp

    @staticmethod
    def value_to_string(v: list) -> list:
        ''' value to string '''
        s = str()
        for i in v:
            s += '"' + i + '"' + ','
        # remove the extra ,
        return s[:-1]

    # ref: https://github.com/carpedm20/emoji/tree/master/utils
    def output_data(self, ofn, the_dict) -> None:
        ''' output data '''
        #print(f'len: {len(self.emoji)}')
        with open(ofn, 'wt', encoding='utf8') as f:
            print(HEADER, file=f)
            print(f'# timestamp: {timestamp}', file=f)
            print(START, file=f)
            for _, (k, v) in enumerate(sorted(the_dict.items())):
                print(f'    \"{k}\": \"{v}\",', file=f)
            print(TAIL, file=f)
        print(f'output to {ofn}')

    def gen_cp(self):
        ''' generate python file that the key is the cp char/string '''
        files = ['en-basic.xml', 'en-derived.xml', 'zh-basic.xml', 'zh-derived.xml']
        ret_dict = {}
        for fn in files:
            self.content = read_textfile(fn)
            self.make_sweetsoup(ret_dict)
        self.output_data('cp_emoji.py', ret_dict)


    def gen_emoji(self):
        ''' generate _emoji.py '''
        # input en.xml comes with CLDR data files
        ret_dict = {}
        for fn in ['en-basic.xml', 'en-derived.xml']:
            print(f'fn: {fn}')
            self.content = read_textfile(fn)
            # parsing xml and store into list()
            self.make_soup(ret_dict)
            # output the results into emoji table in python
            self.output_data('en_emoji.py', ret_dict)

    def action(self) -> None:
        ''' action '''
        self.gen_emoji()
        self.gen_cp()

def main():
    ''' main '''
    obj = Solution()
    obj.action()

if __name__ == '__main__':
    main()
