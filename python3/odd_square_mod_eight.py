#!/usr/bin/env python3
# coding: utf-8
#

'''
if square number is odd, its remainder is 1 after modulus 8
test() will check this
'''

def test() -> None:
    ''' test '''
    UPPER_LIMIT = 1000
    set_picked = set()
    cnt = 0
    for n in range(1, UPPER_LIMIT):
        cnt += 1
        r = pow(n, 2, 8)    # n ** 2 % 8
        #print('{} ** 2 % 8 = {}'.format(n, r))
        # add to set if remainder is 1
        if r == 1:
            set_picked.add(n)
    print('checked numbers:', cnt)
    print('size of set_picked:', len(set_picked))
    #print(f'{set_picked=}')

    # a set filled with odd numbers
    set_odd = set(range(1, 1000, 2))    # 1, 3, 5, 7, ...
    print('difference set:', set_odd - set_picked)  # should be an empty set

def main() -> None:
    ''' main '''
    print(__doc__)
    test()

if __name__ == '__main__':
    main()
