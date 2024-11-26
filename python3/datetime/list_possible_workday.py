#!/usr/bin/python
#coding: utf-8

'''
given yyyy-mm, and output the workdays of this month

for example: 2024-11
output:
2024-11-01
2024-11-02
...
2024-11-29
'''

import sys
from datetime import date, datetime, timedelta
from typing_extensions import Annotated
import typer
from loguru import logger

# pylint: disable=unused-argument
def do_nothing(*args) -> None:
    ''' do nothing '''
    return

class CollectWeekday():
    ''' collect workdays '''
    def __init__(self):
        self.results = []

    def collect_workday(self, the_d: datetime, log):
        ''' list workdays '''
        def is_workday(d: date):
            w = d.isoweekday()
            return 1 <= w <= 5  # Mon to Fri

        logd = log
        logd(f'{the_d=}')
        offset = timedelta(days=1)
        # recompose a date object, due to class date has strftime()
        # but datetime has no such function
        d = date(the_d.year, the_d.month, the_d.day)
        while the_d.month == d.month:
            if is_workday(d):
                self.results.append(d.strftime("%Y-%m-%d"))
            d += offset

    def output_to_file(self, outf: str):
        ''' output to file '''
        with open(outf, "wt", encoding="UTF-8") as fobj:
            self.dump_results(fobj=fobj)

    def dump_results(self, fobj=sys.stdout):
        ''' dump results '''
        for i in self.results:
            print(i, file=fobj)

    def main(self,
        yyyymm: Annotated[datetime, typer.Argument(help="specify a YYYY-mm date, "
                                                   "the dd will be ignored",
                    formats=["%Y-%m", "%Y-%m-%d"]),] = None, #"1970-01",
        outf: Annotated[str, typer.Option("--out", "-o", help="output file nanme")]
                    = None, # output file name
        debug: Annotated[bool, typer.Option("--debug", help="turn on debug")] = False,
    ):
        '''
        List the dates of which weekday are between Monday to Friday.
        For example, ```python this_script.py 2024-12```

        same as the following:

        $ apt-get install dateutils

        $ dateutils.dseq 2024-12-1 2024-12-31 --skip sat,sun
        '''
        logd = do_nothing
        if debug:
            logd = logger.debug
        if yyyymm is None:
            print('[INFO] You need specify some date. Get some help, use "--help"')
            return

        self.collect_workday(yyyymm, log=logd)
        if outf:
            self.output_to_file(outf)
        else:
            self.dump_results()

if __name__ == "__main__":
    obj = CollectWeekday()
    typer.run(obj.main)
