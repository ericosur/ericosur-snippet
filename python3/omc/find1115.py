#!/usr/bin/env python3
# coding: utf-8

'''
x = 11k
find x, number root of x is 15
'''

def get_numroot(n):
    ''' get number root '''
    v = [int(x) for x in list(str(n))]
    return sum(v)

def find_answer():
    ''' find answer '''
    for n in range(100, 1000):
        r = get_numroot(n)
        if r == 15:
            print(n)
            if n % 11 == 0:
                print("==>", n)


def main():
    ''' main '''
    find_answer()

if __name__ == '__main__':
    main()
