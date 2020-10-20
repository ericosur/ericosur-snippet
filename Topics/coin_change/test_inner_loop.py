#!/usr/bin/python3.6
# coding: utf-8

'''
brief description for this script
'''

from itertools import permutations
from minus_square import get_inner_loop


def main():
    ''' main '''
    # change MAX_RANGE to know possible max repeat
    MAX_RANGE = 29
    nums = list(range(MAX_RANGE))

    r = get_inner_loop([0, 9, 4, 1])
    print('test: r: ', r)

    max_r = 0
    cnt = 0
    for v in permutations(nums, 4):
        cnt += 1
        #v = random.sample(nums, k=4)
        #print(v)
        r = get_inner_loop(v)
        if r > max_r:
            print('repeat: ', r, ' and its: ', v)
            max_r = r
    print('{} tested'.format(cnt))

if __name__ == '__main__':
    main()
