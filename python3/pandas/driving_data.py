#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# disable=import-error
# disable=wrong-import-order
# pylint: disable=wrong-import-position

'''
read driving data table (at google drive) and calculate stastics
(or read it from csv file offline)
'''

import argparse
import os
import sys
from datetime import date
from math import floor
import numpy as np

try:
    import pandas as pd
except ImportError:
    print('[ERROR] cannot import module pandas...')
    sys.exit(1)

try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False

from strutil import print_sep, sec2mmss, str2sec
from working_days import LoadWorkingDays

sys.path.insert(0, "..")
sys.path.insert(0, "../../")
from myutil import query_url_for_data, read_jsonfile, isfile, die
from myutil import MyDebug, MyVerbose, DefaultConfig

TMP_CSV = '/tmp/__driving_datasheet__.csv'

def do_nothing(*args):
    ''' do nothing '''
    print(*args)

logd = do_nothing
logi = do_nothing
if USE_LOGURU:
    logd = logger.debug
    logi = logger.info

class MySimpleout():
    ''' my verbose '''
    def __init__(self, simpleout):
        self._simpleout = simpleout

    @property
    def simpleout(self) -> bool:
        ''' simpleout of notification '''
        return self._simpleout
    @simpleout.setter
    def simpleout(self, val: bool):
        ''' setter of simpleout '''
        self._simpleout = val

class DriveConfig(MyDebug):
    ''' class helps to read config '''

    DEFAULT_FN = 'driving_data.json'

    def __init__(self):
        super().__init__(False) # MyDebug
        self.jsonpath = None
        self.data = None
        self.url = None
        self._tag = ''

    def _log(self, *args, **wargs):
        ''' my own log '''
        wargs['tag'] = self._tag
        self.logd(*args, **wargs)

    def compose_url(self):
        ''' compose url '''
        part1 = 'https://docs.google.com/spreadsheets/d/'
        part2 = '/gviz/tq?tqx=out:csv&sheet='
        self._tag = 'compose_url'

        if self.data is None:
            self._log('data is None')
            raise ValueError

        docid = self.data.get('docid', '')
        sheetid = self.data.get('sheetid', '')
        url = part1 + docid + part2 + sheetid
        self._log(f'url: {url}')
        self.url = url
        return url

    def read_setting(self, conf_file):
        ''' read setting '''
        self._tag = 'read_setting'
        self._log('enter...')

        if conf_file:
            self.jsonpath = conf_file
        else:
            self.jsonpath = DefaultConfig(self.DEFAULT_FN).get_default_config()
        if self.jsonpath is None or not isfile(self.jsonpath):
            msg = f"need config file: {self.DEFAULT_FN}"
            raise FileNotFoundError(msg)

        print(f'[INFO] using config: {self.jsonpath}')
        self.data = read_jsonfile(self.jsonpath)
        self.compose_url()

        if self.debug:
            self.dump_setting()
        return self.data

    def get_data(self):
        ''' get data '''
        return self.data

    def get_url(self):
        ''' get url '''
        return self.url

    def get_default_local(self):
        ''' get default local csv file path '''
        return self.data.get("default_localdata")

    def dump_setting(self):
        ''' dump settings '''
        print('dump class DriveConfig:')
        print('jsonpath:', self.jsonpath)
        print(f'{self.data=}')
        print(f'{self.url=}')


