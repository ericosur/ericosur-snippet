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

    def check_pair_sum(self):
        ''' check sum of two primes '''
        if self.limit % 2 != 0:
            print(f'ERROR: limit({self.limit}) must be a even number')
            return
        answers = []
        for p in self.primes[1:len(self.primes)]:
            left = self.limit - p
            if left in self.primes:
                if left > p:
                    (p, left) = (left, p)
                t = (left, p)
                if not t in answers:
                    answers.append(t)
        print(f'pair sum is {self.limit}')
        for i in answers:
            print(i)

    def find_piece(self):
        ''' find_piece '''
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
        obj.show_total()
        obj.check_pair_sum()
        obj.find_piece()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
