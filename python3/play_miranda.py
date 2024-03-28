#!/usr/bin/env python3
# coding: utf-8

'''
pick one of miranda's pre-recorded voices to play
'''

import os
import random
import re
import sys
import time
from typing import List

from myutil import get_home, read_jsonfile, isfile


# pylint: disable=invalid-name
class Miranda():
    ''' miranda tts '''
    DEBUG = False
    CONF = 'miranda.json'
    cli = '/usr/bin/play'

    def __init__(self):
        self.fn = 'miranda1.bin'
        self.zh = []
        self.en = []
        self.path = None

        self._load_config()
        self.collect_phrash()

    def _load_config(self):
        ''' load miranda.json '''
        conf = os.path.join(get_home(), 'Private', self.CONF)
        data = None
        if isfile(conf):
            data = read_jsonfile(conf)
        else:
            print(f'[ERROR] cannot load config file: {conf}')
            sys.exit(1)
        if data:
            self.path = data["path"]
            print(f'[INFO] path of miranda: {self.path}')

    @staticmethod
    def get_immediate_subdirectories(a_dir: str) -> List:
        '''
        refer from:
        https://stackoverflow.com/questions/800197/how-to-get-all-of-the-immediate-subdirectories-in-python
        '''
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]

    def get_en(self):
        ''' return en phrases '''
        return self.en

    def get_zh(self):
        ''' return zh phrases '''
        return self.zh

    def get_fn(self, p):
        ''' compose file path '''
        r = os.path.join(self.path, p, self.fn)
        if self.DEBUG:
            print(f'get_fn: {r}')
        return r

    def collect_phrash(self):
        ''' collect en/zh phrases from directory names '''
        ret = Miranda.get_immediate_subdirectories(self.path)
        for d in ret:
            m = re.match(r'^[a-zA-Z_0-9]+$', d)
            if m:
                self.en.append(m.group(0))
            else:
                self.zh.append(d)
        print('size of en phrases:', len(self.en))
        print('size of zh phrases:', len(self.zh))
        if not self.zh:
            raise ValueError('does not collect any zh phrases...')
        self.en.sort()

    def check_cli(self):
        ''' check the cli is available '''
        if isfile(self.cli):
            return True
        raise FileNotFoundError(f'not found: {self.cli}')

    def play_phrase(self, phrase: str) -> None:
        ''' specify phrase to play tts '''
        if not phrase in self.zh and not phrase in self.en:
            print(f'phrase [{phrase}] not found...')
            return

        self.check_cli()

        tts_fn = self.get_fn(phrase)
        if isfile(tts_fn):
            # for oa18.local
            # oa18_cmd = f'{self.cli} -t raw -b 16 -r 48000 -e signed -c 1 {tts_fn}'

            # for kitty.local
            cmd = f'{self.cli} -t raw -b 16 -r 24000 -e signed -c 2 {tts_fn}'

            os.system(cmd)
            time.sleep(.75)
        else:
            print(f'file not found: {tts_fn}')

def main():
    ''' main '''
    mm = Miranda()

    #items = mm.get_en()
    items = mm.get_zh()
    MAX_COUNT = 1

    for _ in range(MAX_COUNT):
        r = random.choice(items)
        print(f'request playing {r} ...')
        mm.play_phrase(r)

if __name__ == '__main__':
    main()
