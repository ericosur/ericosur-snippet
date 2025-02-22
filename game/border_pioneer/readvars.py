#!/usr/bin/env python3
# coding: utf-8

'''
read variables from save file (in plain text json format)
'''

import json
import os
import sys
from rich import print as rprint
from pydantic import BaseModel
try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False

sys.path.insert(0, ".")
sys.path.insert(0, "..")
sys.path.insert(0, "../../python3/")
from myutil import read_jsonfile  # type: ignore[import]

logd = logger.debug if USE_LOGURU else print
prt = rprint

class HackVector(BaseModel):
    ''' vectors '''
    file: str
    gold: str
    food: str
    tool: str

class HackSaveFile():
    ''' read section __varialbes__ from save file'''
    CONF = "settings.json"

    def __init__(self):
        self.hv = HackVector(file="", gold="", food="", tool="")
        self.__init_vector()

    def __init_vector(self):
        conf = read_jsonfile(HackSaveFile.CONF)
        self.hv.file = conf['file']
        self.hv.gold = conf['gold']
        self.hv.food = conf['food']
        self.hv.tool = conf['tool']

    def show_values(self):
        ''' show the values I need '''
        p = self.data["variables"]
        p[self.hv.gold] += 5999
        p[self.hv.food] += 3999
        p[self.hv.tool] += 7999
        # prt(f'gold: {gold}')
        # prt(f'food: {food}')
        # prt(f'tool: {tool}')
        json.dumps(self.data, indent=2)
        # save self.data into json file
        with open("save03.save", 'wt', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def action(self):
        ''' action '''
        prt(self.hv.file)
        if os.path.exists(self.hv.file):
            self.data = read_jsonfile(self.hv.file)
        self.show_values()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

if __name__ == '__main__':
    HackSaveFile.run()
