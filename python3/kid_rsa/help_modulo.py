#!/usr/bin/env python3
# coding: utf-8

'''
pythonista script help to do m // n = q ... r
'''

from sta_prompt import prompt_input, prompt_alert, has_console

def run_this():
    ''' run this '''
    m = prompt_input('input m')
    n = prompt_input('input n')
    q = m // n
    r = m % n
    msg = '{} / {} = {} ... {}'.format(m, n, q, r)
    prompt_alert(msg)

if __name__ == '__main__':
    if has_console():
        run_this()
    else:
        print('This script is designed to run in pythonista')
