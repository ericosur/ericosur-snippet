#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=consider-using-with

'''
get the correct relative time from klog
<6>[   21.610937] ddd: timestamp 1970-01-10 02:04:37.818

such special kernel log is only for Z
'''

import argparse
import os
import subprocess
from itertools import islice
import re
from datetime import datetime, timedelta

class Toolbox():
    ''' toolbox to process log '''

    def __init__(self, files, number):
        self.files = files
        self.start_line = number

    @staticmethod
    def get_nth_line_from_file(fn, line_num):
        '''
        get nth line from file, start from 1, not 0
        https://www.rosettacode.org/wiki/Read_a_specific_line_from_a_file#Python
        '''
        if line_num == 0:
            return None
        line = None
        with open(fn, "rt", encoding='utf-8') as f:
            try:
                line = next(islice(f, line_num - 1, line_num))
            except StopIteration as e:
                print(e)
        return line.strip()

    @staticmethod
    def get_several_lines_from_file(fn, line_start, count):
        '''
        line count from 1, not 0
        fn: file to read
        line_start: first the to fetch
        count: line count to fetch

        for example, get_several_lines_from_file('abc.log', 1785, 15)
        will fetch from 'abc.log' line 1785 to 1799
        https://www.rosettacode.org/wiki/Read_a_specific_line_from_a_file#Python
        '''
        if line_start == 0:
            return None
        ret = ""
        line_stop = line_start + count - 1
        with open(fn, "rt", encoding='utf-8') as f:
            try:
                lines = islice(f, line_start - 1, line_stop)
                #print(lines)
                for ln in lines:
                    ret = ret + ln
            except StopIteration as e:
                print(e)
        return ret

    @staticmethod
    def wccount(filename):
        ''' external __wc -l__ '''
        out = subprocess.Popen(['/usr/bin/wc', '-l', filename],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT
                               ).communicate()[0]
        return int(out.partition(b' ')[0])

    @staticmethod
    def head1(filename):
        ''' external __head -1__ '''
        out = subprocess.Popen(['/usr/bin/head', '-1', filename],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT
                               ).communicate()[0]
        res = out.decode('utf-8')
        print('head1:', res)
        return res

    @staticmethod
    def tail1(filename):
        ''' external __head -1__ '''
        out = subprocess.Popen(['/usr/bin/tail', '-1', filename],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT
                               ).communicate()[0]
        res = out.decode('utf-8')
        print('tail1:', res)
        return res

    def open_file(self, fn):
        ''' open and read file '''
        with open(fn, 'rt', encoding='utf-8') as fin:
            fileobj = fin.readlines()
            self.parse_log(fileobj)


    def parse_log(self, fileobj):
        '''
        parse __ddd__ line ==>
        <6>[   21.610937] ddd: timestamp 1970-01-10 02:04:37.818
        '''
        cnt = 0
        oldupt = -1
        #ret_delta = None
        for ln in fileobj:
            cnt += 1
            m = re.findall(r'^<\d+>\[\s*(\d+)\.(\d+)\] (.*)$', ln)
            if m:
                uptis = int(m[0][0])
                uptus = int(m[0][1])
                upt = float(m[0][0] + '.' + m[0][1])

                if upt < oldupt:
                    print(f"[WARN] uptime got smaller at {cnt} line:\n{ln}")
                oldupt = upt

                msg = m[0][2]
                if len(msg) == 0:
                    print(f"<no msg?> [{upt}] {msg}")
                else:
                    ret = self.parse_ddd(msg, uptis, uptus)
                    if ret:
                        print(f"{cnt} [kdate]: {ln}", end='')
                        #ret_delta = ret

            else:
                print("{cnt} [kdate]: {ln}")

    def parse_ddd(self, msg, uptis, uptus):
        '''
        parse __ddd__ line ==>
        <6>[   21.610937] ddd: timestamp 1970-01-10 02:04:37.818
        '''
        m = re.findall(r'^ddd: timestamp (\d{4})-(\d+)-(\d+) (\d+):(\d+):(\d+)\.(\d+)$', msg)
        if m:
            delta = timedelta(seconds=uptis, microseconds=uptus)
            us = int(float(m[0][-1]) * 1000)
            yy, MM, dd, hh, mm, ss = [int(x) for x in m[0][:-1]]

            #print("{} [kdate]: {}".format(cnt, ln), ends='')
            #print(hh, mm, ss, us)
            dt = datetime(yy, MM, dd, hh, mm, ss, microsecond=us)
            #print(uptis, uptus)
            #print(dt, delta)
            print(f"[kdate] delta: {delta}")
            return dt, delta

        return None


    def action(self):
        ''' process '''
        for ff in self.files:
            if not os.path.exists(ff):
                continue

            print(f"[kdate] {ff}:")
            self.open_file(ff)


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='brief description for this script')
    parser.add_argument("files", metavar='file', type=str, nargs='+',
        help="show these strings")
    parser.add_argument("-n", "--number", type=int, help='search from line number')
    parser.add_argument("-v", "--verbose", action='store_true', help='verbose')
    args = parser.parse_args()

    #print(args.files)
    if args.verbose:
        print('verbose on')

    number = 1
    if args.number:
        print('args.number:', args.number)
        number = args.number

    tb = Toolbox(args.files, number)
    tb.action()


if __name__ == '__main__':
    main()
