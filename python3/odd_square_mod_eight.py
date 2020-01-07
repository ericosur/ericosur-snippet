#!/usr/bin/env python3
# coding: utf-8
#

'''
if sqauare number is odd, its reminder is 1 after modulus 8
test() will check this
'''

def test():
    ''' test '''
    MAX_NUMBER = 1000
    set_picked = set()
    for n in range(MAX_NUMBER):
        r = pow(n, 2, 8)    # n ** 2 % 8
        #print('{} ** 2 % 8 = {}'.format(n, r))
        if r == 1:
            set_picked.add(n)
    #print(picked)

    set_odd = set(range(1, 1000, 2))    # 1, 3, 5, 7, ...
    print('difference set:', set_odd - set_picked)

def main():
    ''' main '''
    test()

if __name__ == '__main__':
    main()
