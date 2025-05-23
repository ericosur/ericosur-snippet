#!/usr/bin/env python3
# coding: utf-8

'''
alpha beta charlie
https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

'''

import argparse
import sys
from random import sample

sys.path.insert(0, "../")
sys.path.insert(0, "../../")
from myutil import read_from_stdin  # type: ignore[import]

class AlphaBravoCharlie():
    ''' NATO alpha bravo charlie '''
    nato_str = '''
    Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India
    Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo
    Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu
    '''

    def __init__(self):
        self.abc = self.nato_str.strip()
        self.alpha_arr = self.__get_arr()
        # uppercase capital dict
        self.alpha_dict = self.__get_dict()

    def get_arr(self) -> list[str]:
        ''' return list of 'Alpha', 'Bravo', 'Charlie' '''
        return self.alpha_arr

    def get_dict(self) -> dict[str, str]:
        ''' return dict of {'A': 'Alpha', 'B': 'Bravo', ...} '''
        return self.alpha_dict

    def __str__(self):
        ''' abc in capital words '''
        return self.nato_str

    def __get_arr(self) -> list[str]:
        ''' get_arr '''
        return self.abc.split()

    def __get_dict(self) -> dict[str,str]:
        ''' get dict '''
        d = {}
        for ww in self.alpha_arr:
            cap = ww[0]
            d[cap] = ww
        return d

    def translate(self, s: str) -> None:
        ''' translate '''
        for c in list(s.upper()):
            if c in self.alpha_dict:
                print(self.alpha_dict[c], end=' ')
        print()

    def random_pick(self, n: int = 3) -> None:
        ''' random_pick several items '''
        arr = sample(self.alpha_arr, n)
        for c in arr:
            print(c)

def process_args(args: list) -> None:
    ''' process_args '''
    abc = AlphaBravoCharlie()
    if args == []:
        print('>>>>> (demo) random pick:', file=sys.stderr)
        abc.random_pick(3)
        print()
        args.append('hello')
        args.append('world')

    for e in args:
        print('>>>>> translate:', e, file=sys.stderr)
        abc.translate(e)

def main():
    ''' main use argparse to handle cli args '''
    parser = argparse.ArgumentParser(description='convert string into NATO call name',
        epilog="echo 'wtf' | PROG -s")
    parser.add_argument("-s", "--stdin", dest='readFromStdin', action='store_true',
        help='read from STDIN')
    parser.add_argument("arg", nargs='*', default=None)
    args = parser.parse_args()
    #print(args)
    if args.readFromStdin:
        print('[INFO] --help or use Ctrl-D to end of stdin', file=sys.stderr)
        read_from_stdin(process_args)
    else:
        process_args(args.arg)

if __name__ == '__main__':
    main()
