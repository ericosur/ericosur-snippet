#!/usr/bin/env python3
# coding: utf-8

''' want to know the sum of small primes '''

def f(n):
    ''' slice and sum '''
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n == 0:
        return [], 0
    if n < 0:
        raise ValueError
    s = slice(0, n)
    return ps[s], sum(ps[s])

def main():
    ''' main '''
    for i in range(25):
        the_list, the_sum = f(i)
        if the_sum > 100:
            break
        print(the_list, the_sum)


    the_list, the_sum = f(25)
    print(the_list, the_sum)

if __name__ == '__main__':
    main()
