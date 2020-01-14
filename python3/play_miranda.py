#!/usr/bin/env python3
# coding: utf-8

'''
pick one of miranda's pre-recorded voices to play
'''

import os
import random
import re
import time

# pylint: disable=invalid-name
class Miranda():
    ''' miranda tts '''
    def __init__(self):
        self.fn = 'miranda1.bin'
        self.zh = []
        self.en = []

    @staticmethod
    def get_immediate_subdirectories(a_dir):
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
        return p + '/' + self.fn

    def collect_phrash(self):
        ''' collect en/zh phrases from directory names '''
        ret = Miranda.get_immediate_subdirectories('.')
        for d in ret:
            m = re.match(r'^[a-zA-Z_0-9]+$', d)
            if m:
                self.en.append(m.group(0))
            else:
                self.zh.append(d)
        print('len(en):', len(self.en))
        print('len(zh):', len(self.zh))
        if not self.zh:
            raise ValueError('does not collect any zh phrases...')
        self.en.sort()


def main():
    ''' main '''
    mm = Miranda()
    mm.collect_phrash()
    #items = mm.get_en()
    items = mm.get_zh()
    MAX_COUNT = 1
    cnt = 0
    while cnt < MAX_COUNT:
        r = random.choice(items)
        print('playing {} ...'.format(r))
        cnt += 1
        # for oa18.local
        #cmd = 'play -t raw -b 16 -r 48000 -e signed -c 1 {}'.format(p)
        # for kitty.local
        cmd = 'play -t raw -b 16 -r 24000 -e signed -c 2 {}'.format(mm.get_fn(r))
        os.system(cmd)
        time.sleep(.75)

if __name__ == '__main__':
    main()
