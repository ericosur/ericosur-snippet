#!/usr/bin/env python3
#coding: utf-8

'''
imageio examples
iterate files in specified dir
'''

import os
import imageio.v3 as iio
from pathlib import Path

class Solution():
    ''' class solution '''
    def __init__(self):
        self.home = os.getenv('HOME')

    @staticmethod
    def test():
        ''' test '''
        print('test staticmethod')

    def action(self):
        ''' action '''
        #images = list()
        for file in Path(self.home, "dropbox").iterdir():
            if not file.is_file():
                continue
            print(file)
        #images.append(iio.imread(file))

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
