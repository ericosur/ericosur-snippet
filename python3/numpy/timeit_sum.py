#!/usr/bin/env python3

import numpy as np
import timeit

class TestSum(object):
    def __init__(self):
        self.data_arr = []
        self.data_size = 10000
        self.test_number = 8000
        self.fill_arr()

    def fill_arr(self):
        # integer value 0 to 99
        self.data_arr = np.random.randint(100, size=self.data_size)

    def test_sum(self):
        time_start = timeit.default_timer()
        for _ in range(self.test_number):
            s = sum(self.data_arr)
        time_end = timeit.default_timer()
        print('duration: {}'.format(time_end-time_start))

    def test_npsum(self):
        time_start = timeit.default_timer()
        for _ in range(self.test_number):
            s = np.sum(self.data_arr)
        time_end = timeit.default_timer()
        print('duration: {}'.format(time_end-time_start))

    def test(self):
        self.test_sum()
        self.test_npsum()


def main():
    foo = TestSum()
    foo.test()

if __name__ == '__main__':
    main()