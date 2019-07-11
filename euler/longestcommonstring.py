#!/usr/bin/env python3
# coding: utf-8

'''
try to find longest common substring
it's buggy
'''


def get_longest_common_substr(S1, S2):
    ''' longest common substring '''
    M = [[0]*(1+len(S2)) for i in range(1+len(S1))]
    longest, x_longest = 0, 0
    for x in range(1, 1+len(S1)):
        for y in range(1, 1+len(S2)):
            if S1[x-1] == S2[y - 1]:
                M[x][y] = M[x - 1][y - 1] + 1
                if M[x][y] > longest:
                    longest = M[x][y]
                    x_longest = x
            else:
                M[x][y] = 0
    return S1[x_longest-longest: x_longest]

def main():
    ''' main '''
    s = '12345678123456789'
    print(s[len(s) // 2:])
    lcs = get_longest_common_substr(s, s[len(s) // 2:])
    print(lcs)
    if lcs == s[len(s) // 2:] and s.find(lcs) == 0:
        print('incorrect')
    else:
        print('shit')


if __name__ == '__main__':
    main()
