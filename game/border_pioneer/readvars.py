#!/usr/bin/env python3
# coding: utf-8

'''
read variables from save file (in plain text json format)
'''

import json
import os
import shutil
import sys
from rich import print as rprint
from pydantic import BaseModel
try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False
try:
    from icecream import ic
    USE_ICECREAM = True
except ImportError:
    USE_ICECREAM = False

sys.path.insert(0, ".")
sys.path.insert(0, "..")
sys.path.insert(0, "../../python3/")
from myutil import read_jsonfile  # type: ignore[import]

logd = logger.debug if USE_LOGURU else print
prt = rprint

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

if not USE_ICECREAM:
    ic = do_nothing

class FileVector(BaseModel):
    ''' about dirs/files'''
    savedir: str
    file: str
    backup: str
class HackVector(BaseModel):
    ''' vectors '''
    gold: str
    food: str
    tool: str

class HackSaveFile():
    ''' read section __varialbes__ from save file'''
    CONF = "settings.json"

    def __init__(self):
        self.fv = FileVector(savedir="", file="", backup="")
        self.hv = HackVector(gold="", food="", tool="")
        self.__init_vectors()

    def __init_vectors(self):
        conf = read_jsonfile(HackSaveFile.CONF)
        # FileVector
        self.fv.savedir = conf['savedir']
        self.fv.file = conf['file']
        self.fv.backup = conf['backup']
        # HackVector
        self.hv.gold = conf['gold']
        self.hv.food = conf['food']
        self.hv.tool = conf['tool']

    def hack_values(self):
        ''' show the values I need '''
        p = self.data["variables"]
        p[self.hv.gold] += 6999
        ic(p[self.hv.gold])
        p[self.hv.food] += 5999
        ic(p[self.hv.food])
        p[self.hv.tool] += 7999
        ic(p[self.hv.tool])

        #json.dumps(self.data, indent=2)
        # save self.data into json file
        fn = self.fv.file
        with open(fn, 'wt', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        ic(fn)

    def action(self):
        ''' action '''
        srcdir = self.fv.savedir
        if not os.path.exists(srcdir):
            ic(f'not found: {srcdir}')
            return
        target_file = os.path.join(srcdir, self.fv.file)
        if not os.path.exists(target_file):
            ic(f'not found: {target_file}')
            return
        # backup
        shutil.copy(target_file, os.path.join('.', self.fv.backup))
        prt(f'target_file: {target_file}')
        self.data = read_jsonfile(target_file)
        #prt(self.data)  # it's too long, DO NOT print it
        self.hack_values()
        shutil.copy(self.fv.file, target_file)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

if __name__ == '__main__':
    HackSaveFile.run()
