#!/usr/bin/env python3
# coding: utf-8

'''
prompt dialog of pythonista
'''

# for pythonista
#import clipboard
HAS_CONSOLE_MODULE = False
try:
    import console  # type: ignore[import]
    HAS_CONSOLE_MODULE = True
except ImportError:
    print('[WARN] No console module of pythonista, will run normal CLI')


def prompt_input(msg: str):
    ''' prompt, return 0 if invalid '''
    if not HAS_CONSOLE_MODULE:
        return 0

    ret = console.input_alert(msg)
    val = 0
    try:
        val = int(ret)
        if val <= 0:
            raise ValueError
    except ValueError:
        print(f'{ret} not a number')
        print('invalid number, use random number:', val)
    return val

def prompt_alert(msg: str):
    ''' alert '''
    if not HAS_CONSOLE_MODULE:
        print(msg)
    else:
        console.alert(msg)

def has_console():
    ''' return true if console available '''
    return HAS_CONSOLE_MODULE

def main():
    ''' main '''
    print()
    print('Has console module of pythonista? ', end='')
    if has_console():
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
