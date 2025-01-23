#!/usr/bin/env python3
# coding: utf-8

'''
# Monty Hall Problem

refer to: https://en.wikipedia.org/wiki/Monty_Hall_problem

numeric simulation for Monty Hall problem

3 doors, 2 gots and 1 car, the host always open an door with goat,
the play always changes his/her choice.

For 3 doors, chances to get the car is 2/3. D as the number of doors, D >= 3.
If the player chooses the door with car, then he loses after changing choice.
So the first step, the player must choose the goat door. The chance is

```1 - \\frac{1}{D}```

Then the host always opens a goat door. Remain 1 door. The chance to choose:

```\\frac{1}{D-2}```

The total chance would be:

```C = (1 - \\frac{1}{D}) * \\frac{1}{D-2}```

For 4 doors, chances to get the car is 3/8.

```C_4 = (1 - \\frac{1}{4}) * \\frac{1}{2} = \\frac{3}{8}```

'''

from random import randint
from time import time
try:
    from rich import print as rprint
    from rich.progress import Progress
    USE_RICH = True
except ImportError:
    USE_RICH = False

prt = rprint if USE_RICH else print
if USE_RICH:
    from rich.console import Console
    from rich.markdown import Markdown
    console = Console()
    md = Markdown(__doc__)
    console.print(md)
    console.print()

class MontyHall():
    ''' solution for monty hall problem '''
    REPEAT = 5_000_000
    DOORS = 4
    EXPECTED = float(3 / 8)
    ANS = 1

    def __init__(self):
        self.cnt_car = 0
        self.cnt_goat = 0

    def show_result(self, duration: float) -> None:
        ''' show result'''
        prt(f'cnt_car:{self.cnt_car:,}, cnt_goat:{self.cnt_goat}')
        r = self.cnt_car / self.REPEAT
        prt(f'ratio: {r:.4f}, distance to expected: {abs(r-self.EXPECTED):.4f}')
        prt(f'it takes {duration:.3f} sec')

    def run_with_progress(self):
        ''' progress bar, it is slower than without progress bar '''
        self.cnt_car = 0
        self.cnt_goat = 0
        prt(f'repeat={self.REPEAT:,}; start...')
        start = time()
        progress_unit = 100  # do not update progress bar too frequently
        with Progress(refresh_per_second=1) as progress:
            task = progress.add_task('searching...', total=self.REPEAT)
            for i in range(self.REPEAT):
                if i % progress_unit == 0:
                    progress.update(task, advance=progress_unit)
                choose1 = randint(1, self.DOORS)
                if choose1 == self.ANS:
                    self.cnt_goat += 1
                    continue
                choose2 = randint(1, self.DOORS-2)
                if choose2 == self.ANS:
                    self.cnt_car += 1
                else:
                    self.cnt_goat += 1
            progress.update(task, advance=self.REPEAT/progress_unit)
        duration = time() - start
        self.show_result(duration)

    def run_without_progress(self):
        ''' no progress bar'''
        self.cnt_car = 0
        self.cnt_goat = 0
        prt(f'repeat={self.REPEAT:,}, start...')
        start = time()
        for _ in range(self.REPEAT):
            choose1 = randint(1, self.DOORS)
            if choose1 == self.ANS:
                self.cnt_goat += 1
                continue
            choose2 = randint(1, self.DOORS-2)
            if choose2 == self.ANS:
                self.cnt_car += 1
            else:
                self.cnt_goat += 1
        duration = time() - start
        self.show_result(duration)

    @classmethod
    def run(cls):
        ''' run the simulation '''
        obj = cls()
        if USE_RICH:
            obj.run_with_progress()
        else:
            obj.run_without_progress()

def main():
    ''' main '''
    MontyHall.run()

if __name__ == '__main__':
    main()
