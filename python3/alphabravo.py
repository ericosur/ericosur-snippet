#!/usr/bin/env python3
# coding: utf-8

'''
alpha beta charlie
https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

'''

import sys
from random import sample
from myutil import read_from_stdin


class AlphaBravoCharlie():
    ''' NATO alpha bravo charlie '''
    def __init__(self):
        self.abc = AlphaBravoCharlie.get_abc()
        self.alpha_arr = self.__get_arr__()
        # uppercase capital dict
        self.alpha_dict = self.__get_dict__()

    def get_arr(self):
        ''' return list of 'Alpha', 'Bravo', 'Charlie' '''
        return self.alpha_arr

    def get_dict(self):
        ''' return dict of {'A': 'Alpha', 'B': 'Bravo', ...} '''
        return self.alpha_dict

    @staticmethod
    def get_abc():
        ''' abc in capital words '''
        s = '''
        Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India
        Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo
        Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu
        '''.strip()
        return s

    def __get_arr__(self):
        ''' get_arr '''
        return self.abc.split()

    def __get_dict__(self):
        ''' get dict '''
        d = dict()
        for ww in self.alpha_arr:
            cap = ww[0]
            d[cap] = ww
        return d

    def translate(self, s: str):
        ''' translate '''
        for c in list(s.upper()):
            if c in self.alpha_dict:
                print(self.alpha_dict[c], end=' ')
        print()

    def random_pick(self, n: int = 3):
        ''' random_pick several items '''
        arr = sample(self.alpha_arr, n)
        for c in arr:
            print(c)


def main(args: list):
    ''' main '''
    abc = AlphaBravoCharlie()

    if args == []:
        print('\nrandom pick:')
        abc.random_pick(3)
        print()
        args.append('hello')
        args.append('world')

    for e in args:
        print('>>>>> translate:', e)
        abc.translate(e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            read_from_stdin(main)
        else:
            main(sys.argv[1:])
    else:
        print('For stdin: use "{} -"'.format(sys.argv[0]))
        print('OR "alphabeta.py [arg1] [arg2] ..."')
        print('\nDEMO: random pick & hello world')
        main([])
