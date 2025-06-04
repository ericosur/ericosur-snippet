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
from typing import Union, Annotated, Any, Callable
import typer
from loguru import logger
from nothing import do_nothing

def get_thisyear() -> int:
    ''' return current year '''
    return datetime.now().year

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

    def load_holidays(self, jsonfile: str = HOLIDAYS_JSON) -> None:
        ''' load holidays from json file '''
        logd = self.logd
        # load holidays from json file
        try:
            logd(f'[INFO] load holidays from: {jsonfile}')
            with open(jsonfile, 'rt', encoding='UTF-8') as fobj:
                self.holidays = json.load(fobj)
        except FileNotFoundError:
            # no holidays data file, will not terminate
            print(f'[ERROR] holidays file not found: {jsonfile}')

        self.excluded_days = self.collect_holidays(get_thisyear())
        logd(f'size of excluded_days: {len(self.excluded_days)}')
        logd(self.excluded_days)

    def collect_holidays(self, year: int) -> list:
        ''' collect holidays for a specific year '''
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

    def show_holidays(self) -> None:
        ''' show holidays '''
        self.load_holidays(self.datafile)
        if not self.holidays:
            print('[ERROR] no holidays found')
            return
        Y = f'holidays_{get_thisyear()}'
        print(f'{Y}:')
        if Y in self.holidays:
            for d in self.holidays[Y]:
                print(d)
        else:
            print(f'[ERROR] no holidays found for year {Y}')

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
        self.load_holidays(self.datafile)
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
        logd(f'[DEBUG] collected {len(self.results)} workdays in {the_d.month} month')

    def output_to_file(self, outf: str) -> None:
        ''' output to file '''
        with open(outf, "wt", encoding="UTF-8") as fobj:
            self.dump_results(fobj=fobj)

    def dump_results(self, fobj=sys.stdout) -> None:
        ''' dump results, one item per line'''
        for i in self.results:
            print(i, file=fobj)

    def main(self,
        yyyymm: Annotated[Union[datetime, None], typer.Argument(help="specify a YYYY-mm date, "
                                                   "the dd will be ignored",
                    formats=["%Y-%m", "%Y-%m-%d"]),] = None, #"1970-01",
        outf: Annotated[Union[str, None], typer.Option("--out", "-o", help="output file nanme")]
                    = None, # output file name
        vacation: Annotated[bool, typer.Option("--vacation", "-v", help="show holidays")] = False,
        debug: Annotated[bool, typer.Option("--debug", "-d", help="turn on debug")] = False,
    ) -> None:
        '''
        List the dates of which weekday are between Monday to Friday.
        For example, ```python this_script.py 2024-12```

        same as the following:

        $ apt-get install dateutils

        $ dateutils.dseq 2024-12-1 2024-12-31 --skip sat,sun
        '''
        logd = logger.debug if debug else do_nothing
        self.set_logd(logd)
        if vacation:  # show vacation days and exit
            logd('[INFO] show vacation')
            self.show_holidays()
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
    typer.run(obj.main)

