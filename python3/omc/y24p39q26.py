#!/usr/bin/env python3
# coding: utf-8
#

'''
P39 Q26. 某次數學競賽共有 10 道選擇題，評分規則如下：
每一題答對得 4 分，不得得 0 分，答錯倒扣 1 分。
請問這次競賽總共有多少種可能的成績？
'''

def to_ternary(n):
    """
    將十進位數轉換為三進位數
    """
    result = ""
    while n > 0:
        result = str(n % 3) + result
        n //= 3
    return result

def padstr(s):
    ''' fill 0 '''
    return s.zfill(10)

def count_score(s):
    '''
    digit 0, 1, 2
    score -1, 0, 4
    '''
    sc = [-1, 0, 4]
    t = list(s)
    qs = [ int(x) for x in t ]
    total = 0
    for i in qs:
        total += sc[i]
    return total

class Solution():
    ''' to solve more_itertools.dotproduct '''

    def __init__(self):
        self.scores = set()

    def count_all(self):
        ''' count all '''
        cnt = 0
        the_len = 0
        while the_len <= 10:
            tnum = to_ternary(cnt)
            the_len = len(tnum)
            s = count_score(padstr(tnum))
            self.scores.add(s)
            cnt += 1
        print(f'the last cnt: {cnt}')
        print(len(self.scores))
        #print(self.scores)
        score_list = list(self.scores)
        score_list.sort()
        print(score_list)


    def action(self):
        ''' action '''
        print('action!')
        self.count_all()


    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main() -> None:
    ''' main '''
    print(__doc__)
    Solution.run()

if __name__ == '__main__':
    main()
