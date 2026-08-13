#!/usr/bin/env python

'''
locate latest and recommend to refresh dl or not

try:
    dt = datetime.strptime(ds, '%a, %d %m %y %H:%M:%S %z')
    print(dt)
except ValueError:
    pass

'''

import argparse
import os
import re
import sys
from datetime import date, timedelta
from typing import ClassVar

from be_prepared import get_today

SUCCESS = 0
FILENOTFOUND = 1
NOTOLDENOUGH = 2
CANNOTPARSE = 3

class Solution:
    ''' class to parse and action '''
    TS = 'latest.txt'
    MINDIFF = 5
    months: ClassVar[list[str]] = ['Nul', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    selftest_cases: ClassVar[list[tuple[str, bool]]] = [
        ('西元2023年12月15日 (週五) 13時56分55秒 CST', True),
        ('西元2023年12月8日 (週一) 10時39分15秒 CST', True),
        ('Fri, 15 Dec 2023 11:02:34 +0800', True),
        ('cannot parse this line', False),
        ('Mon, 18 Dec 2023 09:52:56 +0800', True),
        ('Tue, 12 Dec 2023 14:47:55 +0800', True),
        ('Tue Dec  9 15:10:30 CST 2023', True),
        ('Thu Aug 13 10:20:30 CST 2026', True),
        ('Thu Aug  3 10:20:30 CST 2026', True),
        ('2026-08-13', True),
        ('2026-08-13 10:20:30', True),
        ('2026/08/13', True),
        ('2026-13-40', False),
        ('15 Dec 2023 11:02:34 +0800', True),
        ('Fri, 15 Dec 2023 11:02:34 -0500', True),
        ('Fri, 15 Dec 2023 11:02:34 CST', True),
    ]
    patterns: ClassVar[list[str]] = [
        # 西元2023年12月15日 (週五) 13時57分07秒 CST
        r'^西元(\d{4})年(\d+)月(\d+)日.*$',
        # Tue, 12 Dec 2023 14:47:55 +0800
        r'^\w+,\s+(\d+)\s+(\w+)\s+(\d+) \d+:\d+:\d+ \+\d+$',
        # Tue Dec 12 15:10:30 CST 2023
        r'^\w+\s+(\w+)\s+(\d+)\s+\d+:\d+:\d+ \w+ (\d+)$',
        # 2026-08-13 or 2026-08-13 10:20:30
        r'^(\d{4})-(\d{1,2})-(\d{1,2})(?:\s+\d+:\d+:\d+)?$',
        # 2026/08/13 or 2026/08/13 10:20:30
        r'^(\d{4})/(\d{1,2})/(\d{1,2})(?:\s+\d+:\d+:\d+)?$',
        # Fri, 15 Dec 2023 11:02:34 -0500 / 15 Dec 2023 11:02:34 +0800
        r'^(?:\w+,\s+)?(\d+)\s+(\w+)\s+(\d+)\s+\d+:\d+:\d+\s+[+-]\d{4}$',
        # Fri, 15 Dec 2023 11:02:34 CST / 15 Dec 2023 11:02:34 GMT
        r'^(?:\w+,\s+)?(\d+)\s+(\w+)\s+(\d+)\s+\d+:\d+:\d+\s+[A-Z]{2,5}$',
    ]

    def __init__(self) -> None:
        self.inputfn: str = ''
        self.lastdate: date | None = None
        self.offset: timedelta = timedelta(days=Solution.MINDIFF)
        self.quiet: bool = False
        self.verbose: bool = False

    def set_quiet(self, yesno: bool) -> None:
        ''' set quiet '''
        self.quiet = yesno

    def set_stampfile(self, p: str) -> None:
        ''' set path of stamp file '''
        if not self.quiet:
            print('set_stampfile:', p)
        self.inputfn = p

    def get_thelastine(self) -> str | None:
        ''' get the last line with content of a file '''
        if self.verbose:
            print(f'parsing: {self.inputfn}')
        lastline = None
        with open(self.inputfn, 'rt', encoding='UTF-8') as fobj:
            for ln in fobj:
                ln = ln.strip()
                if len(ln) > 0:
                    lastline = ln
        return lastline

    def parse_date_format1(self, ds: str) -> date | None:
        ''' parse date format: 西元2023年12月25日 '''
        m = re.match(Solution.patterns[0], ds)
        if m:
            # m[1]: year, m[2]: month, m[3]: day
            self.lastdate = date(year=int(m[1]),month=int(m[2]),day=int(m[3]))
            #print(self.lastdate)
            return self.lastdate

        #print('[warn] cannot parse with format1...')
        return None


    def compose_date_obj(self, y: str, m: str, d: str) -> date | None:
        ''' return a date obj from month name '''
        try:
            yyyy = int(y)
            mm = Solution.months.index(m)
            dd = int(d)
            self.lastdate = date(year=yyyy,month=mm,day=dd)
        except ValueError:
            self.lastdate = None
        return self.lastdate

    def compose_date_obj_num(self, y: str, m: str, d: str) -> date | None:
        ''' return a date obj from numeric month/day '''
        try:
            yyyy = int(y)
            mm = int(m)
            dd = int(d)
            self.lastdate = date(year=yyyy,month=mm,day=dd)
        except ValueError:
            self.lastdate = None
        return self.lastdate

    def parse_date_format2(self, ds: str) -> date | None:
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

    def parse_date_format3(self, ds: str) -> date | None:
        ''' parse date in numeric format '''
        m = re.match(Solution.patterns[3], ds)
        if m:
            return self.compose_date_obj_num(m[1], m[2], m[3])

        m = re.match(Solution.patterns[4], ds)
        if m:
            return self.compose_date_obj_num(m[1], m[2], m[3])
        return None

    def parse_date_format4(self, ds: str) -> date | None:
        ''' parse RFC-2822 style variants '''
        m = re.match(Solution.patterns[5], ds)
        if m:
            return self.compose_date_obj(m[3], m[2], m[1])

        m = re.match(Solution.patterns[6], ds)
        if m:
            return self.compose_date_obj(m[3], m[2], m[1])
        return None


    def parse_stampfile(self) -> None:
        ''' parse stamp file '''
        if not os.path.exists(self.inputfn):
            print('[FAIL] file not found:', self.inputfn)
            sys.exit(FILENOTFOUND)
        ln = self.get_thelastine()
        self.parse_line(ln)

    def parse_line(self, ln: str | None) -> date | None:
        ''' parse one line to date if possible '''
        self.lastdate = None
        if ln is None:
            return None
        d = self.parse_date_format1(ln)
        if d:
            return d
        d = self.parse_date_format2(ln)
        if d:
            return d
        d = self.parse_date_format3(ln)
        if d:
            return d
        return self.parse_date_format4(ln)

    def run_self_test(self) -> None:
        ''' parse built-in sample lines instead of latest.txt '''
        has_mismatch = False
        for ds, should_parse in Solution.selftest_cases:
            parsed = self.parse_line(ds)
            ok = parsed is not None
            if ok == should_parse:
                if not self.quiet:
                    if ok:
                        print(f'[PASS] {ds} -> {parsed}')
                    else:
                        print(f'[PASS] expected parse failure: {ds}')
                continue
            has_mismatch = True
            print(f'[FAIL] parse mismatch: {ds}')

        if has_mismatch:
            sys.exit(CANNOTPARSE)

    @classmethod
    def export_selftest_cases(cls, filepath: str) -> None:
        ''' export built-in sample strings to a file '''
        with open(filepath, 'wt', encoding='UTF-8') as fobj:
            fobj.writelines(f'{ds}\n' for ds, _ in cls.selftest_cases)

    def show_msg(self, msg: str) -> None:
        ''' show message '''
        if not self.quiet:
            print(msg)

    def action(self) -> None:
        ''' action '''
        #self.show_msg('action')
        self.parse_stampfile()
        if self.lastdate:
            if self.lastdate >= get_today() - self.offset:
                self.show_msg(f'[INFO] {self.lastdate} rather new, no need to bother')
                sys.exit(NOTOLDENOUGH)
            else:
                self.show_msg(f'[INFO] {self.lastdate} old enough, ok to refresh')
                return
        self.show_msg('[fail] cannot parse the last date')
        sys.exit(CANNOTPARSE)


    @classmethod
    def run(cls, argv: str = '') -> None:
        ''' run me '''
        obj = cls()
        obj.set_stampfile(argv)
        obj.action()

def start_solution(files: list[str], isquiet: bool, is_self_test: bool,
                   is_export_selftest: bool, export_path: str) -> None:
    ''' control flow '''
    # if not isquiet:
    #     print('files:', files)
    obj = Solution()
    obj.set_quiet(isquiet)

    if is_export_selftest:
        Solution.export_selftest_cases(export_path)
        if not isquiet:
            print(f'[INFO] exported self-test cases to: {export_path}')
        return

    if is_self_test:
        obj.run_self_test()
        return

    if len(files) < 1:
        default_file = os.path.join('.', Solution.TS)
        if os.path.exists(default_file):
            files.append(default_file)
        else:
            user_input = input('Input file path: ').strip()
            if len(user_input) < 1:
                print('[FAIL] no input file given')
                sys.exit(FILENOTFOUND)
            files.append(user_input)

    for f in files:
        obj.set_stampfile(f)
        obj.action()

def main() -> None:
    ''' main '''
    parser = argparse.ArgumentParser(description='from given input file, tell if refresh or not')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("files", metavar='fn', type=str, nargs='*',
        help="file1 file2 file3 ...")
    #parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    parser.add_argument("-q", "--quiet", action='store_true', default=False,
        help='quiet, use return code to judge')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    parser.add_argument("--self-test", action='store_true', default=False,
        help='run parser self-test with built-in sample strings')
    parser.add_argument("--export-test-cases", action='store_true', default=False,
        help='export built-in self-test case strings to a text file and exit')
    parser.add_argument("--export-path", type=str, default=Solution.TS,
        help='output path for --export-test-cases (default: latest.txt)')
    # define the required args
    #requiredNamed = parser.add_argument_group('required named arguments')
    #requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    start_solution(args.files, args.quiet, args.self_test,
                   args.export_test_cases, args.export_path)

    # to show help message directly
    #parser.print_help()

if __name__ == '__main__':
    main()
