#!/usr/bin/env python3
# coding: utf-8

''' 10-digit number, find the max one '''

import itertools as it
import random


class Solution():
    ''' solution '''
    def __init__(self, start: int = 0):
        if start != 0:
            self.start = str(start)
        else:
            self.get_start()

    def __str__(self):
        return str(self.start)

    def get_start(self):
        ''' get start '''
        s = '9876543210'
        l = list(s)
        while True:
            a = []
            for _ in range(10):
                a.append(l[random.randint(0, 9)])
                #a.append(random.choice(s))
            #print('picked:', a)
            try:
                m = ''.join(a)
                #print(f'm:{m} len:{len(m)}')
                if int(m) >= 1e9:
                    break
            except ValueError:
                print('ValueError')
                break
        self.start = m

    def test000(self):
        ''' start '''
        l = list(str(self.start))
        m = sorted(l, reverse=True)
        print('l:', l)
        print('m:', m)

    def test_01(self):
        ''' test '''
        for _ in range(100):
            self.get_start()
            print(str(self.start))

    def get_left(self, remove_part: str) -> str:
        ''' get left digits
            input: 3686167107, 87107
            output: 36616, notice: not 36661
        '''
        begin = self.start
        arr = list(begin)
        print(f'begin: {begin}, remove: {remove_part}')
        res = []
        for cc in list(remove_part):
            i = arr.index(cc)
            lhs = arr[0:i]
            rhs = arr[i+1:]
            #print(cc, ''.join(lhs), ' --- ', ''.join(rhs))
            arr = rhs
            res.extend(lhs)
        return ''.join(res)

    def test(self):
        ''' test '''
        #print('self.start', self.start)
        cnt = 0
        arr = []
        for ii in it.combinations(self.start, 5):
            cnt += 1
            s = ''.join(ii)
            arr.append(int(s))

        #print(f'max:{max(arr)}, cnt:{cnt}')
        # find the max number in all combination
        mpart = str(max(arr))
        # get the left part, remove the max number digits
        misc = self.get_left(mpart)
        print(f"max: {mpart}, misc: {misc}")

    def test_02(self):
        ''' test '''
        self.start = '3686197107'
        print(self.get_left('87107'))


def main():
    ''' main '''
    # 1
    s = Solution(3686197107)
    s.test()
    # 2
    # for _ in range(10):
    #     m = Solution()
    #     m.test()
    #     del m


if __name__ == '__main__':
    main()
