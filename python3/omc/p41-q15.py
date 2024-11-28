#!/usr/bin/env python3
# coding: utf-8

'''
P52 QAI-6 有一個三位數，各位上數字和為21，
只知十位上的數字比個位上的數字大1，這樣的三位數有多少個？
'''


class Solution():
    ''' try to find solution '''

    def __init__(self):
        self.n = 0
        self.digits = []

    @staticmethod
    def get_value(digits):
        ''' given digits, return value '''
        val = 0
        try:
            for d in digits[:-1]:
                val += int(d)
                val *= 10
            val += int(digits[-1])
        except ValueError:
            print("something wrong")
            return None
        return val

    def validate(self, n):
        ''' validate '''
        if n < 100 or n > 999:
            return False

        self.digits = list(str(n))
        ds = [int(x) for x in self.digits]
        if sum(ds) == 21 and ds[1]-ds[2]==1:
            return True
        return False


    def action(self):
        ''' action '''
        for i in range(100, 999+1):
            if self.validate(i):
                print(i)


    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()


def main():
    ''' main '''
    print(__doc__)
    Solution.run()

if __name__ == '__main__':
    main()
