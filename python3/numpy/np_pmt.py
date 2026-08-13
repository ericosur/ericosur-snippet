#!/usr/bin/env python3

'''
numpy_financial.pmt

https://numpy.org/numpy-financial/latest/index.html#functions
'''

import argparse
import sys
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Any

typer: Any = None
try:
    import typer
    USE_TYPER = True
except ImportError:
    USE_TYPER = False
    print('[INFO] failed to load module **typer**, only run the demo')

from numpy_common import prt  # type: ignore[import]


@dataclass
class Loan:
    ''' Loan '''
    rate: float
    nper: int
    pv: float

def calc_and_show(val: Loan) -> None:
    ''' calc pmt '''
    try:
        import numpy_financial as npf  # type: ignore[import]
    except ImportError as e:
        print('failed to load module', e)
        sys.exit(1)

    prt(f'rate: {val.rate*100:.4f}%')
    prt(f'nper: {val.nper}')
    prt(f'  PV: {val.pv:,.2f}')
    # numpy_financial.pmt returns negative cash outflow for repayment.
    payment = abs(npf.pmt(val.rate/12, val.nper, val.pv))
    payment_rounded = int(Decimal(str(payment)).quantize(Decimal(1), rounding=ROUND_HALF_UP))
    prt(f'monthly payment (rounded): {payment_rounded:,d}')

def main(
    rate: float = 9.0,
    nper: int = 84,
    pv: float = 2_000_000,
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


app = None
if USE_TYPER:
    app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
    app.command()(main)

if __name__ == "__main__":
    if not USE_TYPER:
        parser = argparse.ArgumentParser(
            description='use numpy_financial.pmt to calculate the monthly payment'
        )
        parser.add_argument('rate', nargs='?', type=float, default=2.62, help='yearly rate in percentage')
        parser.add_argument('nper', nargs='?', type=int, default=84, help='number of periods')
        parser.add_argument('pv', nargs='?', type=float, default=2_150_000, help='present value')
        args = parser.parse_args()
        main(rate=args.rate, nper=args.nper, pv=args.pv)
    else:
        assert app is not None
        app()
