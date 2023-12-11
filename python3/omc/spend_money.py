#!/usr/bin/python3
# coding: utf-8

'''
柯玲芬、柯伊芬、柯芭芬和柯淑芬與她們的先生一起去大賣場買生活用品，
八人身上所帶的錢，加起來剛好是四萬元 (40)

四位先生各花了一千元、二千元、三千元及四千元
⇒ 各位丈夫花的錢是 (1,2,3,4)

柯玲芬、柯伊芬、柯芭芬和柯淑芬花的錢是她先生的 (1,2,3,4)

⇒ 柯玲芬、柯伊芬、柯芭芬和柯淑芬設為符號 A B C D
四個先生設為符號 a b c d  所以有24種組合

以下列出四對夫婦的組合，以及他們一共花費的錢，還有剩下的錢
⇒ 因為大家都有剩下錢，且剩下一樣多的錢，所以餘錢必定是8的倍數,

'''

import itertools as it


class SpendMoney():
    ''' try to find answer '''
    def __init__(self):
        self.husband = list("abcd")
        self.wife = list("ABCD")
        self.husband_spend = {'a':1, 'b':2, 'c':3, 'd':4}
        self.wife_spend_multiple = {'A':1, 'B':2, 'C':3, 'D':4}
        self.total = 40
        self.cases = []

    def check_cases(self):
        ''' check cases if valid '''
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
