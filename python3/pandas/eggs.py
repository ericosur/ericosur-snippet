#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' simple csv sample
    output 10 random numbers to eggs.csv with csv module
'''

from __future__ import print_function

import csv
import os
import random

try:
    from rich.console import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print

class Solution():
    '''solution class'''

    COUNT = 10
    CSVFN = 'eggs.csv'

    def __init__(self):
        self.arr = []
        self.get_filled_array()

    def get_filled_array(self) -> None:
        ''' get ten random numbers '''
        if len(self.arr) != Solution.COUNT:
            self.arr.clear()
        for _ in range(Solution.COUNT):
            self.arr.append(random.randint(0, 99))

    def output_array_to_csv(self, filename: str) -> None:
        ''' output to csv '''
        if os.path.isfile(filename):
            logd(f'remove existed {filename}')
            os.remove(filename)
        with open(filename, 'wt', encoding='utf8') as csvfile:
            sw = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
            sw.writerow(self.arr)
        logd(f'output {Solution.COUNT} random numbers to {filename}')

    @classmethod
    def run(cls):
        ''' runme '''
        obj = cls()
        obj.get_filled_array()
        obj.output_array_to_csv(Solution.CSVFN)

def main():
    '''main function'''
    Solution.run()

if __name__ == '__main__':
    main()
