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
except ImportError:
    USE_TYPER = False
    print('[INFO] failed to load module **typer**, only run the demo')

sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from myutil import prt  # type: ignore[import]

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
        rate: Annotated[float, typer.Argument(help="yearly rate in percentage")] = 2.62,
        nper: Annotated[int, typer.Argument(help="number of periods")] = 84,
        pv: Annotated[float, typer.Argument(help="present value")] = 2_150_000,
):
    ''' use numpy_financial.pmt to calculate the monthly payment '''
    prt('[blue]if no arugment is given, the default values will be used[/]')
    loan = Loan(rate=rate/100.0, nper=nper, pv=pv)
    calc_and_show(loan)

def demo():
    ''' main '''
    loans = [
        Loan(rate=2.2/100, nper=16*12, pv=2_000_000),
        Loan(rate=2.62/100, nper=7*12, pv=2_150_000),
    ]

    for idx, c in enumerate(loans):
        prt(f'loan case: {idx+1}')
        calc_and_show(c)
        prt('-'*60)

if __name__ == "__main__":
    if not USE_TYPER:
        demo()
    else:
        typer.run(main)
