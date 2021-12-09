#!/usr/bin/env python3
# coding: utf-8

'''
to demo a fib function which would store calculated fib(n)
to elimate unnecessary recursive and calculation
https://projecteuler.net/problem=25
'''

from fib_store import CalcFib

def main():
    ''' main '''
    i = 1000
    with CalcFib() as fibs:
        while True:
            result = fibs.fib(i)
            strlen = len(str(result))
            if strlen > 1000:
                break
            print(f"fib({i}) = {result}, len({strlen})")
            i += 1

if __name__ == '__main__':
    main()
