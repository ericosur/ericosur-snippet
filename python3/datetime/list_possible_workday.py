#!/usr/bin/env python3
#coding: utf-8

'''
given yyyy-mm, and output the workdays of this month

Usage for example:
py list_possible_workday.py 2024-11

output:
2024-11-01
2024-11-02
...
2024-11-29

If holidays.json is available, it will exclude the holidays.

the format of holidays.json is like this:
{
    "holidays_2024": [
        {"date": "2024-01-01", "name": "New Year's Day"}
    ],
    "holidays_2025": [
        {"date": "2025-01-01", "name": "New Year's Day"}
    ]
}

'''

import json
import os
import sys
from datetime import date, datetime, timedelta
from typing import Union, Annotated, Any, Callable, Optional
try:
    import typer
    USE_TYPER = True
except ImportError:
    print('[WARN] typer not found, please install it with "pip install typer"')
    print('[WARN] no CLI options available')
    USE_TYPER = False

# try:
#     from loguru import logger
#     _logd = logger.debug
# except ImportError:
#     _logd = print

try:
    from rich.console import Console
    console = Console()
    _logd = console.log
except ImportError:
    _logd = print

try:
    from nothing import do_nothing
except ImportError:
    print('[WARN] no module nothing, please check the module')
    sys.exit(1)

def get_thisyear() -> int:
    ''' return current year '''
    return datetime.now().year

def print_stderr(*_args: Any, **_kwargs: Any) -> None:
    ''' print to stderr '''
    print(*_args, file=sys.stderr, **_kwargs)

class CollectWeekday():
    ''' collect workdays '''
    HOLIDAYS_JSON = 'holidays.json'

    def __init__(self):
        self.results = []
        self.holidays = {}
        self.excluded_days = []
        self.logd = do_nothing  # default log function
        self.datafile = self.__set_datafile()

    def __set_datafile(self) -> str:
        ''' set data file '''
        # default value
        logd = self.logd
        ret = self.HOLIDAYS_JSON
        home = os.environ.get('HOME')
        private_path = os.path.join(home, 'Private', self.HOLIDAYS_JSON)
        if os.path.isfile(private_path):
            ret = private_path
            logd(f'[INFO] using private data file: {ret}')
        return ret

    def load_holidays(self, the_year: int, jsonfile: str = HOLIDAYS_JSON) -> None:
        ''' load holidays from json file with specified year '''
        logd = self.logd
        # load holidays from json file
        try:
            logd(f'[INFO] load holidays from: {jsonfile}')
            logd(f'[INFO] load_holidays for year: {the_year}')
            with open(jsonfile, 'rt', encoding='UTF-8') as fobj:
                self.holidays = json.load(fobj)
        except FileNotFoundError:
            # no holidays data file, will not terminate
            print(f'[ERROR] holidays file not found: {jsonfile}')

        self.excluded_days = self.collect_holidays(the_year)
        logd(f'size of excluded_days: {len(self.excluded_days)}')
        logd(self.excluded_days)

    def collect_holidays(self, year: int) -> list:
        ''' collect holidays for a specific year '''
        logd = self.logd
        logd(f'[INFO] collect_holidays, year={year}')
        Y = f'holidays_{year}'
        res = []
        if Y not in self.holidays:
            # complain but not terminate
            print(f'[WARN] no holidays found for year {year}')
        else:
            for y in self.holidays[Y]:
                d = y.get('date')
                # transaform string to date object
                if d:
                    d = datetime.strptime(d, "%Y-%m-%d").date()
                res.append(d)
        return res

    def show_holidays(self, this_year: int = 0) -> None:
        ''' show holidays '''
        if this_year <= 0:
            this_year = get_thisyear()
        logd = self.logd
        logd(f'[INFO] show_holidays for year={this_year}')
        self.load_holidays(this_year, self.datafile)
        if not self.holidays:
            print('[ERROR] no holidays found')
            return
        Y = f'holidays_{this_year}'
        logd(f'{Y}:')
        if Y not in self.holidays:
            print(f'[ERROR] no holidays found for year {this_year}')
            return

        the_holidays = self.holidays[Y]
        for d in the_holidays:
            print(f'  {d["date"]}: {d["name"]}')

    def set_logd(self, log: Callable[[Any], None]) -> None:
        ''' set log function '''
        self.logd = log

    def collect_workday(self, the_d: datetime) -> None:
        ''' list workdays '''
        def is_workday(d: date) -> bool:
            w = d.isoweekday()
            return 1 <= w <= 5  # Mon to Fri

        logd = self.logd
        logd(f'{the_d=}')
        offset = timedelta(days=1)
        self.load_holidays(the_d.year, self.datafile)
        # recompose a date object, due to class date has strftime()
        # but datetime has no such function
        d = date(the_d.year, the_d.month, the_d.day)
        while the_d.month == d.month:
            # only check workdays in this month
            if is_workday(d):
                if d in self.excluded_days:
                    logd(f'[DEBUG] {d} is excluded')
                else:
                    self.results.append(d.strftime("%Y-%m-%d"))
            # go to next day
            d += offset
        logd(f'[DEBUG] got {len(self.results)} workdays for {the_d.year}/{the_d.month}')

    def output_to_file(self, outf: str) -> None:
        ''' output to file '''
        with open(outf, "wt", encoding="UTF-8") as fobj:
            self.dump_results(fobj=fobj)

    def dump_results(self, fobj=sys.stdout) -> None:
        ''' dump results, one item per line'''
        print_stderr(f'# no of items: {len(self.results)}')
        for i in self.results:
            print(i, file=fobj)

    def run_default(self) -> None:
        ''' run default, without CLI options '''
        td = date.today()
        default_yymm = td.strftime("%Y-%m")
        print(f'[INFO] use default value: {default_yymm}')
        self.collect_workday(td)
        self.dump_results()

# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
    if USE_TYPER:
        def main(self,
            # input like: "1970-01"
            yyyymm: Annotated[Union[datetime, None],
                typer.Argument(help="specify a YYYY-mm date, the dd will be ignored",
                        formats=["%Y-%m", "%Y-%m-%d"]),] = None,
            # output file name
            outf: Annotated[Union[str, None],
                typer.Option("--out", "-o", help="output file name")] = None,
            # show holidays for a specific year, default current year
            vacation: Annotated[bool, typer.Option("-v", "--vacation", help="Show vacation info, default is current year")] = False,
            vacation_year: Annotated[Optional[int], typer.Option("--vacation-year", help="Must specify the year")] = None,
            # debug mode
            debug: Annotated[bool,
                typer.Option("--debug", "-d", help="turn on debug", is_flag=True)] = False,
        ) -> None:
            '''
            List the dates of which weekday are between Monday to Friday.
            For example, ```python this_script.py 2024-12```

            same as the following:

            $ apt-get install dateutils

            $ dateutils.dseq 2024-12-1 2024-12-31 --skip sat,sun
            '''
            logd = _logd if debug else do_nothing
            self.set_logd(logd)
            # show vacation days and exit
            if vacation:
                this_year = get_thisyear()
                logd(f'[INFO] will show holidays this year: {this_year}')
                self.show_holidays(this_year)
                return
            if vacation_year:
                yy = vacation_year
                logd(f'[INFO] will show holidays in year: {yy}')
                self.show_holidays(yy)
                return

            if yyyymm is None:
                print('[INFO] You need specify some date (yyyy-mm)\n  Get some help, use "--help"')
                return
            self.collect_workday(yyyymm)
            if outf:
                self.output_to_file(outf)
            else:
                self.dump_results()

if __name__ == "__main__":
    obj = CollectWeekday()
    if USE_TYPER:
        typer.run(obj.main)
    else:
        obj.run_default()
