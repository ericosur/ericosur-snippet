#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
parse numeric variant characters from unihan database
"""
import json
import re

try:
    from rich import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print

class ParseVariant():
    """
    parse numeric variant characters from unihan database

    Unihan_NumericValues.txt
    Date: 2024-07-31 00:00:00 GMT [KL]
    Unicode Version 16.0.0
    """
    NUM_VAR_FILE = '../data/Unihan_NumericValues.txt'
    NUM_JSON_FILE = 'number_list.json'

    def __init__(self):
        self.num_list = []
        self.nomatch_lines = []
        self.by_value = {}
        self.keys = set()
        self.parse_unihan()

    def parse_unihan(self):
        """
        parse unihan database
        The format of the file is:
        codepoint   key   description
        U+20136	kVietnameseNumeric	5
        U+79ED	kPrimaryNumeric	1000000000 1000000000000
        """
        pattern = (
            r"^U\+([0-9A-F]{4,})\s+"     # U+79ED codepoint
            r"(k\w+Numeric)\s+"          # kPrimaryNumeric
            r"((([0-9]+)\s+)*([0-9]+))$"    # 1000000000
        )

        with open(self.NUM_VAR_FILE, 'rt', encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                line = line.strip()
                if not line:
                    continue
                m = re.match(pattern, line)
                if not m:
                    self.nomatch_lines.append(line)
                    #logd(f"NOT Matched: {line}")
                    continue
                #logd(line)
                cp = m.group(1)
                k = m.group(2)
                v = m.group(3)
                tmp = {"cp": cp, "k": k, "v": v}
                self.num_list.append(tmp)
        logd(f'not matched: {len(self.nomatch_lines)}')
        logd(f'num_list: {len(self.num_list)}')
        # collect all keys
        # kPrimaryNumeric, kAccountingNumeric, kOtherNumeric, ...
        for item in self.num_list:
            self.keys.add(item['k'])
        logd(f'keys: {len(self.keys)}')

    def dump(self):
        ''' dump '''
        logd('dump')
        if len(self.nomatch_lines) > 0:
            logd('not matched lines:')
            for line in self.nomatch_lines:
                logd(line)
        # dump as json
        fn = self.NUM_JSON_FILE
        with open(fn, 'wt', encoding='utf-8') as f:
            json.dump(self.num_list, f, ensure_ascii=False, indent=2)
        logd(f'dumped to: {fn}')

    def show_all_keys(self):
        ''' show all keys '''
        logd('show all keys =====>')
        logd(self.keys)

    def get_value_from_one_item(self, item):
        ''' get value from one item '''
        # item = self.num_list[0]
        # logd(item)

        cp = item['cp']
        k = item['k']
        v = item['v']
        the_c = chr(int(cp, 16))
        the_v = -1  # should be >= 0

        if ' ' in v:
            # split by space
            nums = v.split(' ')
            the_v = int(nums[1])
        else:
            the_v = int(v)

        ret = {
            'cp': cp,
            'k': k,
            'v': v,
            'the_c': the_c,
            'the_v': the_v
        }
        return ret

    def collect_values(self):
        ''' show primary keys '''
        logd('show collect_values =====>')

        for c in self.num_list:
            ret = self.get_value_from_one_item(c)
            if ret['the_v'] not in self.by_value:
                self.by_value[ret['the_v']] = []
            self.by_value[ret['the_v']].append(ret)

        for k in sorted(self.by_value.keys()):
            v = self.by_value[k]
            logd(f'{k}: {len(v)}')
            for item in v:
                if item["k"] in {"kVietnameseNumeric", "kZhuangNumeric"}:
                    # skip kVietnameseNumeric, kZhuangNumeric
                    continue
                if ord(item["the_c"]) > 0x20000:
                    # skip characters that are not in BMP
                    continue
                logd(f'  {item["cp"]} {item["k"]} {item["the_c"]}')

def main():
    ''' main '''
    parser = ParseVariant()
    parser.dump()   # to json
    parser.show_all_keys()  # show all keys
    parser.collect_values()  # show primary keys

if __name__ == '__main__':
    main()
