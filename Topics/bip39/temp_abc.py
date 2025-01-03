#!/usr/bin/env python3
#coding: utf-8

'''
template script
'''

import random
import sys

import array_util


class Solution():
    ''' class solution '''

    arraydat = 'pickle.dat'
    limit = 16

    def __init__(self):
        self.diskarray = array_util.loadarray(self.arraydat)
        if self.diskarray is None:
            print('[fail] no data load')
            sys.exit(1)

    def show(self):
        ''' show '''
        size = len(self.diskarray)
        print(f'pick {self.limit} words from array')
        msg = ''
        for _ in range(self.limit):
            t = self.diskarray[random.randint(0, size-1)]
            if msg == '':
                msg = t
            else:
                msg = msg + ', ' + t
            #print(self.diskarray[t])
        #t = random.randint(0, size-1)
        #msg =
        print(msg)

    def action(self):
        ''' action '''
        self.show()
        #print('len=', len(self.diskarray))

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
