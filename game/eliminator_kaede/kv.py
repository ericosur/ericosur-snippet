#!/usr/bin/env python3
# coding: utf-8

import os
import sys
sys.path.insert(0, "./")
sys.path.insert(0, "../")
sys.path.insert(0, "../../python3/")

from myutil import read_jsonfile  # type: ignore[import]

class Solution():
    ''' solution '''
    FN = "the_dict.json"
    def __init__(self):
        self.the_dict = {}
        self.load_savefile()

    def load_savefile(self):
        ''' load save file into dict '''
        data = read_jsonfile(Solution.FN)
        if data is None:
            print('data is None...')
            return
        ks = data.get("keys", [])
        vs = data.get("values", [])
        self.the_dict = dict(zip(ks, vs))
        print("for eyes only...")
        for k in sorted(self.the_dict.keys()):
            v = self.the_dict[k]
            print(f'{k}: {v}')

    @classmethod
    def run(cls):
        ''' run '''
        cls()

if __name__ == "__main__":
    Solution.run()
