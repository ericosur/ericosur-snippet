#!/usr/bin/env python3
# coding: utf-8

'''
read from head2tail.py

you cannot play like this:
遠慮深謀
謀深慮遠

the used idiom cannot be used again

'''

import os
import sys
from random import choice, randint
from typing import Callable

try:
    from rich.console import Console
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

try:
    from _heads import idiom_dict as the_head_dict
    from _idioms import the_list as all_idioms
except ImportError:
    print('run __mklist.py__ first to generate necessary tables...')
    sys.exit(1)

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing '''
    return None

DEBUG = True
if DEBUG:
    logd: Callable
    if USE_RICH:
        console = Console()
        logd = console.log
    else:
        logd = print
else:
    logd = do_nothing
prt = rprint if USE_RICH else print

class Idiom():
    ''' play idiom chain '''
    MAX_REP = 10
    def __init__(self):
        self.local_idioms = all_idioms
        self.used = set()
        self.bads = self.__load_bads()
        self.loaded_len_bads = len(self.bads)
        logd(f'{len(the_head_dict)=}')
        self.play()

    def __load_bads(self):
        ''' load_bads '''
        fn = "_bads.txt"
        bads = set()
        if not os.path.exists(fn):
            return bads
        with open(fn, "rt", encoding="UTF-8") as fobj:
            for line in fobj:
                line = line.strip()
                if line:
                    bads.add(line)
        logd(f'load bads: {len(bads)}')
        return bads

    def play(self):
        ''' do_list '''
        logd("do_list")
        for i in range(Idiom.MAX_REP):
            self.play_one_round(i)
        if len(self.bads) > self.loaded_len_bads:
            logd(f'{len(self.bads)=} vs {self.loaded_len_bads=}')
            logd('length of bads increased, save it')
            self.save_bads()

    def play_one_round(self, no: str):
        ''' round '''
        prt(f'Round {no}:')
        # init for a new round
        the_dict = the_head_dict.copy()
        keys = the_dict.keys()
        self.used.clear()

        # pick the first key
        k = choice(list(keys))  #k = '一'
        #k = "對"
        #prt(f'The first key: {k}')
        cnt = 1
        rep = 0
        while True:
            #logd(f'{k=}: ')
            #logd({the_dict[k]})
            #logd(f'{k=}: {the_dict[k]}')

            idxs = the_dict[k]
            if len(idxs) == 0:
                prt('no more idioms to pick, exit...')
                break
            if rep > Idiom.MAX_REP:
                prt(f'too many repeats {rep}, break...')
                break

            p = idxs.pop(randint(0, len(idxs)-1))
            s = self.local_idioms[p]
            if cnt == 1 and s in self.bads:
                prt(f'[red]SHOULD NOT pick {s} for the frist one[/], try again')
                rep += 1
                continue
            if s in self.used:
                prt(f'picked {s} is used')
                rep += 1
                continue
            self.used.add(s)

            prt(f'{cnt}: {s}')
            k = s[-1]
            if k not in keys:
                if cnt == 1:
                    prt(f'[yellow] will not pick {s} as the first one again[/]')
                    self.bads.add(s)
                prt('    [bold yellow]no more...[/]')
                break
            cnt += 1

    def save_bads(self):
        ''' save_bads '''
        # save it as one item on line, not in python syntax
        fn = "_bads.txt"
        with open(fn, "wt", encoding="UTF-8") as fobj:
            for i in self.bads:
                print(f'{i}', file=fobj)
        logd(f'output to: {fn}')

if __name__ == "__main__":
    Idiom()
