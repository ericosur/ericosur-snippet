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

import re
import os
import sys
from datetime import date, timedelta

class Solution():
    ''' class to parse and action '''
    TS = 'latest.txt'
    MINDIFF = 4
    patterns = [
        r'^西元(\d{4})年(\d+)月(\d+)日.*$',
        r'^\w+, (\d+) (\w+) (\d+) \d+:\d+:\d+ \+\d+$'
    ]

    def __init__(self):
        self.inputfn = ''
        self.lastdate = None
        self.offset = timedelta(days=Solution.MINDIFF)

    def set_stampfile(self, p):
        ''' set path of stamp file '''
        self.inputfn = p

    def get_thelastine(self):
        ''' get the last line of a file '''
        print(self.inputfn)
        ret = None
        with open(self.inputfn, 'rt', encoding='UTF-8') as fobj:
            for l in fobj.readlines():
                ret = l.strip()
        return ret

    def parse_date_format1(self, ds):
        ''' parse date format: 西元2023年12月25日 '''
        m = re.match(Solution.patterns[0], ds)
        if m:
            #print(m[1],m[2],m[3])
            self.lastdate = date(year=int(m[1]),month=int(m[2]),day=int(m[3]))
            print(self.lastdate)
            return self.lastdate

        print('[warn] cannot parse with format1...')
        return None

    def parse_date_format2(self, ds):
        ''' parse date in format 2 '''
        #print('parse date in format 2...')
        months = ['Nul', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        m = re.match(Solution.patterns[1], ds)
        if m:
            idx = months.index(m[2])
            print(f'{m[1]}  {m[2]}={idx}  {m[3]}')
            self.lastdate = date(year=int(m[3]),month=idx,day=int(m[1]))
            print(self.lastdate)
            return self.lastdate
        return None

    def parse_stampfile(self):
        ''' parse stamp file '''
        ln = self.get_thelastine()
        print(ln)
        still_try = True
        try_count = 0
        while still_try:
            if try_count > 3:
                break
            d = self.parse_date_format1(ln)
            try_count += 1
            if d:
                break
            d = self.parse_date_format2(ln)
            try_count += 1
            if d:
                break


    def action(self):
        ''' action '''
        self.parse_stampfile()
        if self.lastdate:
            if self.lastdate >= date.today() - self.offset:
                print('[INFO] later, no need to bother')
                sys.exit(-2)
            else:
                print('[INFO] earlier, suggest you refresh folder')
                sys.exit(0)
        print('fail to compare')
        sys.exit(-1)


    @classmethod
    def run(cls, argv=None):
        ''' run me '''
        if not argv:
            # give a default value
            argv = os.path.join('.', cls.TS)

        if not os.path.exists(argv):
            print('[fail] specified path not found:', argv)
            sys.exit(-1)

        obj = cls()
        obj.set_stampfile(argv)
        obj.action()

def main():
    ''' main '''
    # pass full path of latest.txt
    if len(sys.argv) > 1:
        Solution.run(sys.argv[1])
    else:
        Solution.run()

if __name__ == '__main__':
    main()
