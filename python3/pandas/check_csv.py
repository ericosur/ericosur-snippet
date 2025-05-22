#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
check the format of csv, esp. the time
'''

import argparse
import os
import sys
import re

def logd(*args, **wargs) -> None:
    ''' logd '''
    if CheckCsv.debug:
        print(*args, **wargs)

class CheckCsv():
    ''' check csv for time string format '''
    debug = False

    def __init__(self):
        ''' init '''
        self.tb = {}

    @classmethod
    def run(cls) -> None:
        ''' run '''
        parser = argparse.ArgumentParser(description='check csv and validate the format',
                                        epilog='give csv filename')
        parser.add_argument('-i', '--input', dest="csvfn", help='Specify local datasheet, '
                            'will ignore output and config files')
        parser.add_argument("-d", "--debug", action='store_true', default=False,
                            help='deubg mode')

        args = parser.parse_args()
        obj = cls()
        obj.action(args)

    def action(self, args: argparse.Namespace) -> None:
        ''' action '''
        CheckCsv.debug = args.debug
        logd('CheckCsv.action...')
        csvfn = "t.csv"
        if args.csvfn:
            csvfn = args.csvfn
        if not os.path.isfile(csvfn):
            print(f'[FAIL] file not found: {csvfn}')
            sys.exit(1)
        self.read_file(csvfn)
        logd(f'size: {len(self.tb)}')
        self.check_table()

    def read_file(self, fn: str) -> None:
        ''' check csv '''
        logd(f'read_file: {fn}')
        with open(fn, "rt", encoding="UTF-8") as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                if "date" in ln and "duration" in ln:
                    # pass this line
                    continue
                pattern = r'\"(\d{4}-\d{2}-\d{2})\",\"([^\"]*)\",\"[^\"]*\",\"[^\"]*\"'
                m = re.match(pattern, ln)
                if m:
                    # m[1]: date, m[2]: time string
                    k, v = m[1], m[2]
                    self.tb[k] = v
                else:
                    print(ln)


    def check_table(self) -> None:
        ''' check self.tb '''
        p = r'\d{2,}:\d{2}\.\d{2}'
        for k,v in self.tb.items():
            if not v:
                continue
            m = re.match(p, v)
            if not m:
                print(f'Possible error at {k}: {v}')

def main():
    ''' main '''
    CheckCsv.run()

if __name__ == "__main__":
    main()
