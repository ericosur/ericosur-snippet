#!/usr/bin/env python3
# coding: utf-8

'''
read variables from save file (in plain text json format)
'''

import sys
from loguru import logger
from rich import print as rprint

sys.path.insert(0, ".")
sys.path.insert(0, "..")
sys.path.insert(0, "../../python3/")
from myutil import read_jsonfile  # type: ignore[import]

logd = logger.debug
prt = rprint

class HackSaveFile():
    ''' read section __varialbes__ from save file'''
    FN = "save01.json"
    def __init__(self):
        self.data = read_jsonfile(HackSaveFile.FN)

    def action(self):
        ''' action '''
        pivot = self.data["variables"]
        for k,v in pivot.items():
            if isinstance(v, int):
                if 100 <= v <= 999:
                    prt(f"{k}: {v}")

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

if __name__ == '__main__':
    HackSaveFile.run()
