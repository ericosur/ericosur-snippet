#!/bin/usr/env python3
# coding:utf-8


A=[1,None,-1,1,-1,1,1]
B=[1,-1,1,1,-1,-1,None]
C=[None,1,-1,-1,1,-1,1]
D=[-1,-1,-1,1,1,None,-1]
E=[1,1,-1,None,1,-1,1]

def num2ans(n):
    ''' num to ans '''
    ans=[0, 0, 0, 0, 0, 0, 0]
    m = n & 0b01111111
    mask = 0b0000001
    for i in range(7):
        if m & mask:
            ans[i] = 1
        else:
            ans[i] = -1
        mask <<= 1
        #print(mask)
    #print(ans)
    return ans

def get_score(ans, stu):
    ''' correct: +1, incorrect: -1, None: 0 '''
    s = 0
    for i in range(7):
        if stu[i] == ans[i]:
            s += 1
        elif stu[i] is None:
            s += 0
        else:
            s -= 1
    return s

def try_test(ans):
    ''' test '''
    scores = []
    for p in [A, B, C, D]:
        s = get_score(ans, p)
        scores.append(s)
    if scores == [2,2,2,2]:
        return ans
    return None

def main():
    ''' main '''
    correct_ans = None
    for n in range(0,128):
        r = num2ans(n)
        correct_ans = try_test(r)
        if correct_ans:
            print(f'{correct_ans}')
            #print(n)
            break
    if correct_ans:
        print(f'{A},  {get_score(correct_ans,A)}')
        print(f'{B},  {get_score(correct_ans,B)}')
        print(f'{C},  {get_score(correct_ans,C)}')
        print(f'{D},  {get_score(correct_ans,D)}')
        print(f'{E},  {get_score(correct_ans,E)}')


if __name__ == '__main__':
    main()
