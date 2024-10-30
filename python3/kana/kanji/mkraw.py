#!/usr/bin/python3
#coding: utf-8

'''
read raw.txt and output format:
    - yaml
    - json
    - one char one line
'''

FN = "raw.txt"

import re
import json
from wtf import logd

class Solution():
    ''' handle raw.txt '''
    def __init__(self):
        self.a_dict = {}
        self.a_list = []

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

    def line2list(self, ln) -> list:
        ''' split characters into a list '''
        chars = []
        m = re.findall(r'(.)\s*', ln)
        for c in m:
            chars.append(c)
        return chars

    def process_raw(self):
        ''' process raw file into yaml '''
        logd(f'read from: {FN}')
        with open(FN, "rt", encoding="UTF-8") as fobj:
            the_row = "null"
            cnt_row = 0
            for ln in fobj.readlines():
                ln = ln.strip()
                if ln == "":    # skip empty line
                    continue
                if len(ln) == 1:    # skip the line only one char (usu. kanata)
                    the_row = ln[0]
                    #logd(f'{cnt_row}: {the_row}')
                    self.a_dict[the_row] = []
                    cnt_row += 1
                    continue
                ret = self.line2list(ln)
                self.a_dict[the_row] = ret
                self.a_list.extend(ret)

    def report(self):
        ''' some reoprt about internal data structure '''
        logd(f'the size of {len(self.a_list)=}')
        logd(f'the size of {len(self.a_dict)=}')
        total_in_k = 0
        cnt = 0
        for _,v in self.a_dict.items():
            #logd(f'{cnt}: {k}')
            total_in_k += len(v)
            cnt += 1
        logd(f'the total chars: {total_in_k}')

    def output_as_yaml(self):
        ''' yaml '''
        fn = "kanji.yaml"
        with open(fn, "wt", encoding="UTF-8") as the_file:
            for k,v in self.a_dict.items():
                if len(v) < 1: # special case
                    logd(f'has no data member: {k}')
                    print(f'{k}: []', file=the_file)
                    continue
                print(f'{k}: |', file=the_file)
                for i in v:
                    print(f"  {i}", file=the_file)
        logd(f'output to {fn}')

    def output_as_json(self):
        ''' json '''
        fn = "kanji.json"
        with open(fn, "wt", encoding="UTF-8") as the_file:
            print(json.dumps(self.a_dict, indent=2, sort_keys=False), file=the_file)
        logd(f'json output to {fn}')

    def output_one_char_each_line(self):
        ''' one char each line '''
        fn = "kanji_one_char_one_line.txt"
        with open(fn, "wt", encoding="UTF-8") as the_file:
            for c in self.a_list:
                print(c, file=the_file)
        logd(f'output_one_char_each_line: to file: {fn}')

    def action(self):
        ''' action '''
        logd("hello world")
        self.process_raw()
        self.report()
        self.output_as_yaml()
        self.output_as_json()
        self.output_one_char_each_line()

def main():
    ''' main '''
    Solution.run()

if __name__ == "__main__":
    main()
