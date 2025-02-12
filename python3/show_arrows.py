#!/usr/bin/env python3
# coding: utf-8

'''
use rich to show arrow characters
'''

from typing import Annotated
import typer
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console

def no_rich(is_csv: bool, reverse: bool = False):
    ''' with rich '''
    for c in range(0x2190,0x21FF+1):
        A = f'"{c:04X}"' if is_csv else f'{c:04X}'
        B = f'"{chr(c)}"' if is_csv else f'{chr(c)}'
        if reverse:
            A, B = B, A
        if is_csv:
            print(f'{A},{B}')
        else:
            print(f'{A} {B}')

def arrows_in_box():
    ''' arrows '''
    all_arrows = Columns(
        [f'{c:04X} {chr(c)}' for c in range(0x2190,0x21FF+1)]
    )
    console = Console()
    p = Panel(all_arrows, title="arrows", border_style="blue")
    console.print(p)

def main(
    one: Annotated[bool, typer.Option("--one", "-O",
                                      help="One char each line, unicode then char")] = False,
    rev: Annotated[bool, typer.Option("--reverse", "-R",
                                      help="One char each line, char first, then Unicode")] = False,
    csv: Annotated[bool, typer.Option("--csv", "-C",
                                      help="Only works while -O or -R")] = False,
):
    ''' main '''
    if one:
        no_rich(csv, reverse=rev)
        return
    if rev:
        no_rich(csv, reverse=rev)
        return
    arrows_in_box()

if __name__ == '__main__':
    typer.run(main)
