#!/usr/bin/env python3
# coding: utf-8

'''
to demo a fib function which would store calculated fib(n)
to elimate unnecessary recursive and calculation

to solve project euler problem #2:
http://projecteuler.net/problem=2

'''

from fib_store import CalcFib

def main():
    ''' main '''
    # to find the fib number which is even and smaller the upper_limit
    upper_limit = 4e6

    with CalcFib() as fibs:
        i = 1
        even_seq = []
        while True:
            fval = fibs.fib(i)
            if fval > upper_limit:
                break
            if not fval & 1:
                even_seq.append(fval)
                #print "fib(%d) = %d" % (i, fval)
            i += 1

    print(even_seq, "and sum is", sum(even_seq))



if __name__ == '__main__':
    main()
