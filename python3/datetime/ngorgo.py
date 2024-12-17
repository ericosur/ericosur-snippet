#!/usr/bin/env python
# coding: utf-8

'''
locate latest and recommend to refresh dl or not

try:
    dt = datetime.strptime(ds, '%a, %d %m %y %H:%M:%S %z')
    print(dt)
except ValueError:
    pass

'''

import argparse
import re
import os
import sys
from datetime import date, timedelta

SUCCESS = 0
FILENOTFOUND = 1
NOTOLDENOUGH = 2
CANNOTPARSE = 3

class Solution():
    ''' class to parse and action '''
    TS = 'latest.txt'
    MINDIFF = 5
    months = ['Nul', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    patterns = [
        # 西元2023年12月15日 (週五) 13時57分07秒 CST
        r'^西元(\d{4})年(\d+)月(\d+)日.*$',
        # Tue, 12 Dec 2023 14:47:55 +0800
        r'^\w+,\s+(\d+)\s+(\w+)\s+(\d+) \d+:\d+:\d+ \+\d+$',
        # Tue Dec 12 15:10:30 CST 2023
        r'^\w+\s+(\w+)\s+(\d+)\s+\d+:\d+:\d+ \w+ (\d+)$',
    ]

    def __init__(self):
        self.inputfn = ''
        self.lastdate = None
        self.offset = timedelta(days=Solution.MINDIFF)
        self.quiet = False
        self.verbose = False

    def set_quiet(self, yesno):
        ''' set quiet '''
        self.quiet = yesno

    def set_stampfile(self, p):
        ''' set path of stamp file '''
        if not self.quiet:
            print('set_stampfile:', p)
        self.inputfn = p

    def get_thelastine(self):
        ''' get the last line with content of a file '''
        if self.verbose:
            print(f'parsing: {self.inputfn}')
        lastline = None
        with open(self.inputfn, 'rt', encoding='UTF-8') as fobj:
            for l in fobj.readlines():
                ln = l.strip()
                if len(ln) > 0:
                    lastline = ln
        return lastline

    def parse_date_format1(self, ds):
        ''' parse date format: 西元2023年12月25日 '''
        m = re.match(Solution.patterns[0], ds)
        if m:
            # m[1]: year, m[2]: month, m[3]: day
            self.lastdate = date(year=int(m[1]),month=int(m[2]),day=int(m[3]))
            #print(self.lastdate)
            return self.lastdate

        #print('[warn] cannot parse with format1...')
        return None


    def compose_date_obj(self, y: str, m: str, d: str):
        ''' return a date obj '''
        yyyy = int(y)
        mm = Solution.months.index(m)
        dd = int(d)
        self.lastdate = date(year=yyyy,month=mm,day=dd)

    def parse_date_format2(self, ds):
        ''' parse date in format 2 '''
        #print('parse date in format 2...')
        m = re.match(Solution.patterns[1], ds)
        if m:
            # m[1]: dd, m[2]: month name, m[3]: yyyy
            self.compose_date_obj(m[3], m[2], m[1])
        else:
            m = re.match(Solution.patterns[2], ds)
            if m is None:
                return None

            # m[1]: month name, m[2]: dd, m[3]: yyyy
            self.compose_date_obj(m[3], m[1], m[2])

        #print(self.lastdate)
        return self.lastdate


    def parse_stampfile(self):
        ''' parse stamp file '''
        if not os.path.exists(self.inputfn):
            print('[FAIL] file not found:', self.inputfn)
            sys.exit(FILENOTFOUND)
        ln = self.get_thelastine()
        #print(ln)
        still_try = True
        try_count = 0
        self.lastdate = None
        while still_try and try_count < 2:
            d = self.parse_date_format1(ln)
            try_count += 1
            if d:
                break
            d = self.parse_date_format2(ln)
            try_count += 1
            if d:
                break

    def show_msg(self, msg):
        ''' show message '''
        if not self.quiet:
            print(msg)

    def action(self):
        ''' action '''
        #self.show_msg('action')
        self.parse_stampfile()
        if self.lastdate:
            if self.lastdate >= date.today() - self.offset:
                self.show_msg(f'[INFO] {self.lastdate} rather new, no need to bother')
                sys.exit(NOTOLDENOUGH)
            else:
                self.show_msg(f'[INFO] {self.lastdate} old enough, ok to refresh')
                return
        self.show_msg('[fail] cannot parse the last date')
        sys.exit(CANNOTPARSE)


    @classmethod
    def run(cls, argv=None):
        ''' run me '''
        obj = cls()
        obj.set_stampfile(argv)
        obj.action()

def start_solution(files, isquiet):
    ''' control flow '''
    # if not isquiet:
    #     print('files:', files)
    obj = Solution()
    obj.set_quiet(isquiet)

    if len(files) < 1:
        # if not isquiet:
        #     print('give a default value...')
        files.append(os.path.join('.', Solution.TS))

    for f in files:
        obj.set_stampfile(f)
        obj.action()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='from given latest.txt, tell if refresh or not')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("files", metavar='fn', type=str, nargs='*',
        help="file1 file2 file3 ...")
    #parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    parser.add_argument("-q", "--quiet", action='store_true', default=False,
        help='quiet, use return code to judge')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    # define the required args
    #requiredNamed = parser.add_argument_group('required named arguments')
    #requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    start_solution(args.files, args.quiet)

    # to show help message directly
    #parser.print_help()

if __name__ == '__main__':
    main()
