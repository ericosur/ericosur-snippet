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
        self.wdays = []
        self.load_data()

    def load_data(self):
        ''' load data '''
        p = DefaultConfig(self.FN).get_default_config()
        if p is None:
            print(f'[FAIL] fail to {self.FN} in all default locations')
            sys.exit(1)
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
        self.wdays.append(wd)
        msg = f'[INFO] There are {wd} working days in {yy}'
        return msg

    def show_avg(self):
        ''' show average and median of working days '''
        avgd = sum(self.wdays) / len(self.wdays)
        print(f'[INFO] avg: {avgd:.2f} days')
        self.wdays.sort()
        L = len(self.wdays)
        if L % 2 == 0:
            L = L // 2
            m = (self.wdays[L] + self.wdays[L-1]) / 2
        else:
            m = self.wdays[int(L/2)]
        print(f'[INFO] median: {m:.2f} days')

    def dump(self):
        ''' dump '''
        print(self.works)

    def action(self):
        ''' action '''
        for k,v in self.works.items():
            print(self.get_msg(k, wd=v))
        self.show_avg()

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
