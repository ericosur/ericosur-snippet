#!/usr/bin/python3
# coding: utf-8

'''
from (1,40) pick a,b (a<b and a!=b)
sum of a and b is 4m
'''

import itertools as it


def main():
    ''' main '''
    v = [x for x in range(1,40+1)]
    p = it.permutations(v, 2)
    cnt = 0
    ans = []
    ans_dict = {}
    for i in p:
        if i[0] > i[1]:
            continue
        cnt += 1
        k = i[0]
        v = i[1]
        if sum(i) % 4 == 0:
            ans.append(i)

            if k not in ans_dict:
                ans_dict[k] = []
            ans_dict[k].append(v)

            #print(i)
    print('total combination: ', cnt)
    #print('len of ans:', len(ans))

    total = 0
    with open("time4.txt", "wt", encoding='UTF-8') as fobj:
        for k,v in ans_dict.items():
            total += len(v)
            print(f'{k:02d}, [{len(v)}] {v}', file=fobj)
    print('total answers: ', total)

if __name__ == '__main__':
    main()
