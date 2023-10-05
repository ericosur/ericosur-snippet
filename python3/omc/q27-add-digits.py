#!/usr/bin/env python3
# coding: utf-8

'''
Q27. Rani wrote down the numbers from 1 to 100 on a piece of paper
and then correctly added up all the individual digits of the numbers.
What sum did she obtain?
'''

class Solution():
    ''' solution '''

    LOWER=1
    UPPER=100

    def get_digits(self, val):
        ''' return true if ascending '''
        return list(str(val))

    def sum_digits(self, digits):
        ''' sum of all digits '''
        s = 0
        for i in digits:
            s += int(i)
        return s

    def check_all(self):
        ''' check all '''
        total = 0
        for n in range(Solution.LOWER, Solution.UPPER+1):
            ret = self.get_digits(n)
            s = self.sum_digits(ret)
            print(n, s)
            total += s
        print(total)

    @classmethod
    def run(cls):
        ''' run this '''
        obj = cls()
        obj.check_all()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
