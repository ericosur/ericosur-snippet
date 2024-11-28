#!/usr/bin/env python3
# coding: utf-8

'''
在1到100000 (1E5) 的正整數中，有多少能被15和18整除，但不能被28整除？
'''

def verify_n(n):
    '''
    能被15和18整除，但不能被28整除
    '''
    if n % 15 == 0 and n % 18 == 0:
        if n % 28 != 0:
            return True
    return False


def main():
    ''' main '''
    answers = []
    for i in range(100000+1):
        if verify_n(i):
            answers.append(i)
    print(answers)
    print(len(answers))



if __name__ == '__main__':
    main()
