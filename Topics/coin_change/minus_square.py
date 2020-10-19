#!/usr/bin/env python3
# coding: utf-8

'''
four corner

思考力某一題
從 0 至 9 挑選 4 個不重複的數字, 放在正方形四個角落, 計算數字的距離寫在邊長
中間, 新的 4 個數字再連成一個正方形, 反覆計算到四個邊都是 0 為止, 哪一組數
字可以到達最深的八層呢？

0 ------ 1  0 ------ 5
|        |  |        |
|        |  |        |
|        |  |        |
9 ------ 4  9 ------ 8

第二、三、四個答案其實就是第一個作順時針移動

(0, 1, 4, 9)
(1, 4, 9, 0)
(4, 9, 0, 1)
(9, 0, 1, 4)

(0, 9, 4, 1)
(9, 4, 1, 0)
(4, 1, 0, 9)
(1, 0, 9, 4)

(0, 5, 8, 9)
(5, 8, 9, 0)
(8, 9, 0, 5)
(9, 0, 5, 8)

(0, 9, 8, 5)
(9, 8, 5, 0)
(8, 5, 0, 9)
(5, 0, 9, 8)

'''

#import itertools as it
from itertools import permutations

def get_dist(v):
    ''' v is a len=4 list '''
    #print(v)
    t = list()
    t.append(abs(v[1] - v[0]))
    t.append(abs(v[2] - v[1]))
    t.append(abs(v[3] - v[2]))
    t.append(abs(v[0] - v[3]))
    #print(t)
    return t

def check_dist(v):
    ''' v is a len=4 list '''
    if v[0] == v[1] == v[2] == v[3] == 0:
        return True
    return False

def test():
    ''' test '''
    v = [3, 2, 3, 2]
    t = get_dist(v)
    ret = check_dist(t)
    print(ret)

def show_answer(vv):
    ''' vv is list of list '''
    print('There are {} items for answer:'.format(len(vv)))
    for v in vv:
        print(v)

def main():
    ''' main '''
    pp = list(range(10))
    #print(pp)
    cnt = 0
    MAX_LOOP = 8
    max_pairs = list()
    tmp = list()
    # why permutation not combination?
    # the depth would be different if the position of numbers changes
    for v in permutations(pp, 4):
        cnt += 1
        # if cnt > 5:
        #   print('break because count limit')
        #   break
        inner = 0
        tmp = v
        while True:
            t = get_dist(tmp)
            inner += 1
            if check_dist(t):
                #print('break because ending condition:', t)
                break
            tmp = t
        tmp.clear()
        if inner >= MAX_LOOP:
            max_pairs.append(v)

    show_answer(max_pairs)


if __name__ == '__main__':
    main()
    #test()
