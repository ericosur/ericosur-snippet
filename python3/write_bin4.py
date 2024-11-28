#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
demo to write a binary file with random bytes

note:
To profile memory usage of this script,
uncomment "@profile", and use:

python3 -m memory_profiler write_bin4.py

'''

import argparse
import time

import numpy as np


class Solution():
    ''' class to write buffer with random bytes into a file '''

    COUNT = 100
    X_1MB = 1024 * 1024

    # pylint: disable=invalid-name
    def __init__(self):
        self.fn = 'write_bin4.bin'
        self.buffer = None
        self.fill_buffer()

    def fill_buffer(self):
        ''' fill buffer with fixed size '''
        #self.buffer = np.zeros(self.COUNT*self.X_1MB, dtype='uint8')
        rng = np.random.default_rng(int(time.time()))   # np's random number generator
        print(rng)
        # value = 0 .. 255
        self.buffer = rng.integers(0, 256, self.COUNT*self.X_1MB, dtype='uint8')

    def ask(self):
        ''' test '''
        x = self.COUNT * self.X_1MB
        b = 2**16
        if b > x:
            print("b > 100MB")
        else:
            print("b < 100MB")

    #@profile
    def run(self):
        ''' output pre-filled buffer into file '''
        with open(self.fn, 'wb') as binfile:
            binfile.write(self.buffer)
        del self.buffer
        print(f'output to file {self.fn}')

        self.ask()

def test(files):
    ''' test '''
    for f in files:
        print(f)

def main():
    '''main function'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=str, nargs='*', help="specified files to dump")
    parser.add_argument("-d", "--demo", action='store_true', default=False, help='apply demo mode')

    args = parser.parse_args()

    if args.demo:
        #print('demo:', args.demo)
        test([])
        return

    if args.files == []:
        parser.print_help()
        return

    #print(__doc__)
    testrun = Solution()
    testrun.run()

    test(args.files)


if __name__ == '__main__':
    main()
