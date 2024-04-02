#!/usr/bin/env python3
# coding: utf-8

'''
https://en.wikipedia.org/wiki/Monty_Hall_problem

numeric simulation for Monty Hall problem

3 doors, 2 gots and 1 car, the host always open an door with goat,
the play always changes his/her choice.

For 3 doors, chances to get the car is 2/3. D as the number of doors, D >= 3.
If the player chooses the door with car, then he loses after changing choice.
So the first step, the player must choose the goat door. The chance is

1 - \frac{1}{D}

Then the host always opens a goat door. Remain 1 door. The chance to choose:

\frac{1}{D-2}

The total chance would be:

C = (1 - \frac{1}{D}) * \frac{1}{D-2}

--------------------------------------------------
For 4 doors, chances to get the car is 3/8.

C_4 = (1 - \frac{1}{4}) * \frac{1}{2} = \frac{3}{8}

'''

from random import randint
from time import time


class MontyHall():
    ''' solution for monty hall problem '''
    REPEAT = 5_000_000
    DOORS = 4
    EXPECTED = float(3 / 8)

    @classmethod
    def run(cls):
        ''' run the simulation '''
        ans = 1
        cnt_car = 0
        cnt_goat = 0
        print(f'repeat={cls.REPEAT}, start...')
        start = time()
        for _ in range(cls.REPEAT):
            choose1 = randint(1, cls.DOORS)
            if choose1 == ans:
                cnt_goat += 1
                continue
            choose2 = randint(1, cls.DOORS-2)
            if choose2 == ans:
                cnt_car += 1
            else:
                cnt_goat += 1
        duration = time() - start
        print(f'cnt_car:{cnt_car}, cnt_goat:{cnt_goat}')
        r = cnt_car / cls.REPEAT
        print(f'ratio: {r:.4f}, distance to expected: {abs(r-cls.EXPECTED):.4f}')
        print(f'it takes {duration:.3f} sec')

def main():
    ''' main '''
    MontyHall.run()

if __name__ == '__main__':
    main()
