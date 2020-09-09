#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
small game 幾A幾B
'''

from itertools import permutations
from random import choice

DEBUG = False

def get_wawb(m, n):
    ''' get wawb '''
    a = 0
    b = 0
    for i in range(4):
        for j in range(4):
            if i == j:
                if m[i] == n[j]:
                    a = a + 1
            else:
                if m[i] == n[j]:
                    b = b + 1

    return [a, b]

def find_wawb(total, wawb, guess):
    '''
    wawb: [m, n] how many A how many B
    guess: [1,2,3,4] what the guesser guess
    returns possible list
    '''
    possible = list()
    for elem in total:
        if wawb == get_wawb(elem, guess):
            possible.append(elem)

    return possible


def dump_all(all_list):
    ''' dump all '''
    cnt = 0
    zero_cnt = 0
    for elem in all_list:
        if elem[0] == 0:
            zero_cnt = zero_cnt + 1
        print(elem)
        cnt = cnt + 1

    print("cnt = ", cnt)
    print("zero head count = ", zero_cnt)


def test_get_wawb():
    ''' test: get wawb '''
    a = [1, 2, 3, 4]
    b = [2, 1, 8, 9]
    print('test_get_wawb: {}'.format(get_wawb(a,b)))


def test_intersection(all_answer):
    ''' test: intersection '''
    print('test_intersection...')
    p1 = find_wawb(all_answer, [1,2], [1,2,3,4])
    #print "p1: ", p1
    print("p1 len: ", len(p1))
    p2 = find_wawb(all_answer, [2,1], [2,3,4,5])
    #print "p2: ", p2
    print("p2 len: ", len(p2))

    s1 = set(p1)
    s2 = set(p2)
    print(s1 & s2)
    print('test_intersection...')

def check_guess(to_be_checked: list):
    '''
    檢查是否有重覆的數字在裡頭
    to_be_checked: 輸入檢查
    return: True: 沒問題，False: 數字有重複，重猜
    '''
    #print('check_guess...')
    if to_be_checked == list():   # 允許空的list
        return True
    chk = dict()
    for c in to_be_checked:
        if c in chk:
            chk[c] += 1
        else:
            chk[c] = 1
    for v in chk.values():
        if v > 1:
            return False
    return True


def test_check_guess():
    ''' test check_guess '''
    print('test_check_guess: ', end='')
    assert check_guess([1,3,5,7])
    assert check_guess([])
    assert not check_guess([9,9,2,3])
    assert not check_guess([9,1,9,2])
    assert not check_guess([9,1,2,9])
    assert not check_guess([1,0,1,0])
    print('PASS')

def debug_msg(msg: str):
    ''' print debug msg '''
    if DEBUG:
        print(msg)

def make_wawb_guess(allpair, answer):
    ''' make a guess '''
    acopy = allpair.copy()
    poss = []
    #confirm_neg = []
    confirm_ans = []
    MAX_GUESS = 10
    i = 0
    for i in range(MAX_GUESS):
        debug_msg("=====> try #{}".format(i))   # 第幾次嘗試

        if poss != []:
            acopy = list(poss[0])

        while True:
            my_guess = choice(acopy) # 隨機取一個作猜測
            if check_guess(my_guess):
                break

        result = get_wawb(answer, my_guess) # 結果
        debug_msg('{} => {}'.format(my_guess, result))

        found_pair = find_wawb(acopy, result, my_guess)    # 此結果可能的組合
        debug_msg("len(found_pair): {}".format(len(found_pair)))

        if result == [0, 0]: # 恭喜，這四個數字完全不可能
            debug_msg("these 4 numbers are not possible: {}".format(my_guess))
            #confirm_neg = my_guess
        else:
            if poss == []:
                poss.append(found_pair)
            else:
                tmp0 = set(poss[0])
                tmp1 = set(found_pair)
                new_pair = tmp0 & tmp1

                if new_pair == set():
                    debug_msg("no intersection ???")
                    # and try next
                    continue
                if len(new_pair) == 1:
                    debug_msg("Got answer: {}".format(new_pair))
                    confirm_ans = list(new_pair)
                    break
                if len(new_pair) < 10:
                    debug_msg("left pairs: {}".format(new_pair))
                poss[0] = new_pair

    if get_wawb(answer, list(confirm_ans[0])) == [4,0]:
        print("[INFO] got answer {} vs guessed {}, " \
            "after {} times".format(answer, confirm_ans[0], i))
        return i

    return 0

def main():
    ''' main '''
    # a = [0, 1, 2, ..., 9]
    # all_list = C(10, 4)
    all_list = list(permutations(list(range(10)), 4))
    print('Number of total valid answers: {}'.format(len(all_list)))
    #dump_all(all_list)

    test_intersection(all_list)
    test_get_wawb()
    test_check_guess()

    guess_time = list()
    for _ in range(10):
        print('-' * 20)
        question = choice(all_list)
        print("question: ", question)
        ret = make_wawb_guess(all_list, question)
        guess_time.append(ret)

    print('=' * 40)
    print("max: ", max(guess_time))
    print("min: ", min(guess_time))
    print("sum: ", sum(guess_time))
    print("avg: ", sum(guess_time) / len(guess_time))

if __name__ == '__main__':
    main()
