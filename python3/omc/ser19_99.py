#!/usr/bin/python3
# coding: utf-8

'''
19, 99, 80, 19, 61
'''


def main():
    ''' main '''
    p = [19, 99, 80, 19, 61]
    limit = 2023
    for i in range(2, limit):
        if i >= len(p):
            t = abs(p[i-1] - p[i-2])
            p.append(t)
    print(p[2022])



if __name__ == '__main__':
    main()

'''
# 1-18
19, 99, 80, 19, 61, 42, 19, 23, 4, 19, 15, 4, 11, 7, 4, 3, 1, 2,

#19th, 20th, 21th, 22th
1101
#23,24,25,26
1011
#27,28,29,30
0110

1101
1011
0110

'''