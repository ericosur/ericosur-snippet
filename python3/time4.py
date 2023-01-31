#!/usr/bin/python3
# coding: utf-8

'''
find a smallest integer that could be divided by 11 and
all digits sum is 15
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
        cnt += 1
        if i[0] > i[1]:
            continue
        k = i[0]
        v = i[1]
        if sum(i) % 4 == 0:
            ans.append(i)

            if k in ans_dict:
                ans_dict[k] += 1
            else:
                ans_dict[k] = 1

            #print(i)
    print('total: ', cnt)
    print('len of ans:', len(ans))

    total = 0
    for k,v in ans_dict.items():
        total += v
        print(k, v)
    print('total: ', total)

if __name__ == '__main__':
    main()