class DrivingData(MyDebug, MyVerbose, MySimpleout):
    ''' fetch driving data from gdrive or local csv '''

    def __init__(self,debug=False,verbose=False,simpleout=False):
        super().__init__(debug) # mydebug
        MyVerbose.__init__(self, verbose)
        MySimpleout.__init__(self, simpleout)

        self.csvfile = ''
        self.url = ''
        self.default_local = ''
        self.outputs = {}
        self._tag = 'DrivingData'

    def _log(self, *args, **wargs):
        ''' my own log '''
        wargs['tag'] = self._tag
        self.logd(*args, **wargs)

    def set_csvfile(self, csvfile):
        ''' setter csvfile '''
        if csvfile:
            self.csvfile = csvfile
        else:
            self.csvfile = TMP_CSV

    def read_setting(self, conf_file):
        ''' read settings '''
        dc = DriveConfig()
        dc.read_setting(conf_file)
        self.url = dc.get_url()
        self.default_local = dc.get_default_local()
        if self.debug:
            dc.dump_setting()

    def apply_local(self):
        ''' key: default_localdata'''
        self._tag = 'apply_local'
        self._log(f'default_local: {self.default_local}')
        self.set_csvfile(self.default_local)

    def request_data(self):
        ''' request data and output to a csv file'''
        self._tag = 'request_data'
        self._log('enter...')

        csvdata = query_url_for_data(self.url)
        if not self.csvfile:
            die('[ERROR] MUST specify csvfile path before calling request_data()')
            sys.exit(1)

        with open(self.csvfile, 'wb') as ofile:
            ofile.write(csvdata)
            self._log(f'output csv to {self.csvfile}')

    @staticmethod
    def str2date(s):
        ''' date string to date object
            [in] 2020-01-01
        '''
        arr = s.split('-')
        try:
            vals = [int(x) for x in arr]
        except ValueError:
            print('[ERROR] str2date: invalid string to integer:', s)
            return None
        return date(vals[0], vals[1], vals[2])

    @staticmethod
    def get_between_dates(start, end) -> str:
        ''' get dates between
            [in] str start date 2020-01-01
            [out] str end date 2020-02-29
        '''
        start_date = DrivingData.str2date(start)
        end_date = DrivingData.str2date(end)
        ddiff = end_date - start_date
        return str(ddiff.days)

    def extra_header(self):
        ''' show extra header '''
        if self.verbose:
            print(f"[INFO] panda version: {pd.__version__}")
        print(f'[INFO]    first date: {self.outputs["first"]}')
        print(f'[INFO]     last date: {self.outputs["last"]}')
        print(f'[INFO]   during days: {self.outputs["during"]}')

    def show_workingdays(self):
        ''' show working days '''
        if self.verbose:
            wd = LoadWorkingDays()
            for y in range(2021,2024+1):
                print(wd.get_msg(y))

    def action(self):
        ''' main function '''
        # read csv file as dataframe
        data = pd.read_csv(self.csvfile)
        duration = data['duration']

        dates = []
        secs = []
        for ii, ds in enumerate(data['date']):
            try:
                v = duration[ii]
                if isinstance(v, float):
                    # data exists at col "date", but empty at col "duration"
                    #print('float?')
                    break
                dates.append(ds)
                secs.append(str2sec(v))
            except ValueError:
                print(f'[ERROR] at {ii} on {ds}, invalid format: {duration[ii]}')
                return

        self.outputs['first'] = dates[0]
        self.outputs['last'] = dates[-1]
        self.outputs['during'] = DrivingData.get_between_dates(dates[0], dates[-1])

        if len(dates) != len(secs):
            print(f'[ERROR] not the same length {len(dates)} vs {len(secs)}')
            return

        ndict = {"date": dates, "seconds": secs}
        res = pd.DataFrame(ndict)
        des = res.describe()
        self._log('item:', des)
        self.fill_outputs(des)

    def do_show(self):
        ''' do show '''
        if self.simpleout:
            self.show_simplecsv()
        else:
            self.show_details()

    def fill_outputs(self, des):
        ''' fill results in outputs (dict) '''
        self._tag = 'fill_outputs'
        self._log('enters...')
        self.outputs['today'] = date.today()
        ans = peek_target(des, "count")
        count = str(int(floor(ans)))
        self.outputs['count'] = count
        the_vars = {}
        for q in ['max', '75%', 'mean', '50%', '25%', 'min', 'std']:
            ans = peek_target(des, q)
            the_vars[q] = ans
            mmss = sec2mmss(ans)
            self.outputs[q] = mmss
        self.fill_pois(the_vars)

    def show_simplecsv(self):
        ''' csv output '''
        for k,v in self.outputs.items():
            print(f'"{k}", "{v}"')

    def show_details(self):
        ''' show details of res² '''
        self.extra_header()
        self.show_workingdays()
        print_sep()
        for k in ['count', 'max', '75%', 'mean', '50%', '25%', 'min', 'std']:
            v = self.outputs[k]
            if k == "count":
                result = v
                j = result.rjust(9, ' ')
            else:
                try:
                    secs = str2sec(v)
                    result = f'{v}  ({secs:4.0f})'
                    j = result.rjust(20, ' ')
                except ValueError:
                    logd(f'[FAIL] at {k=} {v=}')
                    logi('[INFO] some data line is incorrect,',
                          'download the csv and run ```check_csv.py```')
                    continue
            print(f'{k:10s}: {j:20s}')
        print_sep()
        self.show_poi()

    def fill_pois(self, the_vars):
        ''' some interesting data '''
        self._tag = 'fill_pois'
        self._log('enter...')

        m = the_vars['mean']
        s = the_vars['std']

        opts = []
        t = f'mu = {m}, sigma = {s}'
        opts.append(t)
        mn = self.outputs['min']
        mx = self.outputs['max']
        mm = sec2mmss(m)
        t = f'min({mn})---mean({mm})---max({mx})'
        opts.append(t)
        (L1, R1) = (sec2mmss(m-s), sec2mmss(m+s))
        t = f'68.2%: {L1}--{mm}--{R1}'
        opts.append(t)
        (L2, R2) = (sec2mmss(m-2*s), sec2mmss(m+2*s))
        t = f'95.4%: {L2}--{mm}--{R2}'
        opts.append(t)
        self._log('opts:', opts)
        self.outputs['opts'] = opts


    def show_poi(self):
        ''' show some values (extra) '''
        self._tag = 'show_poi'
        self._log('verbose:', self.verbose)
        self._log('outputs:', self.outputs)
        if not self.verbose:
            return
        print('# more verbose....')
        for t in self.outputs.get('opts'):
            print(t)

