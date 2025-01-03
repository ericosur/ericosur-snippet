#!/usr/bin/env python3
# coding: utf-8

'''
show an emoji that matches the current time
'''

import sys
import argparse
from datetime import datetime
sys.path.insert(0, "..")
sys.path.insert(0, "python3")
from myutil import prt  # type: ignore[import]

class ShowClock():
    ''' class to show clock '''
    clocks = {
        "0100": "🕐",
        "0200": "🕑",
        "0300": "🕒",
        "0400": "🕓",
        "0500": "🕔",
        "0600": "🕕",
        "0700": "🕖",
        "0800": "🕗",
        "0900": "🕘",
        "1000": "🕙",
        "1100": "🕚",
        "1200": "🕛",
        "0130": "🕜",
        "0230": "🕝",
        "0330": "🕞",
        "0430": "🕟",
        "0530": "🕠",
        "0630": "🕡",
        "0730": "🕢",
        "0830": "🕣",
        "0930": "🕤",
        "1030": "🕥",
        "1130": "🕦",
        "1230": "🕧",
    }

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.hh = None
        self.mm = None
        self.key = None
        self._whatnow()

    def setmm(self, m):
        ''' set m '''
        if 0 <= m <= 59:
            self.mm = m
        else:
            raise ValueError

    def sethh(self, h):
        ''' set h '''
        if h == 0:
            h = 12
        if 12 < h <= 23:
            h = h - 12
        if 1 <= h <= 12:
            self.hh = h
            #prt(f'sethh: {self.hh=}')
        else:
            raise ValueError

    def _whatnow(self):
        ''' get current hour and minute (type: int)
            hh (0 to 23)
            mm (0 to 59)
        '''
        now = datetime.now()
        # Extract hour and minute
        self.sethh(now.hour)
        self.setmm(now.minute)
        assert 0 <= self.mm <= 59
        assert 1 <= self.hh <= 12

    def _step_hour(self):
        ''' 1 to 2, 2 to 3, 11 to 12, 12 to 1
            will not change the current time
        '''
        hh = self.hh + 1
        if hh > 12:
            hh = 1
        assert 0 < hh <= 12
        return hh

    def choose_icon(self):
        ''' choose an icon '''
        m = self.mm
        h = self.hh
        if 0 <= m <= 15:
            # if 1415 use 1400 icon
            m = 0
        elif 16 <= m < 45:
            # if 1623 use 1630 icon
            # if 1342 use 1330 icon
            m = 30
        else:
            m = 0
            h = self._step_hour()
        return f'{h:02d}{m:02d}'

    def get_icon(self):
        ''' return icon '''
        self.key = self.choose_icon()
        return self.clocks.get(self.key)

    def test(self, hh, mm):
        ''' test '''
        self.sethh(hh)
        self.setmm(mm)
        # if you specify hh and mm, you need call
        # choose_icon() and then get_icon()
        r = self.choose_icon()
        i = self.get_icon()
        prt(f'{hh:02d}{mm:02d} ==> {r}\t{i}')

    def do_tests(self):
        ''' run tests '''
        #prt(f"Current hour: {self.hh}, minute: {self.mm}")
        #self.choose_icon()
        self.test(0, 0)
        self.test(0, 14)
        self.test(0, 15)
        self.test(0, 16)
        self.test(0, 29)
        self.test(0, 30)
        self.test(0, 31)
        self.test(0, 44)
        self.test(0, 45)
        self.test(0, 46)
        self.test(12, 15)
        self.test(12, 16)
        self.test(12, 45)
        self.test(12, 46)

    def action(self):
        ''' action '''
        #prt(f'{self.verbose=}')
        icon = self.get_icon()
        if self.verbose:
            prt(self.key, end=' ')
        prt(icon)

    @classmethod
    def run(cls, show_more):
        ''' run me '''
        obj = cls(verbose=show_more)
        obj.action()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='accept an option to verbose')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    parser.add_argument("-t", "--test", action='store_true', default=False,
        help='running tests')
    args = parser.parse_args()

    if args.test:
        obj = ShowClock()
        obj.do_tests()
    else:
        ShowClock.run(args.verbose)

if __name__ == '__main__':
    main()
