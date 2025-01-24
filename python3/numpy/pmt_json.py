#!/usr/bin/env python3
#coding: utf-8

'''
numpy_financial.pmt

https://numpy.org/numpy-financial/latest/index.html#functions
'''

import sys
from typing import Annotated
import numpy_financial as npf  # type: ignore[import]
from pydantic import BaseModel
try:
    import typer
    USE_TYPER = True
except ImportError as e:
    USE_TYPER = False
    print('[INFO] failed to load module **typer**, only run the demo')

sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from myutil import prt  # type: ignore[import]
from myutil import read_jsonfile  # type: ignore[import]

class Loan(BaseModel):
    ''' Loan '''
    rate: float
    nper: int
    pv: float

def calc_and_show(val: Loan) -> None:
    ''' calc pmt '''
    prt(f'rate: {val.rate*100:.4f}%')
    prt(f'nper: {val.nper}')
    prt(f'  PV: {val.pv:,.2f}')
    # Calculate the monthly payment
    payment = npf.pmt(val.rate/12, val.nper, val.pv)
    prt(f'monthly payment: {payment:,.2f}')

def main(
        conf: Annotated[str, typer.Argument(help="json file with loan data")] = 'pmt.json'
):
    ''' use numpy_financial.pmt to calculate the monthly payment '''
    prt('[blue]if no arugment is given, the default values will be used[/]')
    d = read_jsonfile(conf)
    rate = d.get('rate', 2.62)
    nper = d.get('nper', 84)
    pv = d.get('pv', 2_150_000)
    loan = Loan(rate=rate/100.0, nper=nper, pv=pv)
    calc_and_show(loan)

if __name__ == "__main__":
    typer.run(main)