# return type: numpy.float64
def peek_target(desc_table, target):
    ''' peek target '''
    #print('desc_table:', desc_table)
    desc_list = desc_table.index.tolist()
    try:
        midx = desc_list.index(target)
        mean_value = desc_table.iloc[midx, 0]
        #result = sec2str(mean_value)
        result = np.int64(mean_value)
        #print(f'{result=}, {type(result)=}')
        return result
    except ValueError as e:
        print(f'WARN: ValueError: {e.args}')
    return ''


def perform_show_driving_data(args):
    ''' universal starter '''
    in_file = args.input
    out_file = args.output
    conf_file = args.conf
    simpleout = args.excel
    verbose = args.verbose

    # if no config specified in cli parameters
    if not conf_file:
        # try environment variable
        r = os.getenv('DRIVING_CONFIG')
        if r:
            conf_file = r

    obj = DrivingData(verbose=verbose, simpleout=simpleout)
    # use local file (higher priority), no need out_file and conf_file
    if in_file:
        print('[INFO] input file from:', in_file)
        obj.set_csvfile(in_file)
    elif args.local:
        if not conf_file:
            print('[FAIL] specify local file, MUST specify config file')
            sys.exit(1)
        obj.read_setting(conf_file)
        obj.apply_local()
    else:   # request remote file
        print('[INFO] request data from google drive...')
        obj.set_csvfile(out_file)
        obj.read_setting(conf_file)
        obj.request_data()

    obj.action()
    obj.do_show()

def show_curios():
    ''' show some readme '''
    msg = '''
# some curios for normal distribution (only right side of μ)
0~1σ = 34.1%
1σ~2σ = 13.6% (acc: 47.7%, ±2σ: 95.4%)
2σ~3σ = 2.1%  (acc: 49.8%, ±4σ: 99.6%)
3σ~   = 0.1%  (acc: 49.9%)
'''
    print(msg)

def show_parameters(parser):
    ''' show parameters content '''
    print('[INFO] show parameters only, need `--run` to real work, dump...\n')
    args = parser.parse_args()
    has_parameter = False
    if args.input:
        print('input:', args.input)
        has_parameter = True
    if args.output:
        print('output:', args.output)
        has_parameter = True
    if args.conf:
        print('conf:', args.conf)
        has_parameter = True
    if args.excel:
        print('excel:', args.excel)
        has_parameter = True

    # to show help message directly
    if has_parameter is False:
        parser.print_help()


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='parsing driving data at google drive',
                                     epilog='''
set environment var DRIVING_CONFIG to specify config file, for example:
export DRIVING_CONFIG=driving_data.json''', usage='driving_data.py --run')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument('-i', '--input', help='Specify local datasheet, '
                        'will ignore output and config files')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-c', '--conf', help='Specify config for google drive (json format)')
    parser.add_argument("-l", "--local", action='store_true', default=False,
        help='must use -c if apply -l, tell script use the default local data sheet')
    parser.add_argument("--run", action='store_true', default=False,
        help='Specify this parameter to run actually')
    parser.add_argument("-x", "--excel", action='store_true', default=False,
        help='just print data, easy to paste to spreadsheets')
    parser.add_argument("-s", "--sigma", action='store_true', default=False,
        help='show some curios about normal distribution')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')

    #parser.parse_args(['-i input.csv -o out.csv'])
    args = parser.parse_args()

    if args.sigma:
        show_curios()
        return

    if not args.run:
        show_parameters(parser)
        return

    perform_show_driving_data(args)


if __name__ == '__main__':
    main()
