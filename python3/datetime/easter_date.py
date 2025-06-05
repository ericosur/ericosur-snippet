#!/usr/bin/env python3
# coding: utf-8

'''
Anonymous Gregorian algorithm
https://en.wikipedia.org/wiki/Date_of_Easter

http://www.oremus.org/liturgy/etc/ktf/app/easter.html
'''

# datetime.datetime, datetime.date
from datetime import date
import sys
from typing import Optional, Annotated
try:
    import typer
    USE_TYPER = True
except ImportError:
    USE_TYPER = False
    print('warn: failed to import typer, only demo, no CLI...')
try:
    from rich import print as rprint
    from rich.console import Console
    from rich.table import Table
    USE_RICH = True
    console = Console()
    logd = console.log
except ImportError:
    USE_RICH = False
    logd = print
try:
    from be_prepared import get_thisyear, prepare_values, get_year_color
    #from nothing import do_nothing
except ImportError:
    print('cannot import necessary modules: be_prepared, nothing')
    sys.exit(1)

# ruff: noqa: E741
def calculate_easter(year: int) -> date:
    ''' Calculate the date of Easter Sunday for the given year '''
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    # Return the date of Easter Sunday as a datetime object
    return date(year, month, day)

class Solution():
    ''' Solution class for Easter date calculation '''
    def __init__(self, years: list[int], table: bool = False) -> None:
        ''' init '''
        self.results = []
        self.years = years
        self.use_table = table

    def __show_by_list(self) -> None:
        target = get_thisyear()
        for r in self.results:
            if USE_RICH:
                clr = get_year_color(r.year, target_year=target)
                rprint(f'[{clr}]{r}')
            else:
                print(r)

    def __show_by_table(self) -> None:
        ''' show results by table '''
        def date_for_table(dd: date) -> str:
            ''' format date for table '''
            return dd.strftime("%b %d")

        table = Table(title="Easter Dates", show_lines=True)
        table.add_column("Year", justify="right")
        table.add_column("Easter Date", justify="left")
        table.add_column("YYYY-MM-DD", justify="left")
        for r in self.results:
            clr = get_year_color(r.year, target_year=get_thisyear())
            mmdd = date_for_table(r)
            table.add_row(f"[{clr}]{r.year}[/]", f"[{clr}]{mmdd}[/]", f"[{clr}]{r}[/]")
        console.print(table)

    def show_results(self) -> None:
        ''' _show '''
        if self.use_table and USE_RICH:
            self.__show_by_table()
        else:
            logd(f'[INFO] found {len(self.results)} Easter dates')
            self.__show_by_list()

    def collect_results(self) -> None:
        ''' collect results from self.years '''
        for y in self.years:
            res = calculate_easter(y)
            self.results.append(res)

    @classmethod
    def run_with_options(cls, years: list[int], table: bool) -> None:
        '''
        run with options, if no options, use default demo
        '''
        obj = cls(years, table)
        obj.collect_results()
        obj.show_results()

    @classmethod
    def demo(cls) -> None:
        ''' default demo '''
        years = prepare_values(get_thisyear(), after=4)
        obj = cls(years)
        obj.collect_results()
        obj.show_results()

if USE_TYPER:
    def main(values: Annotated[Optional[list[int]],
                                        typer.Argument(help="specify year")] = None,
            after: Annotated[int,
                                typer.Option("--after", "-A", help="after nn year")] = 0,
            before: Annotated[int,
                                typer.Option("--before", "-B", help="before nn year")] = 0,
            context: Annotated[int, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = 0,
            table: Annotated[bool, typer.Option("--table", "-t", help="show results as table")] = False,
            ) -> None:
        '''
        If no option is specified, it will run demo. If available, color will
        refelct: red for specified year, green is the current year, yellow is both
        '''
        # if no value is specified, if options available, use them
        if values is None:
            if context == 0:
                if after != 0 or before != 0:
                    logd('[INFO] year not specified, apply this year')
                else:
                    logd('[WARN] context is not set, using default context of 2 years')
                    context = 2
            years = prepare_values(get_thisyear(), after=after, before=before, radius=context)
        else:
            years = []
            for v in values:
                ys = prepare_values(v, after=after, before=before, radius=context)
                years.extend(ys)
                years = list(set(years))  # remove duplicates
                years.sort() # sort years
        Solution.run_with_options(years, table)

if __name__ == '__main__':
    if USE_TYPER:
        typer.run(main)
    else:
        if len(sys.argv) > 1:
            print('[WARN] no arguments supported, running demo only')
        print('[INFO] running demo...')
        Solution.demo()
