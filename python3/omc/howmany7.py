#!/usr/bin/env python3
# coding: utf-8

'''
3 same digit from 1001 to 2008
'''

class Solution():
    ''' solution '''
    lower = 1
    upper = 999

    def __init__(self):
        self.answers = []

    def count_digits(self, val):
        '''
        count_digits
        '''
        digits = list(str(val))
        counts = 0
        for d in digits:
            if d == '7':
                counts += 1
        if counts > 0:
            #print(val, counts)
            pass
        return int(digits[0])-1, counts


    def find_answer(self):
        ''' run this '''
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
                cnt += ret
        print('total:', cnt)
        print(answers)

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
