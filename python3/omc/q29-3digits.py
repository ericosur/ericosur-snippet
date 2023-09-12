#!/usr/bin/env python3
# coding: utf-8

'''
Q29: Find the largest 3-digit number, with no two digits
the same and with its digits in ascending order,
which when multiplied by 5 has its digits in descending order?

124, 126, 128, 146, 148, 168
'''

class Solution():
    ''' class to find solution '''
    LOWER=100
    UPPER=999

    def __init__(self):
        self.answers = []
        self.drops = []

    def if_the_same(self, d):
        ''' check same '''
        return d[0] == d[1] or d[1] == d[2] or d[2] == d[0]

    def if_ascending(self, d):
        ''' return true if ascending '''
        return d[2] > d[1] > d[0]

    def if_descending(self, d):
        ''' return true if ascending '''
        return d[0] > d[1] > d[2]

    def check_digits_method2(self, val):
        ''' check digits '''

        # rule 3, multipled by 5 must be still 3-digit number
        if val * 5 > 999:
            #print(f'#3, drop, too large: {val}')
            self.drops.append(val)
            return

        digits = list(str(val))
        if self.if_the_same(digits):
            #print(f'drop the same: {val}')
            return
        if not self.if_ascending(digits):
            return
        self.answers.append(val)

    def check_digits_method1(self, val):
        ''' check digits '''
        show_drop = False
        digits = list(str(val))
        # rule 1, no digits are the same
        if self.if_the_same(digits):
            if show_drop:
                print(f'#1, drop: {val}')
            return
        # rule 2, ascending
        if not self.if_ascending(digits):
            if show_drop:
                print(f'#2, drop: {val}')
            return
        # rule 3, multipled by 5
        if val * 5 > 999:
            if show_drop:
                print(f'#3, drop, too large: {val}')
            return
        digits = list(str(val*5))
        if self.if_descending(digits):
            self.answers.append(val)
            return
        if show_drop:
            print(f'#4, drop, not descending: {val}')

    def check_all(self):
        ''' check all '''
        for n in range(Solution.LOWER, Solution.UPPER+1):
            self.check_digits_method1(n)

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.check_all()
        print(f'{len(obj.answers)=}')
        print(f'{obj.answers[-1]=}')
        print(f'{obj.answers=}')
        rev = [x*5 for x in obj.answers]
        print(f'{rev=}')
        #print(f'{len(obj.drops)=}')

def main():
    ''' main '''
    Solution.run()


if __name__ == '__main__':
    main()
