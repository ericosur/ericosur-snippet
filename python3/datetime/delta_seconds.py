#!/usr/bin/env python3

'''
get delta seconds from specified time point
'''

import argparse
import datetime
import sys

try:
    from rich.table import Table
    RICH_ENABLED = True
except ImportError:
    RICH_ENABLED = False

try:
    from be_prepared import TAIPEI_TZ
    from datetime_common import prt
except ImportError as e:
    print('[WARN] import error: ', e)
    sys.exit(1)

class Solution:
    ''' a class to calculate delta seconds '''
    base = 2
    birthday = datetime.datetime(1989, 6, 4, hour=12, minute=34, tzinfo=TAIPEI_TZ)
    base_start = 27
    base_end = 31

    def __init__(self, rich=RICH_ENABLED):
        self.use_rich = rich
        self.title = f"Delta Seconds from {self.birthday.strftime('%Y-%m-%d %H:%M:%S')}"

    @classmethod
    def get_delta(cls, power):
        ''' get delta seconds from birthday '''
        return cls.birthday + datetime.timedelta(seconds=cls.base**power)

    @staticmethod
    def get_now() -> datetime.datetime:
        ''' return datetime for now '''
        return datetime.datetime.now(tz=TAIPEI_TZ)

    def show_delta_as_table(self):
        ''' show delta seconds as a table '''
        if not RICH_ENABLED:
            raise ImportError("rich is not available")

        table = Table(title=self.title) # type: ignore
        table.add_column(f"Power of {Solution.base}", justify="right", style="cyan")
        table.add_column("DateTime", justify="left", style="magenta")
        table.add_column("In days", justify="right", style="green")
        for i in range(Solution.base_start, Solution.base_end + 1):
            delta_time = Solution.get_delta(i)
            delta_days = (delta_time - Solution.get_now()).days
            table.add_row(str(i), str(delta_time), str(delta_days))
        prt(table)

    def show_by_print(self):
        ''' show delta seconds by print '''
        print(self.title)
        for i in range(Solution.base_start, Solution.base_end + 1):
            result = Solution.get_delta(i)
            # to get the delta days between today
            delta_days = (result - Solution.get_now()).days
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
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--rich', '-r', dest='use_rich', action='store_true',
                       help='force rich.table output')
    group.add_argument('--print', '-p', dest='use_print', action='store_true',
                       help='force plain print output')
    args = parser.parse_args()
    if args.use_print:
        sol = Solution(rich=False)
    elif args.use_rich:
        sol = Solution(rich=True)
    else:
        # default: rich if available, else print
        sol = Solution(rich=RICH_ENABLED)
    sol.show()

if __name__ == '__main__':
    main()
