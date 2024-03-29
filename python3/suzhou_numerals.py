#!/usr/bin/env python3
# coding: utf-8

'''
https://en.wikipedia.org/wiki/Suzhou_numerals
https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90

蘇州碼子

'''

import random
import sys


def rep_suzhou(the_input):
    ''' int num to string suzhou numerals '''

    s = the_input
    if not isinstance(the_input, str):
        s = str(the_input)

    ten = '\u3038'
    twenty = '\u3039'
    thirty = '\u303a'
    if s == '30':
        return thirty
    if s == '20':
        return twenty
    if s == '10':
        return ten

    arr = ['\u3007', '\u3021', '\u3022', '\u3023', '\u3024',
           '\u3025', '\u3026', '\u3027', '\u3028', '\u3029']

    #print('arr:', arr)
    ans = ''
    for cc in s:
        try:
            ans += arr[int(cc)]
        except ValueError as e:
            print(f'{e}: {cc}')
        except IndexError as e:
            print(f'{e}: {cc}')

    return ans

def prepare_args():
    ''' prepare args '''
    REPEAT = 5
    rets = []
    rets.append('1234567890')
    for _ in range(REPEAT):
        r = random.randint(100, 999999999)
        rets.append(str(r))
    return rets

def main(args):
    ''' main '''
    if args == []:
        print('using default values...')
        args = prepare_args()

    for s in args:
        print(f'{s:>10s} => {rep_suzhou(s)}')


if __name__ == '__main__':
    main(sys.argv[1:])
