#!/usr/bin/env python3
# coding: utf-8

'''
https://en.wikipedia.org/wiki/Suzhou_numerals
https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90

蘇州碼子

'''

import random
import sys
try:
    from rich.console import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print

# suzhou numerals
# key: str
# value: str (the codepoint)
suzhou_numerals = {
    # 〡〢〣〤〥〦〧〨〩〇
    '0': '3007',    # ideographic number zero
    '1': '3021',    # hangzhou numeral one
    '2': '3022',    # hangzhou numeral two
    '3': '3023',    # hangzhou numeral three
    '4': '3024',    # hangzhou numeral four
    '5': '3025',    # hangzhou numeral five
    '6': '3026',    # hangzhou numeral six
    '7': '3027',    # hangzhou numeral seven
    '8': '3028',    # hangzhou numeral eight
    '9': '3029',    # hangzhou numeral nine
    # 〸 〹 〺
    '10': '3038',   # hangzhou numeral ten, not U+5341 十
    '20': '3039',   # hangzhou numeral twenty, not U+5344 廾
    '30': '303A'    # hangzhou numeral thirty, not U+5345 卅
    # extra info: U+534C (forty) 卌
}

def lookup_suzhou_char_from_str(s: str) -> str:
    ''' get integer value from suzhou numerals '''
    if not isinstance(s, str):
        raise ValueError('s is not str')
    if s in suzhou_numerals:
        return chr(int(suzhou_numerals[s], 16))
    raise ValueError(f'not in suzhou numerals: {s}')

def lookup_suzhou_cp_from_str(the_strs: str) -> str:
    ''' get integer value from suzhou numerals '''
    ret = []
    if the_strs in {'10', '20', '30'}:
        return suzhou_numerals.get(the_strs)
    for s in the_strs:
        ret.append(suzhou_numerals.get(s))
    return ret

def rep_suzhou(the_str: str):
    ''' int num to string suzhou numerals '''
    if the_str in {'10', '20', '30'}:
        return lookup_suzhou_char_from_str(the_str)
    ans = []
    for c in the_str:
        r = lookup_suzhou_char_from_str(c)
        ans.append(r)
    return ''.join(ans)

def show_cp_only(rets):
    ''' show codepoint only '''
    logd('show codepoint only =====>')
    for s in rets:
        try:
            r = lookup_suzhou_cp_from_str(s)
            print(f'{s:>10s} => {r}')
        except ValueError as e:
            print(f'{s:>10s} => {e}')
            continue
    return

def prepare_args():
    ''' prepare args '''
    REPEAT = 3
    rets = ['10', '20', '30', '1234567890']
    for _ in range(REPEAT):
        r = random.randint(100, 999999999)
        rets.append(str(r))
    return rets

def main(args):
    ''' main '''
    if args == []:
        show_cp_only(['10', '20', '30', '1234567890'])
        args = prepare_args()

    for s in args:
        print(f'{s:>10s} => {rep_suzhou(s)}')


if __name__ == '__main__':
    main(sys.argv[1:])
