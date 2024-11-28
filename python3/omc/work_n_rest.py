#!/usr/bin/env python3
# coding: utf-8

'''
A works 9 days and rests 1 day
B works 6 days and rests 1 day

today A takes a rest and B will rest next day.
How many days later will A and B both rest?
'''

class Solution():
    ''' solution '''
    WORK_A = 9
    WORK_B = 6
    def __init__(self):
        self.day_over = 0

    def action(self):
        '''  action '''
        cnt = 0
        while True:
            self.day_over += 1
            cnt += 1
            if self.day_over % (self.WORK_A+1) == 0:
                print(f'A rest on {self.day_over=}')
            if self.day_over % (self.WORK_B+1) == 0:
                tmp = self.day_over + 1
                print(f'B will rest next day {tmp}')
            if cnt > 100:
                break

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
