#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=wrong-import-position
#

'''
read working days from json
'''

import sys

sys.path.insert(0, "..")
from myutil import read_jsonfile, DefaultConfig

__VERSION__ = '2024.02.26'


class LoadWorkingDays():
    ''' load working days '''
    FN = 'working-days.json'

    def __init__(self):
        self.works = {}
        self.load_data()

    def load_data(self):
        ''' load data '''
        p = DefaultConfig(self.FN).get_default_config()
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
