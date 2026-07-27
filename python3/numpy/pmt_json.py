#!/usr/bin/env python3

'''
numpy_financial.pmt

https://numpy.org/numpy-financial/latest/index.html#functions
'''

import sys
from decimal import ROUND_HALF_UP, Decimal
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
from myutil import (
    prt,  # type: ignore[import]
    read_jsonfile,  # type: ignore[import]
)


class Loan(BaseModel):
    ''' Loan '''
    rate: float
    nper: int
    pv: float

def calc_and_show(val: Loan) -> None:
    ''' calc pmt '''
    prt(f'{"rate":<28}: {val.rate*100:.4f}%')
    prt(f'{"nper":<28}: {val.nper}')
    prt(f'{"PV":<28}: {val.pv:,.2f}')
    # numpy_financial.pmt returns negative cash outflow for repayment.
    payment = abs(npf.pmt(val.rate/12, val.nper, val.pv))
    payment_rounded = int(Decimal(str(payment)).quantize(Decimal(1), rounding=ROUND_HALF_UP))
    prt(f'{"monthly payment (rounded)":<28}: {payment_rounded:,d}')

def main(
        conf: Annotated[str, typer.Option(help="json file with loan data")] = 'pmt.json'
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
