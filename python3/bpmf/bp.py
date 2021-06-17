#!/usr/bin/python3
# coding: utf-8

'''
given e04
output 幹
'''

import argparse
import re
import os




class Solution():
    def __init__(self):
        self.data = 'bpmf.txt'
        self.binf = 'bp.txt'
        self.mydict = dict()
        self.debug = False
        self.ime = list(',-./0123456789;abcdefghijklmnopqrstuvwxyz')
        self.load_table()

    def load_table(self):
        ''' load table from file '''
        cnt = 0
        if os.path.exists(self.binf):
            self.data = self.binf
        with open(self.data, "rt") as f:
            for ln in f.readlines():
                cnt += 1
                m = re.search(r'^(\S+) (\S+)$', ln)
                if m:
                    if self.debug:
                        print('{} <=> {}'.format(m[1], m[2]))
                    if not m[1] in self.mydict:
                        self.mydict[m[1]] = m[2]
        if self.debug:
            print('cnt:', cnt)
            print('len:', len(self.mydict))
        if os.path.exists(self.binf):
            print('{} exists'.format(self.binf))
        else:
            with open(self.binf, "wt") as fo:
                for kk in self.mydict:
                    print('{} {}'.format(kk, self.mydict[kk]), file=fo)

    def test(self):
        ''' test '''
        tt = ['ji3', '1j4', 'cjo4', 'gji ', '5j/ ', 'jp6']
        self.lookup_list(tt)

    def lookup_list(self, clist):
        ''' given list return chinese characters '''
        for t in clist:
            r = self.lookup(t)
            if r:
                print(r, end='')
            else:
                print(t, end='')
        print()

    def lookup(self, key):
        ''' look up in table '''
        # 3, 4, 6, 7 and space may split a character
        key = key.strip()
        if key in self.mydict:
            return self.mydict[key]
        else:
            return None

    def parse_chars(self, inp):
        ''' parse '''
        s = ''
        ll = list()
        for cc in list(inp):
            if not cc in self.ime:
                ll.append(s)
                s = ''
                continue
            if cc in ['3','4','6','7',' ']:
                s = s + cc
                if self.debug: print('append:', s)
                ll.append(s)
                s = ''
            else:
                s = s + cc
        #print(ll)
        return ll

    def demo(self):
        ''' demo '''
        #self.test()
        t = 'ji31j4cjo4gji 5j/ jp6'
        self.run(t)

    def run(self, sentence):
        ll = self.parse_chars(sentence)
        self.lookup_list(ll)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='brief description for this script')
    parser.add_argument("strings", metavar='str', type=str, nargs='*',
        help="show these strings")
    parser.add_argument("-d", "--demo", help="demo", action='store_true')

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    if args.demo:
        foo = Solution()
        foo.demo()
    elif len(args.strings) == 0:
        parser.print_help()
    else:
        #print(args.strings)
        foo = Solution()
        for s in args.strings:
            foo.run(s)


if __name__ == '__main__':
    main()
