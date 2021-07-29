#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
demo to write a binary file with random bytes

note:
To profile memory usage of this script,
uncomment "@profile", and use:

python3 -m memory_profiler write_bin4.py

'''

import time
import numpy as np

class Solution():

    X_1MB = 1024 * 1024
    COUNT = 100

    def __init__(self):
        self.fn = 'write_bin4.bin'
        self.buffer = None
        self.fill_buffer()

    def fill_buffer(self):
        ''' fill buffer '''
        #self.buffer = np.zeros(self.COUNT*self.X_1MB, dtype='uint8')
        rng = np.random.default_rng(int(time.time()))
        print(rng)
        self.buffer = rng.integers(0, 255, self.COUNT*self.X_1MB, dtype='uint8')

    def ask(self):
        x = self.COUNT * self.X_1MB
        b = 2**16
        if b > x:
            print("b > 100MB")
        else:
            print("b < 100MB")

    #@profile
    def run(self):
        ''' run '''
        with open(self.fn, 'wb') as binfile:
            binfile.write(self.buffer)
        del self.buffer
        print('output to file {}'.format(self.fn))

        self.ask()

def main():
    '''main function'''
    testrun = Solution()
    testrun.run()

if __name__ == '__main__':
    main()
