#!/usr/bin/env python3
#coding: utf-8

'''
find sum of sequencial primes that meet limit
'''

class Solution():
    ''' class solution '''
    # primes <= 100 (size=25)
    primes = [
        2,3,5,7,11,13,17,19,23,29,
        31,37,41,43,47,53,59,61,67,71,
        73,79,83,89,97]

    def __init__(self):
        self.limit = 60

    def show_total(self):
        ''' show total sum of self.primes '''
        total = sum(self.primes)
        print(f'total sum of primes = {total}')

    def action(self):
        ''' action '''
        print('action!')
        self.show_total()
        for sz in range(len(self.primes)-1, 1, -1):
            for i in range(len(self.primes)-(sz-1)):
                s = slice(i, i+sz)
                piece = self.primes[s]
                if len(piece) != sz:
                    print('ERROR:', i, sz, piece)
                    break
                total = sum(piece)
                if total == self.limit:
                    print(f'{sz=}, {total=}, {piece=}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
