# coding: utf-8

'''
return home directory or '.' if no HOME env
'''

import os

def get_home() -> str:
    ''' get home '''
    _h = os.getenv('HOME')
    home = _h if _h else '.'
    return home

if __name__ == '__main__':
    print('provides get_home():', get_home())
