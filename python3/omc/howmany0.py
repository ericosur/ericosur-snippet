#!/usr/bin/env python3
# coding: utf-8

'''
1 to 10000, how many digit 0 are written
'''

import itertools as it
import operator

class Solution():
    ''' solution '''
    lower = 1
    upper = 10000

    def __init__(self):
        self.answers = []

    def count_digits(self, val):
        '''
        count_digits
        '''
        digits = list(str(val))
        counts = 0
        for d in digits:
            if d == '0':
                counts += 1
        if counts > 0:
            #print(val, counts)
            pass
        return int(digits[0])-1, counts


    def find_answer(self, lower, upper):
        ''' run this '''
        self.lower = lower
        self.upper = upper
        cnt = 0
        answers = [0 for _ in range(9)]
        #print(answers)
        for n in range(self.lower, self.upper+1):
            _, ret = self.count_digits(n)
            if ret > 0:
                if len(str(n)) == 1:
                    answers[0] += ret
                elif len(str(n)) == 2:
                    answers[1] += ret
                elif len(str(n)) == 3:
                    answers[2] += ret
                elif len(str(n)) == 4:
                    answers[3] += ret
                elif len(str(n)) == 5:
                    answers[4] += ret

                cnt += ret
        print(f'{lower} ~ {upper}:', cnt)
        #print(answers)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.find_answer(1000, 1999)
        obj.find_answer(2000, 2999)
        obj.find_answer(3000, 3999)
        obj.find_answer(4000, 4999)
        obj.find_answer(1000, 9999)
        obj.find_answer(1, 9999)


def main():
    ''' main '''
    print('main')
    Solution.run()

if __name__ == '__main__':
    main()
