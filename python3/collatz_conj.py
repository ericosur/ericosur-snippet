#!/usr/bin/env python3
# coding: utf-8

'''
http://en.wikipedia.org/wiki/Collatz_conjecture

f(n)=
n/2 if n==0 (mod 2)
3n+1 if n==1 (mod 2)

'''

import argparse
from random import randint


class Collatz():
    ''' collatz conjecture '''
    def __init__(self):
        self.cnt = 0
        self.result = []

    @staticmethod
    def do_rule(n: int) -> int:
        ''' rule of collatz '''
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        return n

    def recursive_collatz(self, n: int) -> None:
        ''' recursive version '''
        self.cnt += 1
        if n <= 1:
            print(n)
            return
        n = Collatz.do_rule(n)
        if n != 1:
            print(n, end='  ')
        self.recursive_collatz(n)
        return

    def loop_collatz(self, n: int) -> None:
        ''' while loop version '''
        while n > 1:
            n = Collatz.do_rule(n)
            self.result.append(n)
            print(n, end='  ')
        print('\nsize:', len(self.result))

def argp():
    ''' prepare and parse CLI arguments '''
    parser = argparse.ArgumentParser(description='calculate Collatz Conjecture')
    parser.add_argument("ints", metavar='int', type=int, nargs='*', default=[randint(2, 97)])
    args = parser.parse_args()
    main(args.ints)

def main(argv: list):
    ''' main '''
    for e in argv:
        obj = Collatz()
        try:
            n = int(e)
            print('===========>>> input:', n)
            print('recursive way:')
            obj.recursive_collatz(n)
            print('  another way:')
            obj.loop_collatz(n)
        except ValueError:
            print(f'{e} is not a valid integer')

if __name__ == '__main__':
    print(__doc__)
    argp()
