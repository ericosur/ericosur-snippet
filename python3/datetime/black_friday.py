#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
to list black Friday
Here "black Friday" means date 13 for each month and it's Friday.
Not the "Black Friday" after the Thanksgiving
'''

from __future__ import print_function
from datetime import date
from typing import Optional, Annotated
try:
    import typer
    USE_TYPER = True
except ImportError:
    print('warn: fail to import module typer, only demo...')
    USE_TYPER = False
try:
    from rich import print as rprint
    USE_RICH = True
except ImportError as e:
    USE_RICH = False
    print('import error of module rich', e)
from be_prepared import get_thisyear, prepare_values, get_year_color

def get_blackfridays_from_this_year(the_year: int) -> list[date]:
    '''
    if specified year has black, return list[date], or []
    '''
    MIN_MONTH = 1
    MAX_MONTH = 12
    # 0:MON, 1:TUE, 2:WED, 3:THU, 4:FRI, 5:SAT, 6:SUN
    WEEKDAY_FRIDAY = 4
    rets = []
    for mnth in range(MIN_MONTH, MAX_MONTH+1):
        dd = date(the_year, mnth, 13)
        if dd.weekday() == WEEKDAY_FRIDAY:
            rets.append(dd)
    return rets

def show_date(dd: date) -> None:
    ''' show date '''
    if not USE_RICH:
        print(dd)
        return
    clr = get_year_color(dd.year, target_year=-1)
    rprint(f'[{clr}]{dd}[/]')

def get_date_str(dd: date) -> str:
    ''' print date time by format: 13 Sep 2024
    '''
    return dd.strftime("%d %b %Y")

class Solution():
    ''' handle neighbor years from CLI '''
    def __init__(self):
        self.years = None

    def prepare_list_and_run(self, year: int, after: int, before: int,
                             context: int) -> None:
        ''' prepare the list '''
        self.years = prepare_values(year, after=after, before=before, radius=context)
        self.iterate_years()

    def default_demo(self) -> None:
        '''
        list black friday by specifying from_year to to_year
        '''
        self.years = prepare_values(get_thisyear(), after=4)
        self.iterate_years()

    def iterate_years(self):
        ''' iterate years '''
        for y in self.years:
            ret = get_blackfridays_from_this_year(y)
            for r in ret:
                show_date(r)

    @classmethod
    def run(cls):
        ''' run demo only '''
        obj = cls()
        obj.default_demo()

if USE_TYPER:
    def main(values: Annotated[Optional[list[int]],
                                        typer.Argument(help="specify year")] = None,
            after: Annotated[int,
                                typer.Option("--after", "-A", help="after nn year")] = 0,
            before: Annotated[int,
                                typer.Option("--before", "-B", help="before nn year")] = 0,
            context: Annotated[int, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = 0,
            demo: Annotated[bool, typer.Option("--demo", "-D", help="run the demo")] = False,
            ) -> None:
        '''
        If no option is specified, run the default test. If available, color will
        refelct: red for specified year, green is the current year, yellow is both
        '''
        if demo or values is None:
            Solution.run()
            return
        for y in values:
            obj = Solution()
            obj.prepare_list_and_run(y,after=after,before=before,context=context)
            print()

if __name__ == '__main__':
    if USE_TYPER:
        typer.run(main)
    else:
        Solution.run()
