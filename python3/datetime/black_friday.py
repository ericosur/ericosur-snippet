#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
to list black Friday
Here "black Friday" means date 13 for each month and it's Friday.
Not the "Black Friday" after the Thanksgiving
'''

from __future__ import print_function
from datetime import date
import sys
from typing import Optional, Annotated, Callable, Any
try:
    import typer
    USE_TYPER = True
except ImportError:
    print('[WARN] no module typer, not support CLI options')
    USE_TYPER = False
try:
    from rich import print as rprint
    from rich.console import Console
    from rich.table import Table
    USE_RICH = True
    console = Console()
    consolelog = console.log
except ImportError as e:
    USE_RICH = False
    print('import error of module rich', e)
try:
    from be_prepared import get_thisyear, prepare_values, get_year_color
    from nothing import do_nothing
except ImportError:
    print('import error of be_prepared, please check the module')
    sys.exit(1)


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
    if USE_RICH:
        clr = get_year_color(dd.year, target_year=-1)
        rprint(f'[{clr}]{dd}[/]')
    else:
        print(dd)

def get_date_str(dd: date) -> str:
    ''' print date time by format: 13 Sep 2024
    '''
    return dd.strftime("%d %b %Y")

class Solution():
    ''' handle neighbor years from CLI '''
    def __init__(self, table: bool, log: Callable[[Any], None] = do_nothing) -> None:
        self.logd = log
        self.years = None
        self.results = []
        self.dicts = {}
        self.use_table = table

    def prepare_list_and_run(self, year: int, after: int, before: int,
                             context: int) -> None:
        ''' prepare the list '''
        self.years = prepare_values(year, after=after, before=before, radius=context)
        self.iterate_years()
        self.show_results()

    def default_demo(self) -> None:
        '''
        list black friday by specifying from_year to to_year
        '''
        self.years = prepare_values(get_thisyear(), after=4)
        self.iterate_years()
        self.show_results()

    def show_results(self) -> None:
        ''' show results '''
        if not self.results:
            self.logd('[INFO] no black Friday found')
            return
        if self.use_table:
            self.__show_by_table()
        else:
            self.__show_by_print()

    def __show_by_print(self) -> None:
        ''' show results '''
        logd = self.logd
        logd(f'[INFO] found {len(self.results)} black Fridays')
        for r in self.results:
            show_date(r)

    def __show_by_table(self) -> None:
        ''' show results by table '''

        def date_for_table(dd: date) -> str:
            ''' format date for table '''
            return dd.strftime("%b %d")

        logd = self.logd
        if not USE_RICH:
            logd('[ERROR] rich module is not available, cannot show as table')
            return
        table = Table(title="Black Fridays")
        table.add_column("Year", justify="right", style="cyan")
        table.add_column("Date", justify="left", style="magenta")
        for y in self.years:
            shown_y = None
            if y in self.dicts:
                for dd in self.dicts[y]:
                    #logd(f'[DEBUG] {y} {shown_y}')
                    if shown_y is None or shown_y != y:
                        clr = get_year_color(y, target_year=-1)
                        table.add_row(f"[{clr}]{y}[/]", date_for_table(dd))
                        shown_y = y
                    else:
                        # if the year is already shown, just show the date
                        # without year
                        table.add_row('', date_for_table(dd))
            else:
                table.add_row(str(y), 'No black Friday found')
        console.print(table)

    def iterate_years(self):
        ''' iterate years '''
        self.results = []
        for y in self.years:
            ret = get_blackfridays_from_this_year(y)
            self.dicts[y] = ret
            self.results.extend(ret)

    @classmethod
    def run(cls, table: bool, logd: Callable[[Any], None] = do_nothing) -> None:
        ''' run demo only '''
        obj = cls(table, logd)
        obj.default_demo()

if USE_TYPER:
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    def main(
        values: Annotated[Optional[list[int]],
            typer.Argument(help="specify year")] = None,
        after: Annotated[int,
            typer.Option("--after", "-A", help="after nn year")] = 0,
        before: Annotated[int,
            typer.Option("--before", "-B", help="before nn year")] = 0,
        context: Annotated[int,
            typer.Option("--context", "-C", help="radius nn year, conflicts: after/before")
        ] = 0,
        verbose: Annotated[bool,
            typer.Option("--verbose", "-v", help="enable verbose mode")] = False,
        table: Annotated[bool,
            typer.Option("--table", "-t", help="show results as table")] = False,
        demo: Annotated[bool,
            typer.Option("--demo", "-D", help="run the demo")] = False,
    ) -> None:
        '''
        If no option is specified, run the default test. If available, color will
        refelct: red for specified year, green is the current year, yellow is both.
        '''
        logd = do_nothing
        if verbose:
            if USE_RICH:
                logd = consolelog
            else:
                logd = print
            logd('[DEBUG] debug mode enabled')
        if demo or values is None:
            logd('[INFO] run the demo')
            Solution.run(table, logd)
            return
        for y in values:
            obj = Solution(table, logd)
            obj.prepare_list_and_run(y,after=after,before=before,context=context)
            print()

def run_demo() -> None:
    ''' run the demo '''
    if len(sys.argv) > 1:
        print('[WARN] module typer not installed, no arguments supported, run the demo only')
    print('[INFO] run the demo')
    Solution.run(table=False, logd=do_nothing)

if __name__ == '__main__':
    if USE_TYPER:
        typer.run(main)
    else:
        run_demo()
