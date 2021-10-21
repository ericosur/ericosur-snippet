#!/usr/bin/python3
# coding: utf-8

'''
read phone.txt, output two json file,
  - phone.json, like phone.txt, key is phonetic, values are han characters
  - bpmf.json, key is han character, values are all phonetics for this han char
'''

import json
import re
import os
import sys

# pylint: disable=invalid-name
class Solution():
    ''' solution '''
    def __init__(self, fn):
        self.fn = fn
        self.key = ''
        self.val = ''
        self.words = {}
        self.chars = {}

    def parse_one_line(self):
        ''' parse one line '''
        #re.findall(r'')
        arr = self.val.split(' ')
        self.words[self.key] = arr
        for cc in arr:
            if cc in self.chars:
                phs = self.chars[cc]
            else:
                phs = []
            phs.append(self.key)
            self.chars[cc] = phs

    def check_file(self):
        ''' check file
        key=,-./0123456789;abcdefghijklmnopqrstuvwxyz
        '''
        cnt = 0
        with open(self.fn, "rt", encoding='utf8') as f:
            for ln in f.readlines():
                m = re.search(r'^([,-.;/0-9a-z]{,4}) (.+)$', ln.strip())
                if m:
                    self.key = m.group(1)
                    self.val = m.group(2).strip()
                    self.parse_one_line()
                    cnt += 1
        print('cnt:', cnt)

    def show(self):
        ''' show '''
        cnt = 0
        for k,v in self.words.items():
            cnt += 1
            if cnt > 10:
                break
            print(f"{k}: {v}")

    def dump(self):
        ''' dump '''
        with open('phone.json', 'wt', encoding='utf8') as of:
            of.write(json.dumps(self.words, indent=2, sort_keys=True))
        print('output to phone.json, len:', len(self.words))
        with open('bpmf.json', 'wt', encoding='utf8') as of:
            of.write(json.dumps(self.chars, indent=2, sort_keys=True))
        print('output bpmf.json, len:', len(self.chars))

    def run(self):
        ''' run '''
        self.check_file()
        self.dump()

def main():
    ''' main '''
    fn = 'phone.txt'
    if not os.path.exists(fn):
        print('[ERROR] file not found:', fn)
        sys.exit(1)

    sol = Solution(fn)
    sol.run()


if __name__ == '__main__':
    main()
