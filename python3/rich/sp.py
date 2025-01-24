#!/usr/bin/env python3
#coding: UTF-8

'''
simple demo for rich.console
'''

from random import randint
from time import sleep
from rich.console import Console
from rich.spinner import SPINNERS
#from rich.text import Text

console = Console()
tasks = [f"task {n}" for n in range(6)]
prt = console.print

def get_dot() -> str:
    ''' return dots([2-12])?'''
    r = randint(1,12)
    if r == 1:
        return 'dots'
    return f'dots{r}'

def do_tasks():
    ''' do tasks '''
    #picked = choice(sorted(SPINNERS))
    sp_name = get_dot()
    with console.status("[bold green]Working on tasks...",
                        spinner=sp_name,
                        refresh_per_second=12.5) as _status:
        while tasks:
            task = tasks.pop(0)
            sleep(1.25)
            console.log(f"{task} complete")

def show_spinners():
    ''' show spinners'''
    with open('spinners.txt', "wt", encoding='UTF-8') as fobj:
        for sp_name in sorted(SPINNERS):
            print(sp_name, file=fobj)

if __name__ == "__main__":
    #show_spinners()
    do_tasks()
