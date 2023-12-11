#!/usr/bin/python3
# coding: utf-8

'''
try to search in EMOJI, need
_emoji.py
'''

import argparse
import re

from _emoji import EMOJI


class Solution():
    ''' solution '''
    def __init__(self, querys):
        ''' init '''
        self.size = len(EMOJI)
        self.keys = EMOJI.keys()
        self.querys = querys

    def __str__(self):
        ''' str '''
        return f'emoji size: {self.size}'

    def query(self, q):
        ''' query '''
        ans_dict = {}

        if q in self.keys:
            ans_dict[q] = EMOJI[q]
        else:
            # try partial match
            for i in self.keys:
                m = re.search(q, i)
                if m:
                    ans_dict[i] = EMOJI[i]

        return ans_dict


    @staticmethod
    def show_result(r):
        ''' show result '''
        if not r:
            raise ValueError("no value")

        if len(r) == 0:
            print('not found')

        for k, v in sorted(r.items()):
            print(f'{k}: {v}')


    def test(self, q):
        ''' test '''
        r = self.query(q)
        if r:
            print(f"query: {q}")
            self.show_result(r)
        else:
            print("No such key exactly: ", q)
        print('--------------------')

    def action(self):
        ''' action '''
        print('action:')
        for q in self.querys:
            self.test(q)

def run_test():
    ''' run test '''
    querys = ['sand', 'note', 'boot']
    sol = Solution(querys)
    sol.action()

def main():
    ''' main '''

    # define argparse
    parser = argparse.ArgumentParser(description='find emoji from _emoji table')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("emo", metavar='emo', type=str, nargs='*',
        help="search keyword of emojis")
    parser.add_argument('-t', '--test', action='store_true', default=False,
        help='perform self test')

    args = parser.parse_args()

    if args.test:
        print('perform self test...')
        run_test()
        return

    if args.emo:
        sol = Solution(args.emo)
        sol.action()
        return

    print('no arguments specified, use "-h" to see the help, will run default function...\n')
    #parser.print_help()
    run_test()

if __name__ == '__main__':
    main()
