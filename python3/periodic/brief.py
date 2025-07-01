#!/usr/bin/env python3
# coding: utf-8

'''
read json and list
'''

import json
import os
import sys
try:
    from rich import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print
try:
    sys.path.insert(0, "..")
    from myutil import read_jsonfile, isfile
except ImportError:
    print("Error: myutil module not found")
    sys.exit(1)

class ShowElement():
    ''' ShowElement class '''
    DATAFILE = 'periodic-table-lookup.json'
    zsymbolfile = "zsymbol.json"
    max_num = 118  # max atomic number

    def __init__(self) -> None:
        self.data = self.__load_data()
        if not self.data:
            print(f"Error: {ShowElement.DATAFILE} not found or empty")
            sys.exit(1)

    def read_json(self, filename: str) -> None:
        ''' read json file '''
        data = read_jsonfile(ShowElement.DATAFILE)
        logd(f"read_json: {filename}")
        logd(f'data len: {len(data)}')

    def __load_data(self) -> None:
        ''' load data from json file '''
        the_dict = {}
        if isfile(ShowElement.zsymbolfile):
            the_dict = read_jsonfile(ShowElement.zsymbolfile)
            return the_dict
        if not os.path.exists(ShowElement.DATAFILE):
            print(f"Error: {ShowElement.DATAFILE} not found")
            return the_dict

        d = read_jsonfile(ShowElement.DATAFILE)
        for n in d['order']:
            t = d[n]
            num = t['number']
            if isinstance(num, int):
                num = str(num)
            sym = t['symbol']
            if num not in the_dict:
                the_dict[num] = sym
            if sym not in the_dict:
                the_dict[sym] = num
        # save to zsymbol.json
        self.__save_zsymbol(the_dict)
        return the_dict

    def __save_zsymbol(self, the_dict: dict) -> None:
        ''' save zsymbol to json file '''
        if isfile(ShowElement.zsymbolfile):
            # already exists, do not overwrite
            return

        with open(ShowElement.zsymbolfile, 'wt', encoding='utf-8') as f:
            json.dump(the_dict, f, indent=4, sort_keys=True)

    def __concat_keys(self, keys: list) -> str:
        ''' concatenate keys with '/' '''
        return '/'.join(str(k) for k in keys)

    def is_num(self, i: str) -> bool:
        ''' check if i is a number '''
        try:
            int(i)
            return True
        except ValueError:
            return False

    def query_list(self, a_list: list) -> None:
        ''' test '''
        # 16/92/53/34/53
        # 99/25/92/19/53
        keys = []
        vals = []
        for i in a_list:
            if self.is_num(i):
                if i > ShowElement.max_num:
                    print(f"Error: atomic number {i} exceeds max number {ShowElement.max_num}")
                    continue
                i = str(i)
            r = self.data.get(i, None)
            if r is None:
                logd(f"Error: {i} not found in data")
                continue
            keys.append(i)
            vals.append(r)

        key_str = self.__concat_keys(keys)
        val_str = ' '.join(vals)
        print(f"{key_str}, {val_str}")


if __name__ == '__main__':
    print(f'Do not run {sys.argv[0]} directly, use query-element.py')
    sys.exit(1)
