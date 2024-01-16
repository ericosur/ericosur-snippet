#!/usr/bin/env python3
# coding: utf-8

'''
calculate time difference
'''

import re


USE_ANSICOLOR = False
try:
    from colorama import Fore, Style
    USE_ANSICOLOR = True
except ImportError:
    print('[info] suggest install colorama to enable ansi color')

class Solution:
    ''' time difference in ms '''

    def __init__(self):
        pass

    def e(self, msg):
        ''' error message '''
        if USE_ANSICOLOR:
            print(Fore.RED, end='')
        print(msg)
        if USE_ANSICOLOR:
            print(Style.RESET_ALL, end='')

    def w(self, msg):
        ''' warning message '''
        if USE_ANSICOLOR:
            print(Fore.YELLOW, end='')
        print(msg)
        if USE_ANSICOLOR:
            print(Style.RESET_ALL, end='')

    def s2ms(self, s):
        ''' 14:36:14.783 to xxxxx ms '''
        #print(f'{s=}')
        m = re.match(r'(\d\d):(\d\d):(\d\d)\.(\d\d\d)', s)
        if not m:
            return None
        (hh, mm, ss, ms) = (int(m[1]), int(m[2]), int(m[3]), int(m[4]))
        #print(hh, mm, ss, ms)
        t = hh * 3600.0 + mm * 60.0 + ss * 1.0 + ms/1000.0
        return t

    def tdiff(self, t):
        ''' time diff '''
        t0 = self.s2ms(t[0])
        t1 = self.s2ms(t[1])
        d = t1 - t0
        print(f'{t} ==> {d:.3f} sec')

    def action(self):
        ''' action '''
        inputs = [
            ("14:36:14.783", "14:36:53.659"),
            ("14:49:24.168", "14:50:02.097"),
            ("14:51:03.856", "14:51:21.137"),
            ("14:52:21.603", "14:53:01.536"),
            ("14:53:56.034", "14:54:15.066"),
        ]
        for i in inputs:
            self.tdiff(i)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
