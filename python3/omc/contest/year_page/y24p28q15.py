#!/usr/bin/env python3

'''
在1到100000 (1E5) 的正整數中，有多少能被15和18整除，但不能被28整除？
'''

def verify_n(n):
    '''
    能被15和18整除，但不能被28整除
    '''
    return (n % 15 == 0 and n % 18 == 0) and (n % 28 != 0)


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
