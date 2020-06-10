#!/usr/bin/env python3
# coding: utf-8

'''
demo utf-8 string token as variable name
'''

# pylint: disable=non-ascii-name
def main():
    ''' main '''
    總和 = 0
    次數 = 100
    初值 = 1
    最大值 = 100

    for _ in range(次數):
        for i in range(初值, 最大值+1):
            總和 += i

    print('在重覆 {} 次後，總和為: {}'.format(次數, 總和))

if __name__ == '__main__':
    main()
