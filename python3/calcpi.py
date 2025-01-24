#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# Monte Carlo method

Using Monte Carlo method to calculate Pi
reference: http://snippets.dzone.com/posts/show/5433

'''

import math
import random
import time

try:
    from rich.console import Console
    from rich.markdown import Markdown
    USE_RICH = True
except ImportError:
    USE_RICH = False

class CalcPi():
    ''' a class to calculate pi from random numbers '''
    REPEAT_TIME = 20_000_000

    def __init__(self):
        self.inside = 0
        self.outside = 0
        self.start = 0
        self.end = 0
        self.console = Console() if USE_RICH else None

    @staticmethod
    def is_on_circle(x, y) -> bool:
        ''' is (x, y) in range of the unit circle '''
        return math.sqrt(x ** 2 + y ** 2) < 1

    def _run_repeat(self):
        ''' repeat random tries '''
        self.outside = 0
        for x in range(CalcPi.REPEAT_TIME):
            x, y = random.random(), random.random()
            if self.is_on_circle(x, y):
                self.inside += 1
            else:
                self.outside += 1

    def get_results(self) -> tuple:
        ''' return results '''
        return float(self.inside), float(self.outside)

    def get_pi(self):
        ''' return guessed pi '''
        self.start = time.time()
        if self.console:
            with self.console.status("[bold green]running...[/]", spinner="dots") as _status:
                self._run_repeat()
        else:
            self._run_repeat()
        r = self.get_results()
        pi = r[0] / (r[0] + r[1]) * 4
        self.end = time.time()
        return pi

    def get_duration(self):
        ''' print duration '''
        d = abs(self.start - self.end)
        print(f"duration: {d:.4f} seconds")

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        if USE_RICH:
            md = Markdown(__doc__)
            obj.console.print(md)
        else:
            print(__doc__)
        print()

        print(f"REPEAT_TIME: {CalcPi.REPEAT_TIME:,}")
        got_pi = obj.get_pi()
        dist = abs(math.pi - got_pi)
        print(f'Estimated pi is {got_pi:.8f} and distance: {dist:.8f}')
        obj.get_duration()

def main():
    '''main function'''
    CalcPi.run()

if __name__ == '__main__':
    main()
