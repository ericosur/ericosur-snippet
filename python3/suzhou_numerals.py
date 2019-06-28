#!/usr/bin/env python3
# coding: utf-8

'''
https://en.wikipedia.org/wiki/Suzhou_numerals
https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90

蘇州碼子

'''

import random

def rep_suzhou(s):
    ''' int num to string suzhou numerals '''

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
            print('{}: {}'.format(e, cc))
        except IndexError as e:
            print('{}: {}'.format(e, cc))

    return ans

def main(n=None):
    ''' main '''
    if n is None:
        for _ in range(10):
            r = random.randint(100, 999999999)
            print('{} => {}'.format(str(r), rep_suzhou(str(r))))
    else:
        print('{} => {}'.format(n, rep_suzhou(n)))


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        main()
    else:
        for arg in sys.argv[1:]:
            main(arg)
