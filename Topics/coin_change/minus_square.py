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
from typing import List

def get_dist(v: List) -> List:
    ''' v is a len=4 list '''
    #print(v)
    t = []
    t.append(abs(v[1] - v[0]))
    t.append(abs(v[2] - v[1]))
    t.append(abs(v[3] - v[2]))
    t.append(abs(v[0] - v[3]))
    #print(t)
    return t

def is_all_zeros(v: List) -> bool:
    ''' input v, check if it is all zeros '''
    t = v if isinstance(v, list) else list(v)
    zeros = [0 for _ in range(len(v))]
    return t == zeros

# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
def checkEqual3(lst: List):
    ''' check if all elements are equal in list '''
    return lst[1:] == lst[:-1]

def test():
    ''' test '''
    v = [3, 2, 3, 2]
    t = get_dist(v)
    ret = is_all_zeros(t)
    print(ret)

def test2():
    ''' test2 '''
    pairs = [(1,2,3,4), (5,6,7,8)]
    ret = check_duplicated(pairs, [2,3,4,1])
    print(ret)

def show_answer(vv: List):
    ''' vv is list of list '''
    print(f'There are {len(vv)} items for answer:')
    for v in vv:
        print(v)

# refer to: https://www.techiedelight.com/rotate-list-python/
def rotate(seq: List, k: int) -> List:
    ''' rotate a list k position, for example,
        a=[1,2,3,4,5], k=2, returns: [3,4,5,1,2]
    '''
    try:
        return seq[k:] + seq[:k]
    except IndexError:
        print('[ERROR] out of bound')
        return None


def check_rotated(m: list, n: list) -> bool:
    ''' m is answer, n is to test
        sometimes n is tuple, need to cast to 'list', or list != tuple
        return true if m = [2, 3, 5, 7], n belongs to [3, 5, 7, 2] or [5, 7, 2, 3]
        raise exception if size mismatched
    '''
    #print('{} vs {}... '.format(m, n), end='')
    p = m if isinstance(m, list) else list(m)
    q = n if isinstance(n, list) else list(n)

    # should be same length
    if not len(p) == len(q):
        raise IndexError

    # obviously not a same rotated list (if all positive numbers)
    if sum(p) != sum(q):
        return False

    if p == q:
        #print('same 1')
        return True

    max_rotate = len(m)
    for k in range(max_rotate):
        tmp = rotate(p, k)
        #print(tmp, ' vs ', q)
        if tmp == q:
            #print('same 2')
            return True

    return False

def check_duplicated(pairs, v) -> bool:
    ''' pairs are checked (no matter best answer or not), v is a list '''
    print(f'there are {len(pairs)} items in pairs')
    for i in pairs:
        if check_rotated(i, v):
            print(f'dup: {i} vs {v}')
            return True
    return False

def remove_duplicated(pairs) -> List:
    ''' remove duplicated '''
    ans = []
    pivot = 0
    while len(pairs) > 0:
        try:
            head = pairs[pivot]
            #print('head:', head)
            remove_list = []
            for i in pairs[pivot+1:]:
                if check_rotated(head, i):
                    #print('dupe', head, 'vs', i)
                    remove_list.append(i)
            for r in remove_list:
                #print('removed:', r)
                pairs.remove(r)
            remove_list.clear()
            #print('add:', head)
            ans.append(head)
            pivot += 1
        except IndexError:
            #ans.append(head)
            #print('add:', head)
            break

    #print('remove_duplicated: ', len(pairs), pairs)
    return pairs

def get_inner_loop(v: List) -> int:
    ''' get inner loop
        return the repeat times
    '''
    MAX_REPEAT = 999
    inner = 0
    tmp = v
    while True:
        t = get_dist(tmp)
        inner += 1
        if is_all_zeros(t):
            #print('break because ending condition:', t)
            break
        tmp = t
        if inner > MAX_REPEAT:  # shit happens
            raise IndexError

    return inner

def main():
    ''' main '''
    MAX_LOOP = 8
    MAX_ELEM = 4
    pp = list(range(10))    # [0, 1, 2, 3, ..., 9]
    cnt = 0
    max_pairs = []
    stat = {}

    # why permutation not combination?
    # the depth would be different if the position of numbers changes
    for v in permutations(pp, MAX_ELEM):
        cnt += 1
        # if cnt > 5:
        #   print('break because count limit')
        #   break
        inner = get_inner_loop(v)

        if not inner in stat:
            stat[inner] = []
        stat[inner].append(v)

        if inner >= MAX_LOOP:
            max_pairs.append(v)

    print(f'total checked: {cnt}')
    print('=====> before removing duplicated items...')
    show_answer(max_pairs)
    max_pairs = remove_duplicated(max_pairs)
    print('=====> after removing duplicated items...')
    show_answer(max_pairs)

    print('the distribution...')
    for k in sorted(stat.keys()):
        print(f'{k}: {len(stat[k])}')


if __name__ == '__main__':
    main()
    #test2()
