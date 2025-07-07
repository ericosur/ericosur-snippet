#!/usr/bin/python3
# coding: utf-8

'''
use doomsday algorithm to calculate weekday from range of year
https://en.wikipedia.org/wiki/Doomsday_rule
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
