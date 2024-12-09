#!/usr/bin/env python3
# coding: utf-8

'''
Anonymous Gregorian algorithm
https://en.wikipedia.org/wiki/Date_of_Easter

http://www.oremus.org/liturgy/etc/ktf/app/easter.html
'''

# datetime.datetime, datetime.date
from datetime import date
from typing import List, Optional
from typing_extensions import Annotated
try:
    import typer
    USE_TYPER = True
except:
    USE_TYPER = False
    print('warn: failed to import typer, only demo, no CLI...')

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
from be_prepared import get_thisyear, prepare_values, get_year_color

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

if USE_TYPER:
    def main(values: Annotated[Optional[List[int]],
                                        typer.Argument(help="specify year")] = None,
            after: Annotated[int,
                                typer.Option("--after", "-A", help="after nn year")] = 0,
            before: Annotated[int,
                                typer.Option("--before", "-B", help="before nn year")] = 0,
            context: Annotated[int, typer.Option("--context", "-C",
                                        help="radius nn year, conflicts: after/before")] = 0,
            ) -> None:
        '''
        If no option is specified, run the default test. If available, color will
        refelct: red for specified year, green is the current year, yellow is both
        '''

        # if no value is specified, if options available, use them
        if values is None:
            if context == 0:
                context = 2
            years = prepare_values(get_thisyear(), after=after, before=before, radius=context)
            for y in years:
                show_result(y)
            return
        for v in values:
            years = prepare_values(v, after=after, before=before, radius=context)
            for y in years:
                show_result(y, target=v)

def show_result(y, target=get_thisyear()):
    ''' _show '''
    res = calculate_easter(y)
    if USE_RICH:
        clr = get_year_color(y, target_year=target)
        rprint(f'[{clr}]{res}')
    else:
        print(res)

def run_default_demo():
    ''' default demo '''
    years = prepare_values(get_thisyear(), after=4)
    for y in years:
        show_result(y)

if __name__ == '__main__':
    if USE_TYPER:
        typer.run(main)
    else:
        run_default_demo()
