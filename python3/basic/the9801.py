#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
計算 1/9801 的小數部分，並輸出其循環位數長度及內容。
'''

from math import gcd
from decimal import Decimal, getcontext
from sympy import factorint
try:
    from rich.console import Console
    console = Console()
    logd = console.log
except ImportError:
    logd = print

def do_nothing(*_args, **_wargs) -> None:
    ''' do nothing'''
    return None

logd = do_nothing

class Solution():
    ''' Solution class '''

    def __init__(self, n: int):
        ''' Constructor '''
        self.n = n
        self.ans = None

    @staticmethod
    def find_order_direct(a, n):
        '''
        找出 a 在 mod n 下的階
        :param a: Description
        :param n: Description
        '''
        for L in range(1, n + 1):
            r = pow(a, L, n)
            logd(f'{a}^{L} mod {n} = {r}')
            if r == 1:
                return L
        return None

    @staticmethod
    def use_decimal(n: int, cylen: int) -> None:
        ''' use decimal to get longer precision '''
        getcontext().prec = cylen * 3
        result = Decimal(1) / Decimal(n)
        # verbose output
        #print(f"1/{n} 的小數表示為: {result}")
        # 轉為字串並去除 "0." 部分
        cycle_str = str(result).split('.')[1]
        pivot = cylen
        part1 = cycle_str[0:pivot]
        part2 = cycle_str[pivot:2*pivot]
        if part1 == part2:
            print(f"前 {pivot} 位確認為循環節")
            logd(part1)
            return part1
        return None

    @staticmethod
    def determine_cycle_length(n):
        ''' determine_cycle_length '''
        thed = factorint(n)
        print(f"{n} 的質因數分解: {thed}")
        nums = []
        for key in thed.keys():
            #print(key, thed[key])
            nums.append(pow(key, thed[key]))
        logd(f"{nums=}")  # [81, 121]
        lens = []
        for num in nums:
            r = Solution.find_order_direct(10, num)
            logd(f'find_order_direct(10, {num}):{r}')
            lens.append(r)
        print(f"各質因數的循環長度: {lens}")
        # 計算最小公倍數
        lcm = lens[0]
        for length in lens[1:]:
            lcm = lcm * length // gcd(lcm, length)
        print(f"最小公倍數(總循環長度): {lcm}")
        return lcm

    def action(self):
        ''' action method '''
        cycle_length = Solution.determine_cycle_length(self.n)
        self.ans = Solution.use_decimal(self.n, cycle_length)
        if self.ans is not None:
            print(f"1/{self.n} 的循環節長度為 {cycle_length}，內容為:")
            print(self.ans)
        else:
            print("無法確認循環節內容")

    @classmethod
    def run(cls, n: int):
        ''' run method '''
        obj = cls(n)
        obj.action()

def main():
    ''' main '''
    num = 9801
    Solution.run(num)

if __name__ == "__main__":
    main()
