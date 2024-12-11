#!/usr/bin/env python3
# coding: utf-8

'''
prt wraps rich.print or built-in print
'''

try:
    from rich import print as rprint
    USE_RICH = True
except ImportError:
    USE_RICH = False

prt = rprint if USE_RICH else print
