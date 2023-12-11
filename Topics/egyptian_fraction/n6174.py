#!/usr/bin/env python3
# coding: utf-8

''' number 6174
https://en.wikipedia.org/wiki/6174_(number)

Kaprekar's constant

'''

import random


class Solution():
    ''' solution to calculate Kaprekar's constant '''
    def __init__(self):
        self.kaprekar = 6174
        self.last_p = -1
        self.last_q = -1
        self.list_digit = list('0123456789')
        self.max_repeat = 11

    def get_nr_digits(self) -> list:
        ''' rule: no repeat digits '''
        return random.sample(self.list_digit, 4)

    def get_digits(self) -> list:
        ''' get digits '''
        res = []
        for _ in range(4):
            res.append(random.choice(self.list_digit))
        return res

    @staticmethod
    def get_digit2() -> list:
        ''' get digit from integer '''
        n = random.randint(1, 9998)
        return Solution.stringify(n)

    @staticmethod
    def list_to_integer(digits: list) -> int:
        ''' list to integer '''
        v = digits.copy()
        v.reverse()
        s = 0
        t = 1
        for x in v:
            s = s + int(x) * t
            t = t * 10
        return s

    @staticmethod
    def stringify(n: int) -> list:
        ''' stringify and keep 4 digits '''
        s = f'{n:04d}'
        return list(s)

    @staticmethod
    def is_valid(m: list) -> bool:
        ''' is valid '''
        r = Solution.list_to_integer(m)
        if r % 1111 == 0:
            return False
        return True


    def action(self, m: list = None):
        ''' action '''
        ans = -1
        self.last_p = -1
        self.last_q = -1
        if m is None:
            #m = get_nr_digits()
            m = self.get_digits()
        count = 0
        print('=====> start from: ', ''.join(m))

        if not Solution.is_valid(m):
            print('MUST NOT all the same digit')
            return

        while True:
            n = m.copy()
            m.sort(reverse=True)    # 9,8,7,6
            n.sort(reverse=False)   # 6,7,8,9
            #print('{} vs {}'.format(m, n))
            p = self.list_to_integer(m)
            q = self.list_to_integer(n)

            if self.last_p == p and self.last_q == q:
                break

            ans = p - q
            print(f'{p:4d} - {q:4d} = {ans:4d}')
            if ans == self.kaprekar:
                break

            self.last_p = p
            self.last_q = q

            m = Solution.stringify(ans)
            count += 1
            if count >= self.max_repeat:
                print('max repeat hit, terminated')

        print('count: ', count + 1)


def main():
    ''' main '''
    kap = Solution()
    # kap.action(list('6336'))
    # kap.action(list('9999'))
    # kap.action(list('0000'))
    REPEAT = 3
    for _ in range(REPEAT):
        kap.action()

if __name__ == '__main__':
    main()
