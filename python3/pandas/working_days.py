#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
read working days from json
'''

import json
import os

__VERSION__ = '2024.02.26'

FN = 'working-days.json'

def read_jsonfile(fn:str, debug=False):
    '''
    specify json filename and return whole json object
    '''
    if debug:
        print(f'load json from {fn}')
    if not os.path.exists(fn):
        if debug:
            print(f'file not found: {fn}')
        return None
    # read from json file

    # method #1
    with open(fn, 'r', encoding='utf8') as fstream:
        data = json.load(fstream)
    return data

class LoadWorkingDays():
    ''' load working days '''

    def __init__(self):
        self.works = {}
        self.load_data()

    def load_data(self):
        ''' load data '''
        p = self.get_default_config()
        d = read_jsonfile(p)
        try:
            miny = int(d['minyear'])
            maxy = int(d['maxyear'])
            #print(f'{miny=}, {maxy=}')
            for y in range(miny, maxy+1):
                wd = d[f'year{y}']['total']
                self.works[y] = wd

        except ValueError:
            print('ValueError')

    def get_msg(self, yy, wd=None):
        ''' get format message from yy '''
        if yy not in self.works:
            raise IndexError
        if wd is None:
            wd = self.works[yy]
        msg = f'[INFO] There are {wd} working days in {yy}'
        return msg

    def dump(self):
        ''' dump '''
        print(self.works)

    @staticmethod
    def get_default_config():
        ''' search config file in default paths '''
        home = os.getenv('HOME')
        paths = []
        # 1. home/Private/
        tmp = os.path.join(home, 'Private', FN)
        paths.append(tmp)
        # 2. home
        tmp = os.path.join(home, FN)
        paths.append(tmp)
        # 3. local
        tmp = os.path.join('./', FN)
        paths.append(tmp)
        for q in paths:
            if os.path.exists(q):
                return q
        return None


    def action(self):
        ''' action '''
        for k,v in self.works.items():
            print(self.get_msg(k, wd=v))

    @classmethod
    def run(cls):
        ''' run me '''
        obj = LoadWorkingDays()
        obj.action()


def main():
    ''' main '''
    LoadWorkingDays.run()


if __name__ == '__main__':
    main()
