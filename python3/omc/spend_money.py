#!/usr/bin/python3
# coding: utf-8

import itertools as it


class SpendMoney():
    def __init__(self):
        self.husband = list("abcd")
        self.wife = list("ABCD")
        self.husband_spend = {'a':1, 'b':2, 'c':3, 'd':4}
        self.wife_spend_multiple = {'A':1, 'B':2, 'C':3, 'D':4}
        self.total = 40
        self.cases = []

    def check_cases(self):

        for c in self.cases:
            spend_total = 0
            pair_text = []
            for x in c:
                pair_text.append(f'{x[0]}{x[1]}')
                ws = self.wife_spend_multiple[x[0]] * self.husband_spend[x[1]]
                pair_total = ws + self.husband_spend[x[1]]
                #msg = msg + f' {ws},{self.husband_spend[x[1]]} ;'
                spend_total += pair_total
            pair_text.sort()

            left_money = self.total - spend_total
            print(pair_text, spend_total, left_money)
            if left_money % 8 == 0:
                print('bingo!!')

    def run(self):
        '''
        wife ABCD husband abcd, no need to arrange abcd, just get
        permutations of ABCD like ABCD, ABDC, ACDB, ACBD... len = 24
        and then zip them with abcd. We get all permutations of
        wife-husband cases.
        '''
        for x in it.permutations(self.wife, 4):
            z = zip(list(x), self.husband)
            p = []
            for y in z:
                p.append(y)
            self.cases.append(p)

        self.check_cases()


def main():
    ''' main '''
    sm = SpendMoney()
    sm.run()

if __name__ == '__main__':
    main()
