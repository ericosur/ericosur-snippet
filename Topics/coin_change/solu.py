#!/usr/bin/env python
#

def sum_up(coins, ans):
    val = 0
    for ii in range(0, len(coins)):
        val = val + coins[ii] * ans[ii]
    return val

def check_guard(ans):
    for ii in len(ans):
        if ans[ii] < 0:
            return False
    return True

def make_arr(coins, all_limits, all_ans):
    cnt = 0
    for k in range(0, all_limits[2]):
        for j in range(0, all_limits[1]):
            for i in range(0, all_limits[0]):
                one_val = [i, j, k]
                all_ans.append(one_val)
                cnt += 1
    print('cnt: ', cnt)

coins = [411, 295, 161]
all_ans = []
make_arr(coins, [8, 11, 20], all_ans)
#print(all_ans)
TARGET = 3200
for aa in all_ans:
    if sum_up(coins, aa) == TARGET:
        print(aa)
        break
