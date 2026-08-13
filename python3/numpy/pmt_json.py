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


try:
    from numpy_common import prt  # type: ignore[import]

    from myutil import read_jsonfile  # type: ignore[import]
except ImportError as e:
    print('failed to load module', e)
    sys.exit(1)


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

    prt(f'{"rate":<28}: {val.rate*100:.4f}%')
    prt(f'{"nper":<28}: {val.nper}')
    prt(f'{"PV":<28}: {val.pv:,.2f}')
    # numpy_financial.pmt returns negative cash outflow for repayment.
    payment = abs(npf.pmt(val.rate/12, val.nper, val.pv))
    payment_rounded = int(Decimal(str(payment)).quantize(Decimal(1), rounding=ROUND_HALF_UP))
    prt(f'{"monthly payment (rounded)":<28}: {payment_rounded:,d}')


def main(
    conf: str = 'pmt.json'
):
    ''' use numpy_financial.pmt to calculate the monthly payment '''
    prt('[blue]if no arugment is given, the default values will be used[/]')
    d = read_jsonfile(conf)
    rate = d.get('rate', 2.62)
    nper = d.get('nper', 84)
    pv = d.get('pv', 2_150_000)
    loan = Loan(rate=rate/100.0, nper=nper, pv=pv)
    calc_and_show(loan)


app = None
if USE_TYPER:
    app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
    app.command()(main)


if __name__ == "__main__":
    if USE_TYPER and app is not None:
        app()
    else:
        parser = argparse.ArgumentParser(
            description='use numpy_financial.pmt to calculate the monthly payment'
        )
        parser.add_argument(
            '--conf',
            '-c',
            default='pmt.json',
            help='json file with loan data',
        )
        args = parser.parse_args()
        main(args.conf)
