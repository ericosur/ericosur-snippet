#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
get delta seconds from specified time point
'''

from __future__ import print_function
import argparse
import datetime
try:
    from rich.console import Console
    from rich.table import Table
    RICH_ENABLED = True
except ImportError:
    RICH_ENABLED = False

class Solution():
    ''' a class to calculate delta seconds '''
    base = 2
    birthday = datetime.datetime(1989, 6, 4, hour=12, minute=34)
    base_start = 27
    base_end = 31

    def __init__(self, rich=RICH_ENABLED):
        self.use_rich = rich
        self.title = f"Delta Seconds from {self.birthday.strftime('%Y-%m-%d %H:%M:%S')}"

    @classmethod
    def get_delta(cls, power):
        ''' get delta seconds from birthday '''
        return cls.birthday + datetime.timedelta(seconds=cls.base**power)

    def show_delta_as_table(self):
        ''' show delta seconds as a table '''
        console = Console()
        table = Table(title=self.title)
        table.add_column(f"Power of {Solution.base}", justify="right", style="cyan")
        table.add_column("DateTime", justify="left", style="magenta")
        table.add_column("In days", justify="right", style="green")
        for i in range(Solution.base_start, Solution.base_end + 1):
            delta_time = Solution.get_delta(i)
            delta_days = (delta_time - datetime.datetime.now()).days
            table.add_row(str(i), str(delta_time), str(delta_days))
        console.print(table)

    def show_by_print(self):
        ''' show delta seconds by print '''
        print(self.title)
        for i in range(Solution.base_start, Solution.base_end + 1):
            result = Solution.get_delta(i)
            # to get the delta days between today
            delta_days = (result - datetime.datetime.now()).days
            print('2 ^', i, ": ", result, "\t", delta_days)

    def show(self):
        ''' show the delta seconds '''
        if self.use_rich:
            self.show_delta_as_table()
        else:
            self.show_by_print()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='Calculate delta seconds from a base date.')
    parser.add_argument('--print', dest='use_print', action='store_true', default=False,
                        help='force to use print to display the table'
                        ' (default: use rich if available)')
    args = parser.parse_args()
    if args.use_print:
        sol = Solution(rich=False)
    else:
        # use rich if available
        sol = Solution()
    sol.show()

if __name__ == '__main__':
    main()
