#!/usr/bin/python3
# coding: utf-8

'''
provides magic numbers for doomsday algorithm

## original flow
The normal flow to calculate weekday from doom number is:
1. get the doom number for this year, for example, 2025 is 2
2. get the month modifiers for all months in 2025,
   the modifiers are: (if leap year, Februrary is 1, common year is 0,
   all other months are the same no matter which year)
    [3, 0, 0, 4, 9, 6,
    11, 8, 5, 10, 7, 12]
3. examples:
  1. 2025/7/4, july = 11, year 2025 modifier = 2, so
   4 - 2 - 11 = -9, which is smaller than 0, so we add 7 repeatedly
   until it is >= 0, so it is 5 which is Friday (0 is Sunday,
   and 1 to 6 are Monday to Saturday)

  2. 2025/12/25, December = 12, year 2025 modifier = 2, so
   25 - 2 - 12 = 11, the 11 mod 7 = 4, which is Thursday

  3. 2025/10/5, October = 10, year 2025 modifier = 2, so
   5 - 2 - 10 = -7, which is smaller than 0, so we add 7 repeatedly
   until it is >= 0, so it is 0 which is Sunday

## simplified flow
This script provides simplied magic numbers for each month in a given year,
and it is much easier to use and avoid negative numbers. **Use addition instead.**

1. For 2025, all magic numbers are:
    2, 5, 5, 1, 3, 6
    1, 4, 0, 2, 5, 0
2. exmaples:
  1. 2025/7/4 (july magic number = 1), can be calculated as:
    (4 + 1) mod 7 = 5, which is Friday.
  2. 2025/12/25 (december magic number = 0), can be calculated as:
    (25 + 0) mod 7 = 4, which is Thursday.
  3. Ex3: 2025/10/5 (october magic number = 2), can be calculated as:
    (5 + 2) mod 7 = 0, which is Sunday.
'''

import sys
from datetime import date
try:
    from rich import print as pprint
    from rich.console import Console
    from rich.table import Table
    USE_RICH = True
    console = Console()
    logd = console.log
except ImportError:
    logd = print
    print("[WARN] no rich.console to use")
    USE_RICH = False
try:
    from dooms_day import DoomsDay
except ImportError:
    logd('cannot import dooms_day, exit')
    sys.exit(1)

class EasyDoomsDay():
    ''' utility functions to provide doomsday number '''
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def __init__(self):
        ''' init '''
        self.today = date.today()
        self.this_year = self.today.year
        self.modifer_year = 0
        self.month_modifiers = []
        self.normalized_modifiers = []

    def normalize_modifier(self):
        ''' normalize month modifier to a list of integers '''
        logd(f'No year doom: {self.month_modifiers}')
        normalized = []
        for d in self.month_modifiers:
            n = -1 * d - self.modifer_year
            while n < 0:
                n += 7
            normalized.append(n)
        logd(f'  normalized: {normalized}')
        self.normalized_modifier = normalized

    def display_in_table(self):
        ''' display magic number in table format '''
        pprint(f'Doom numbers for {self.this_year}: {self.modifer_year}')
        table = Table(title=f"Month Magic Numbers for {self.this_year}")
        table.add_column("Month", justify="left", style="cyan")
        table.add_column("Magic Number", justify="center", style="magenta")
        table.add_column("Doom Number", justify="center", style="green")
        for i in range(12):
            m = self.months[i]
            magic_num = self.normalized_modifier[i]
            doom_num = self.month_modifiers[i]
            table.add_row(m, str(magic_num), str(doom_num))
        console.print(table)

    def display_in_text(self):
        ''' display magic number in text format '''
        # zip mons and self.normalized_modifier
        m = list(zip(self.months, self.normalized_modifier))
        logd(m)
        print(f'Month magic numbers for {self.this_year}:')
        for i in m:
            print(i)

    def display_month_magic_number(self):
        ''' display magic number for this year '''
        if USE_RICH:
            self.display_in_table()
        else:
            self.display_in_text()

    def run(self, year=None):
        ''' calculate doomsday number for the given year '''
        if year is None:
            year = self.this_year
        self.modifer_year = DoomsDay.get_doom_num(year)
        self.month_modifiers = DoomsDay.get_month_modifier(year)
        self.normalize_modifier()
        self.display_month_magic_number()

if __name__ == '__main__':
    # Example usage
    edd = EasyDoomsDay()
    #print(f'Today is {edd.today}')
    edd.run(2025)
