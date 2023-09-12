#!/usr/bin/env python3
# coding: utf-8

'''
3 same digit from 1001 to 2008
'''

class Solution():
    ''' solution '''
    lower = 1001
    upper = 2008

    def __init__(self):
        self.answers = []

    def is_valid(self, val):
        ''' is valid for question '''
        if val > self.upper or val < self.lower:
            return False
        counts = self.count_digits(val)
        if 3 in counts:
            print(val, counts)
            return True
        return False

    def count_digits(self, val):
        '''
        form 0 to 9, how many digits?
        for 1351, get [0, 2, 0, 1, 0, 1, 0, 0, 0, 0]
        '''
        digits = list(str(val))
        counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for d in digits:
            counts[int(d)] += 1

        #print(val, counts)
        return counts


    def find_answer(self):
        ''' run this '''
        cnt = 0
        for n in range(self.lower, self.upper+1):
            if self.is_valid(n):
                cnt += 1
        print('total:', cnt)


    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.find_answer()


def main():
    ''' main '''
    print('main')
    Solution.run()

if __name__ == '__main__':
    main()
