#!/usr/bin/python
#coding: UTF-8

'''
Use typer to call AlphaBravoCharlie translator
It's much easier than argparse
'''

#from typing import Optional
from typing_extensions import Annotated
import typer
from alphabravo import AlphaBravoCharlie

def main(name: Annotated[str,
                         typer.Argument(help="pass string to translate")]
                         = "Hello world"):
    '''
    call class AlphaBravoCharlie to translate
    '''
    obj = AlphaBravoCharlie()
    obj.translate(name)

if __name__ == "__main__":
    typer.run(main)
